from bc4py import __version__, __chain_version__
from bc4py.config import C, V, P
from bc4py.chain.utils import GompertzCurve
from bc4py.chain.difficulty import get_bits_by_hash, get_pos_bias_by_hash
from bc4py.database.create import closing, create_db
from bc4py.database.builder import builder, tx_builder
from bc4py.database.keylock import is_locked_database
from bc4py.database.tools import get_validator_info
from bc4py.user.api import web_base
from binascii import hexlify
import time

MAX_256_INT = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
start_time = int(time.time())

__api_version__ = '0.0.1'


async def chain_info(request):
    best_height = builder.best_block.height
    best_block = builder.best_block
    old_block_height = builder.best_chain[0].height - 1
    old_block_hash = hexlify(builder.get_block_hash(old_block_height)).decode()
    data = best_block.getinfo()
    pos_bias = get_pos_bias_by_hash(previous_hash=best_block.previous_hash)[1]
    pos_target = get_bits_by_hash(previous_hash=best_block.previous_hash, consensus=C.BLOCK_POS)[1]
    pow_target = get_bits_by_hash(previous_hash=best_block.previous_hash, consensus=C.BLOCK_POW)[1]
    data['difficulty'] = {
        'pos': round(MAX_256_INT / pos_target / 100000000, 6),
        'pow': round(MAX_256_INT / pow_target / 100000000, 6),
        'bias': pos_bias,
        'hashrate(Mh/s)': round(MAX_256_INT/pow_target/V.BLOCK_TIME_SPAN/1000000, 3)}
    data['size'] = best_block.getsize()
    data['checkpoint'] = {'height': old_block_height, 'blockhash': old_block_hash}
    data['money_supply'] = GompertzCurve.calc_total_supply(best_height)
    data['total_supply'] = GompertzCurve.k
    return web_base.json_res(data)


async def system_info(request):
    with closing(create_db(V.DB_ACCOUNT_PATH)) as db:
        cur = db.cursor()
        data = {
            'system_ver': __version__,
            'api_ver': __api_version__,
            'chain_ver': __chain_version__,
            'booting': P.F_NOW_BOOTING,
            'connections': len(V.PC_OBJ.p2p.user),
            'unconfirmed': [hexlify(txhash).decode() for txhash in tx_builder.unconfirmed.keys()],
            'directory': V.DB_HOME_DIR,
            'encryption': '*'*len(V.ENCRYPT_KEY) if V.ENCRYPT_KEY else V.ENCRYPT_KEY,
            'mining': {
                'address': V.MINING_ADDRESS,
                'message': V.MINING_MESSAGE,
                'status': bool(V.MINING_OBJ),
                'threads': V.MINING_OBJ.getinfo() if V.MINING_OBJ else None},
            'staking': {
                'status': bool(V.STAKING_OBJ),
                'threads': V.STAKING_OBJ.getinfo() if V.STAKING_OBJ else None},
            'locked': is_locked_database(cur),
            'validator_address': V.CONTRACT_VALIDATOR_ADDRESS,
            'access_time': int(time.time()),
            'start_time': start_time}
    return web_base.json_res(data)


async def validator_info(request):
    try:
        validator_cks, required_num = get_validator_info()
        return web_base.json_res({
            'validator_address': V.CONTRACT_VALIDATOR_ADDRESS,
            'validators': list(validator_cks),
            'all': len(validator_cks),
            'require': required_num})
    except BaseException:
        return web_base.error_res()


__all__ = [
    "chain_info", "system_info", "validator_info"
]
