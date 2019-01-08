from bc4py.config import C, V, BlockChainError
from bc4py.user import Accounting
from bc4py.database.create import closing, create_db
from time import time
import os
from binascii import hexlify
from bc4py.user.utils import extract_keypair
from weakref import ref
import logging


def read_txhash2log(txhash, cur):
    d = cur.execute("""
        SELECT `type`,`user`,`coin_id`,`amount`,`time` FROM `log` WHERE `hash`=?
    """, (txhash,)).fetchall()
    if len(d) == 0:
        return None
    movement = Accounting()
    _type = _time = None
    for _type, user, coin_id, amount, _time in d:
        movement[user][coin_id] += amount
    return MoveLog(txhash, _type, movement, _time)


def read_log_iter(cur, start=0):
    d = cur.execute("SELECT DISTINCT `hash` FROM `log` ORDER BY `id` DESC").fetchall()
    c = 0
    for (txhash,) in d:
        if start <= c:
            yield read_txhash2log(txhash, cur)
        c += 1


def insert_log(movements, cur, _type=None, _time=None, txhash=None):
    assert isinstance(movements, Accounting), 'movements is Accounting.'
    _type = _type or C.TX_INNER
    _time = _time or int(time() - V.BLOCK_GENESIS_TIME)
    txhash = txhash or (b'\x00' * 24 + _time.to_bytes(4, 'big') + os.urandom(4))
    move = list()
    index = 0
    for user, coins in movements.items():
        for coin_id, amount in coins:
            move.append((txhash, index, _type, user, coin_id, amount, _time))
            index += 1
    cur.executemany("""INSERT INTO `log` (`hash`,`index`,`type`,`user`,`coin_id`,
    `amount`,`time`) VALUES (?,?,?,?,?,?,?)""", move)
    return txhash


def delete_log(txhash, cur):
    cur.execute("""DELETE FROM `log` WHERE `hash`=?
    """, (txhash,))


def read_address2keypair(address, cur):
    d = cur.execute("""
        SELECT `id`,`sk`,`pk` FROM `pool` WHERE `ck`=?
    """, (address,)).fetchone()
    if d is None:
        raise BlockChainError('Not found address {}'.format(address))
    uuid, sk, pk = d
    assert len(sk) == 32, 'Not correct length of SecretKey {}bytes'.format(len(sk))
    return uuid, sk.hex(), pk.hex()


def read_address2user(address, cur):
    user = cur.execute("""
        SELECT `user` FROM `pool` WHERE `ck`=?
    """, (address,)).fetchone()
    if user is None:
        return None
    return user[0]


def insert_keypair(keypair, cur):
    sk, pk, ck, user, _time = keypair
    assert isinstance(sk, bytes) and isinstance(pk, bytes) and isinstance(ck, str) and isinstance(user, int)
    cur.executemany("""
    INSERT INTO `pool` (`sk`,`pk`,`ck`,`user`,`time`) VALUES (?,?,?,?,?)
    """, keypair)


def read_account_info(user, cur):
    d = cur.execute("""
        SELECT `name`,`description`,`time` FROM `account` WHERE `id`=?
    """, (user,)).fetchone()
    if d is None:
        return None
    name, description, _time = d
    return name, description, _time


def read_pooled_address_iter(cur):
    cur.execute("SELECT `id`,`ck`,`user` FROM `pool`")
    return cur


def read_address2account(address, cur):
    user = read_address2user(address, cur)
    if user is None:
        raise BlockChainError('Not found account {}'.format(address))
    return read_account_info(user, cur)


def read_name2user(name, cur):
    assert isinstance(name, str)
    d = cur.execute("""
        SELECT `id` FROM `account` WHERE `name`=?
    """, (name,)).fetchone()
    if d is None:
        return create_account(name, cur)
    return d[0]


def read_user2name(user, cur):
    assert isinstance(user, int)
    d = cur.execute("""
        SELECT `name` FROM `account` WHERE `id`=?
    """, (user,)).fetchone()
    if d is None:
        raise Exception('Not found user id. {}'.format(user))
    return d[0]


def create_account(name, cur, description="", _time=None, is_root=False):
    assert isinstance(name, str)
    if not (name.startswith('@') == is_root):
        raise BlockChainError('prefix"@" is root user, is_root={} name={}'.format(is_root, name))
    _time = _time or int(time() - V.BLOCK_GENESIS_TIME)
    cur.execute("""
        INSERT INTO `account` (`name`,`description`,`last_index`,`time`) VALUES (?,?,?,?)
    """, (name, description, 0, _time))
    d = cur.execute("SELECT last_insert_rowid()").fetchone()
    return d[0]


def create_new_user_keypair(name, cur):
    assert isinstance(name, str)
    # get last_index
    user = read_name2user(name, cur)
    d = cur.execute("""
    SELECT `last_index` FROM `account` WHERE `id`=?
    """, (user,)).fetchone()
    last_index = d[0]
    # check the keypair is used
    while True:
        sk, pk, ck = extract_keypair(user=user, is_inner=False, index=last_index)
        last_index += 1
        if read_address2user(address=ck, cur=cur) is None:
            break
    insert_keypair(keypair=(sk, pk, ck, int(time())), cur=cur)
    # update last_index
    cur.execute("""
    UPDATE `account` SET `last_index`=? WHERE `id`=?
    """, (last_index, user))
    return ck


class MoveLog:
    __slots__ = ("txhash", "type", "movement", "time", "tx_ref")

    def __init__(self, txhash, _type, movement, _time, tx=None):
        self.txhash = txhash
        self.type = _type
        self.movement = movement
        self.time = _time
        self.tx_ref = ref(tx) if tx else None

    def __repr__(self):
        return "<MoveLog {} {}>".format(C.txtype2name.get(self.type, None), hexlify(self.txhash).decode())

    def __hash__(self):
        return hash(self.txhash)

    def get_dict_data(self, outer_cur=None):
        with closing(create_db(V.DB_ACCOUNT_PATH)) as db:
            cur = outer_cur or db.cursor()
            movement = {read_user2name(user, cur): dict(balance) for user, balance in self.movement.items()}
        return {
            'txhash': hexlify(self.txhash).decode(),
            'height':  self.height,
            'recode_flag': self.recode_flag,
            'type': C.txtype2name.get(self.type, None),
            'movement': movement,
            'time': self.time + V.BLOCK_GENESIS_TIME}

    def get_tuple_data(self):
        return self.type, self.movement, self.time

    @property
    def height(self):
        if not self.tx_ref:
            return None
        try:
            return self.tx_ref().height
        except Exception:
            return None

    @property
    def recode_flag(self):
        if not self.tx_ref:
            return None
        try:
            return self.tx_ref().recode_flag
        except Exception:
            return None


__all__ = [
    "read_txhash2log", "read_log_iter", "insert_log", "delete_log",
    "read_address2keypair", "read_address2user", "insert_keypair",
    "read_account_info", "read_pooled_address_iter", "read_address2account",
    "read_name2user", "read_user2name", "create_account", "create_new_user_keypair",
    "MoveLog"
]
