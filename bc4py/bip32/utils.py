from bc4py.bip32.base58 import check_decode, check_encode
import hashlib


def is_address(ck, prefix):
    """check base58 decode and prefix"""
    try:
        raw = check_decode(ck)
    except ValueError:
        return False
    if prefix == raw[:1]:
        return True
    else:
        return False


def get_address(pk, prefix):
    """get address from public key"""
    identifier = hashlib.new('ripemd160', hashlib.sha256(pk).digest()).digest()
    return check_encode(prefix + identifier)


def convert_address(ck, prefix):
    """convert address's prefix"""
    raw = check_decode(ck)
    return check_encode(prefix + raw[1:])


def dummy_address(seed):
    assert len(seed) == 20
    return check_encode(b'\xff' + seed)


addr2bin = check_decode
bin2addr = check_encode


__all__ = [
    "is_address",
    "get_address",
    "convert_address",
    "dummy_address",
    "addr2bin",
    "bin2addr",
]


"""
0x0 1HqoNfpAJFMy9E36DBSk1ktPQ9o9fn2RxX
0x1 hBQMn7T1RpqxfBBEbn4VtAB2f46ULSFSC
0x2 26X1LtQjicHin6KGG27Nz1RxfAK36eGrHB
0x3 2VrcKzi2RnkbbXTMHSShU8hkHfZysgtVCH
0x4 2uCDK71K8yDUQxbSJrn1xFyXvApvb9m3Y6
0x5 3JXpJDJbr9gMEPjXLH7LSPFKYg5sK3cc6u
0x6 3hsRHKbtZL9E3pscMhSevWX7BBLoyKiCBT
0x7 47D2GRuBGWc6sG1hP7myQdntogbkiEBZxY
0x8 4WYdFYCTyh4ygh9nQY7Htm4gSBrhN4rN6e
0x9 4utEEeVkgsXrW8HsRxScNtLU4h7e9yngqc
0xa 5KDqDko3Q3zjKZRxTNmvs1cFhCNarbD3pw
0xb 5iZSCs6L7ETc8za3Uo7FM8t3KhdXVjNurq
0xc 67u3ByPcpQvUxRi8WDSZqG9pxCtUEQHqzX
0xd 6XEeB5guXbPMmrrDXdmtKPRcai9QvKogWG
0xe 6vaFABzCEmrEbHzJZ47CoWhQDDQMcqzWem
0xf 7Kur9JHUwxK7Qj8PaUSXHdyBqifJPUFzGE
0x10 7jFT8Qamf8mzEAGUbtmqmmEyUDvF65ABy6
0x11 88b47Wt4NKEs3bQZdK7AFtWm6jBBq2ncDN
0x12 8Xvf6dBM5Vhjs2YeejSUk1nYjES8XzQe8k
0x13 8wGG5jUdngAcgTgjg9moE94LMjh5Bmp7BS
0x14 9Lbs4qmvVrdVVtppha77iGL7zEx1wCJYpg
0x15 9jwU3x5DD36NKKxuizSSCPbuckCxfXvcey
0x16 A9H534NVvDZF8m6zkQmkgWshFFTuKYzoVP
0x17 AYcg2AfndQ27xCF5mq75Ae9Uskir32iUBP
0x18 AwxH1Gy5LaUzmdPAoFSPemRGWFynm4huvw
0x19 BMHszPGN3kwsb4XFpfmi8th48mEjTkT5A7
0x1a BkdUyVZekwQkQVfLr672d1xqmGVgEBu8e3
0x1b C9y5xbrwU7sdDvoRsWSM79EdPmkcspc59b
0x1c CZJgwiAEBJLW3MwWtvmfbGWR2H1ZbHRMot
0x1d CxeHvpTWtUoNro5bvM6z5PnCenGWM2AT6U
0x1e DMytuvkobfGFgEDgwmSJZX3zHHXT3DinKN
0x1f DmKVu346Jqj8VfMmyBmd3eKmunnPnwaDHH
0x20 EAf6t9MP22C1K6Vrzc6wXmbZYJ3LUnqNow
0x21 EZzhsFefjCet8Xdx22SG1tsMAoJH8jEND3
0x22 EyLJrMwxSP7kwxn33SmaW298oJZDuybvZu
0x23 FNfuqUFF9ZadmPv84s6tz9QvRopAYE5HAv
0x24 Fn1WpaYXrk3Waq4D6HSDUGgi4K57KsCw5f
0x25 GBM7ogqpZvWPQGCJ7hmXxPxVgpL4465ThB
0x26 Gagino97H6yGDhLP986rSXEHKKazhysFar
0x27 Gz2KmuSPzHS938UUAYSAveW4wpqwQV8jP8
0x28 HPMvm1jghTu1rZcZBxmVQmmraL6t7YjVYQ
0x29 HnhXk82yQeMtfzkeDP6otu3eCqMpsQfg9k
0x2a JC38jELG7ppmVRtjEoS8P2KRqLcmaJMkMf
0x2b JbNjiLdYq1HeJs2pGDmSs9bDTqsiJ8QAj4
0x2c JziLhSvqYBkX8JAuHe6mMGs16M8ewGU78f
0x2d KQ3wgZE8FNDPwjJzK4S5qQ8nirPbi24R6n
0x2e KoPYffXQxYgGmAT5LUmQKXQaMMeYQQTqEA
0x2f LCj9emphfj99abbAMu6ioegMyruVAmardc
0x30 Lc4kdt7zNuc2Q2jFPKS3Hmx9cNARmtzz5T
0x31 M1QMczRH664uDTsLQjmMmuDwEsRNX92Jc4
0x32 MQjxc6iZoGXn2u1RSA6gG2VisNgKFEN2Tg
0x33 Mp5ZbD1rWSzerL9WTaRzk9mWVswG1K6sDT
0x34 NDRAaKK9DdTXfmHbUzmKEH3J8PCCfLGHk6
0x35 NckmZRcRvovQVCRgWR6diQK5ktT9R8F6Ft
0x36 P26NYXuidzPHJdZmXqRxCXasPPi658RTMx
0x37 PRRyXeD1MArA84hrZFmGgerf1ty2p9E5NN
0x38 PpmaWkWJ4MK2wVqwag6bAn8SeQDyW7SmJ6
0x39 QE7BVroamXmukvz2c6RueuQEGuUvDB1XFg
0x3a QdSnUy6sUiEnaN87dWmE92g1uQjrvPgrWG
0x3b R2nPU5QABthfPoGCew6Yd9woXuzof55SnN
0x3c RS7zTBhSu5AYDEQHgMRs7HDbARFkKTDnmv
0x3d RqTbSHzjcFdR2fYNhmmBbQVNnvWh5SKA4F
0x3e SEoCRQJ2KS6Hr6gTjC6W5XmARRmdkrcZLi
0x3f Se8oQWbK2cZAfXpYkcRpZf2x3w2aYnDXMw
0x40 T3UQPctbjo23Uxxdn2m93nJjgSHXFx1NK1
0x41 TSp1NjBtSyUvJQ6ioT6TXuaXJwYTwcYERC
0x42 Tr9cMqVBA9wo7qEopsRn22rJwSoQg8nwrs
0x43 UFVDLwnTsLQfwGNtrHm6WA86Zx4MPZoQiM
0x44 UeppL45kaWsYkhWysi6QzHPtCTKJ3jbC5R
0x45 V4ARKAP3HhLRa8f4u8RjUQffpxaEmdT3zA
0x46 VTW2JGgKzsoJPZo9vYm3xXwTTTqBT76VCy
0x47 VrqdHNyci4GBCzwEwy6NSfDF5y68DsGzaa
0x48 WGBEGVGuREj42S5KyPRgvnV2iUM4s6LAah
0x49 WfWqFbaC8RBvqsDQzom1QukpLyc1ed8giT
0x4a X4rSEhsUqbeofJMW2E6Ku32byUrxK6TP4C
0x4b XUC3DpAmYn7gUjVb3eRePAJPbz7u3W7CYi
0x4c XsXeCvU4FxaZJAdg54kxsHaBEVNqiaxdjy
0x4d YGsFC2mLy93S7bmm6V6HMQqxrzdnRfm4qE
0x4e YgCrB94dgKWJw2ur7uRbqY7kVVtjCSC525
0x4f Z5YTAFMvPVyBkU3w9KkvKfPY819frWs7WQ
0x50 ZUt49MfD6gS4ZuC2Ak6EonfKkWQcXPFLoD
0x51 ZtDf8TxVortwPLL7CARZHuw7P1fZEk1QTw
0x52 aHZG7aFnX3MpCmUCDaksn3Cu1WvW1JFkgg
0x53 agts6gZ5EDph2CcHF16CGAUge2BSmSe7w9
0x54 b6EU5nrMwQHZqdkNGRRWkHkUGXSPUiPcHW
0x55 bVa54u9eeakSf4tTHqkqER2Fu2hL7ZXnm4
0x56 btug41SwMmDKUW2YKG69iYJ3XXxGq1ptnk
0x57 cJFH37kE4wgCHwAdLgRUCfZqA3DDbd7THW
0x58 chat2E3Wn8957NJiN6kngnqcnYUAH2rPca
0x59 d6vV1LLoVJbwvoSoPX67Av7QR3j6yCyDmS
0x5a dWG5zSe6CV4pkEatQwRRf3PC3Yz3hNrrRb
0x5b dubgyYwNufXhZfiySMkk9Aeyg4EzRKkwKM
0x5c eJwHxfEfcqzaP6s4Tn64dHvmJZVw9SkXLT
0x5d eiGtwmXxL2TTCY19VCRP7RCYw4ksoiLKKP
0x5e f7cVvsqF3CvL1y9EWckhbYULZa1pZpwMEy
0x5f fWx6uz8XkPPCqQHKY3625fk8C5GmCNVtEi
0x60 fvHhu6RpTZr5eqRQZTRLZo1upaXhys6Y4z
0x61 gKdJtCj7AkJxUGZVaskf3vHhT5neg4gjeg
0x62 gixusK2PsvmqHhhacJ5yY3ZV5b3bQTqFpT
0x63 h8JWrRKgb7Ei78qfdiRJ2AqGi6JY3x1HEP
0x64 hXe7qXcyJHhavZykf8kcWJ74LbZUpjBpsh
0x65 hvyipdvG1UATk17qgZ5vzRNqy6pRWGTu7s
0x66 iLKKokDYiedLZSFvhyRFUYedbc5NDVBLBN
0x67 ijevnrWqRq6DNsQ1jPkZxfvRE7LJtNY1TS
0x68 j8zXmxp891Z6CJY6kp5tSoCCrcbFfYcGaZ
0x69 jYL8m57QrC1y1jgBnERCvvTzV7rCN7EjeU
0x6a jwfjkBQhZNUqqApGoekXR3jn7d7957JYWX
0x6b kM1LjHhzGYwiebxMq55quB1Zk8N5k19Fns
0x6c kkLwiQ1GyjQbU36SrVRAPJHMNdd2TR3Xsw
0x6d m9gYhWJZgusUHUEXsukUsRZ918sy9FzPdg
0x6e mZ29gcbrQ6LM6uNcuL5oMYpvde8uxA1wjt
0x6f mxMkfiu97GoDvLWhvkR7qg6iG9PravnSLV
0x70 nMhMeqCRpTG6jmenxAkSKoNVteeoNf4ETF
0x71 nm2xdwViXdiyZCnsyb5koveHX9uk1MXtwB
0x72 oANZd3o1EpBrNdvy11R5J3v59fAgkoUWzA
0x73 oZiAcA6HwzejC5542RkPnBBrnARdToh4UW
0x74 oy3mbGPafB7c1WD93r5iGJTeQfgaED2i3s
0x75 pNPNaNgsNMaUpwME5GR2kRjS3AwWt8fZur
0x76 pmiyZUzA5Y3MeNVK6gkMEZ1DfgCTcnrmdc
0x77 qB4aYbHSniWETodQ875figH1JBTQGCS5DS
0x78 qaQBXhajVty7HEmV9XQzCoYnvgiM512vhc
0x79 qyjnWot2D5Rz6fuaAwkJgvpaZByHgEKJLp
0x7a rP5PVvBJvFtrv73fCN5dB46NBhEEUSGc8R
0x7b rnQzV2UbdSMjjYBkDnQwfBN9pCVBBRAj8H
0x7c sBkbU8mtLcpcYyKqFCkG9JdwShk7rs7JzC
0x7d sb6CTF5B3oHVNQTvGd5adRuj5D14Yhq2oK
0x7e szRoSMNTkykNBqc1J3Qu7ZBWhiG1KRWMqu
0x7f tPmQRTfkUADF1Gk6KTkDbgTJLDWx1JyBSH
0x80 to71QZy3BLg7phtBLt5Y5oj5ximtgnUrPg
0x81 uCScPgGKtX8ze92GNJQrZvzsbE2qPeuEuP
0x82 ubnDNnZcbhbsTaAMPikB44GfDjHn8XeQk3
0x83 v17pMtruJt4kH1JSR95VYBYSrEYiscicuF
0x84 vQTRM1AC24Xd6SSXSZQp2JpEUjofZA1psz
0x85 voo2L7TUjEzVusacTyk8WS627F4cGto3x4
0x86 wD8dKDkmSRTNjJihVQ5SzZMojkKYwAwiWd
0x87 wcUEJL449bvFYjrnWpQmUgdbNFaVhPKGxZ
0x88 x1oqHSMLrnP8NAzsYEk5xouNzkqSPZyQ9Z
0x89 xR9SGYedZxr1Bc8xZf5QSwBAdG6P4hxydh
0x8a xpV3FewvH9Jt13H3b5Qiw4SxFmMKpV6yHP
0x8b yDpeEmFCzKmkpUR8cVk3RBijtGcGZhfdov
0x8c ydAFDsYVhWEdduZDdv5MuJzXWmsDBdTc6v
0x8d z2VrCyqnQghWTLhJfLQgPSGK9H89zU3Ck6
0x8e zRqTC6957sAPGmqPgkjzsZY6mnP6egbprC
0x8f zqB4BCSMq3dG6CyUiB5KMgotQHe3NP9dei
0x90 21EWfAJjeYE68ue7ZjbQdqp5g2ntz4MHRdz
0x91 21drG9R2wFQZ1j5Fem1jxKwMTfJ9voxCmTP
0x92 223Bs8XLDxb1tYWPjnS5Gp4dFHoQsVHgGmD
0x93 22SXU7ddWfmUmMwXporQbJBu2vJfpAWWsrg
0x94 22qs56jvoNwweBNfuqGjunKApYovkwmYh4d
0x95 23FCg5rE668QWzoozrh5EGSScBKBheYgZ3q
0x96 23eYH4xXNoJsPpEx5t7QYkZiPopSeMqunSU
0x97 243st44pfWVLGdg6AuXjsEgzBSKhb3ut7mp
0x98 24TDV3B7xDfo9T7EFvx5BipFy4pxXnGhs4r
0x99 24rZ62HREvrG2GYNLxNQWCwXkhLDUVFsboo
0x9a 25Fth1PiXe2iu5yWRynjph4oYKqUR99vK4n
0x9b 25fEHzW1pMDBmuQeX1D59BC5KxLjMuGSv8w
0x9c 264ZtycK74Peeiqnc2dQTfKM7aqzJa94szt
0x9d 26TuVxicPma7XYGvh43jn9ScuDMFFMGhckp
0x9e 26sF6wpugUkaQMi4n5U56dZtgqrWC4DSdxk
0x9f 27GahvwCyBw3HB9Cs6tQR7hAUUMm8oGMBuB
0xa0 27fvJv3WFu7W9zaLx8JjjbpSG6s25UCP1YY
0xa1 285Fuu9oYcHy2p1V39j545wi3jNH29PsPp6
0xa2 28UbWtG6qKURudSd8B9QNa4yqMsXxqe7LKH
0xa3 28sw7sNQ82etnSsmDCZjh4CFczNnuZMR62i
0xa4 29HGirUhQjqMfGJuJDz51YKXQct3rG3yHbX
0xa5 29gcKqazhT1pY5k3PFQQL2SoCFPJny9GNRM
0xa6 2A5wvphHzACHQuBBUGpjeWa4ystZjhLAKEs
0xa7 2AVHXoobGsNkHicKZJF4xzhLmWPpgTNH4cZ
0xa8 2Atd8nutZaZDAY3TeKfQHUpcZ8u5dBiaP9j
0xa9 2BHxjn2BrHjg3MUbjM5jbxwtLmQLZobJsGY
0xaa 2BhJLm8V8zv8vAujpNW4vT5A8PubWb3R2kM
0xab 2C6dwkEnRi6bnzLsuPvQEwCRv2QrTFGFQtq
0xac 2CVyYjM5iRH4fon1zRLjZRKhhev7Q2PBbcL
0xad 2CuK9iTP18TXYdDA5Sm4suSyVHRNLfY2Bfv
0xae 2DJekhZgHqdzRSeJAUBQCPaFGuvdHPcpes4
0xaf 2DhzMgfyaYpTJG5SFVbjWshX4YRtEB5TEdf
0xb0 2E7KxfnGsFzvB5WaLX24qMpnrAw9Ao1YugY
0xb1 2EWfZeta9yBP3twiRYSQ9qx4doSQ7XgpeF2
0xb2 2Ev1AdzsSgMqviNrWZrjUL5LRRwf4HHqS5h
0xb3 2FKLmd7AjPYJoXozbbH4npCcD4Suzxzpgj3
0xb4 2FigNcDU26imgMF8gchQ7JKszgxAwgvogFB
0xb5 2G81ybKmJouEZAgGme7jRnT9nKTRtN6zH3a
0xb6 2GXMaaS4bX5hRz7QrfY4kGaRZwxgq86oNCw
0xb7 2GvhBZYMtEGAJoYYwgxQ4khhMaTwmoQtcQc
0xb8 2HL2nYefAwSdBcyh2iNjPEpy9CyCiXSRWez
0xb9 2HjNPXkxTed64SQq7jo4hixEvqUTfHDh8Eh
0xba 2J8hzWsFkMoYwFqyCmDQ2D5WiTyibxHe7dx
0xbb 2JY3bVyZ34z1p5H7HndjLhCnW6UyYdjvwUx
0xbc 2JwPCV5rKnAUgtiFNp44fBL4HizEVPKppdY
0xbd 2KLioUC9cVLwZi9PTqUPyfTL5MVVS5ec7Wt
0xbe 2Kk4QTJSuCXQSXaXYrtjJ9abryzkNnh6aQC
0xbf 2L9Q1SQkBuhsKM1fdtK4cdhsecW1KT1faoD
0xc0 2LYjcRX3UctLCASoiujPw7q9SF1GGCS8Gzg
0xc1 2Lx5DQdLmL4o4yswow9jFbxRDsWXCsZh7tK
0xc2 2MMQpPje43FFwoK5txa4a65h1W1n9cQw8TN
0xc3 2MkkRNqwLkRipckDyyzPtaCxo8X36NTgvLR
0xc4 2NA62MxEdTcBhSBN51QjD4LEam2J34ufotY
0xc5 2NZRdM4XvAneaFcWA2q4XYTWNPXYyoYHGrF
0xc6 2NxmELAqCsy7T53eF4FPr2anA22ovTai1D3
0xc7 2PN6qKH8Vb9aKtUnL5fjAWi3weY4s9Z4F5C
0xc8 2PmSSJPRnJL3ChuvR764UzqKjH3KosKK2Yv
0xc9 2QAn3HVj51WW5XM4W8WPoUxbWuYakYiMGWC
0xca 2Qa7eGc2MigxxLnCb9vj7y5sJY3qhGCa6zR
0xcb 2QyTFFiKeRsRqADLgBM4STD96AZ6dz6q27W
0xcc 2RNnrEpcw93thyeUmCmPkwLQso4MaiYi6VF
0xcd 2Rn8TDvvDrEMao5crEBj5RTgfRZcXQmTiJb
0xce 2SBU4D3DWZQpTcWkwFc4PuaxT44sU6yyoT7
0xcf 2SaofC9WoGbHLRwu2H2PiPiEEga8QtEfcWP
0xd0 2Sz9GBFp5ymkDFP37JSj2sqW2K5PMaHXiny
0xd1 2TPUsAN7NgxD64pBCKs4MMxmowaeJGfxsZt
0xd2 2TnpU9UQfQ8fxtFKHMHPfr63ba5uF41y84W
0xd3 2UCA58ahx7K8qhgTNNhizLDKPCbABisTq7A
0xd4 2UbVg7h1EpVbiX7bTQ84JpLbAq6R8Q75nLd
0xd5 2UzqH6oJXXg4bLYjYRYPdJTrxTbg5BYT4xd
0xd6 2VQAt5ubpErXU9ysdSxiwnb8k66w1u5245n
0xd7 2VoWV51u6x2zLyR1iUP4GGiQXicBxbVcBSo
0xd8 2WCr648CPfDTDnr9oVoPakqgKM7SuH7bHDB
0xd9 2WcBh3EVgNPv6cHHtXDiuExx6ychqyLk3Ro
0xda 2X1XJ2Lny5aNyRiRyYe4Dj6Dtc7xneLnxnX
0xdb 2XQru1T6FnkqrF9a4a4PYDDVgEdDjQa2db6
0xdc 2XpCVzZPYVwJj4ai9bUirhLmTs8Ug6Biqn8
0xdd 2YDY6yfgqD7mbt1rEcu4BBU3FVdjcryEPuY
0xde 2Ycshxmz7vJEUhSzKeKPVfbK388zZX9EjP7
0xdf 2Z2DJwtHQdUhMWt8Qfjip9iapkeFWDDL1ua
0xe0 2ZRYuvzahLfAELKGVhA48dqrcP9WSxGypKz
0xe1 2ZptWv6sz3qd79kQaiaPT7y8Q1emPeFxnPS
0xe2 2aEE7uDBGm25yyBYfjzimc6QBeA2LNi4xT8
0xe3 2adZitKUZUCYrncgkmR466DfyGfHH4TuX2j
0xe4 2b2uKsRmrBP1jc3pqnqPQaLwkuAYDoiwdXD
0xe5 2bSEvrY58tZUcRUxvpFij4UDYXfoAVSFfAo
0xe6 2bqaXqeNRbjwVEv71qg43YbVLAB47EnuxFm
0xe7 2cEv8pkfiJvQN4MF6s6PN2im7ngK3sn9JUa
0xe8 2ceFjory126sEsnPBtWigWr2uRBZzdrrGnN
0xe9 2d3bLnyGHjHL7hDXGuw3zzyJh3gpwLdjgeZ
0xea 2dSvwn5ZaSTnzWefMwMPKV6aUgC5t7fCqCd
0xeb 2drGYmBrs9eFsL5oSxmidyDrGJhLpjG1pHq
0xec 2eFc9kJA9rpik9WwXzC3xTM83wCbmXB3Zao
0xed 2eewkjQTSa1Bcxx5d1cPGwUPqZhriAPaFvP
0xee 2f4HMiWkjHBeVnPDi32ibRbfdCD7evDQYqv
0xef 2fTcxhd41zN7NbpMo4T3uuiwQpiNbfoQhdo
0xf0 2frxZgjMJhYaFRFVt5sPEPrDCTDdYLAq87G
0xf1 2gGJAfqebQj38Egdy7HiYsyUz5itV6CFj6b
0xf2 2gfdmewwt7uW147n48i3sN6kmiE9Rj6mzYP
0xf3 2h4yNe4FAq5xssYv9A8PBrE2ZLjQNVVv4dB
0xf4 2hUJydAYTYGRkgz4EBYiWLMJLyEfK8Rdb31
0xf5 2hseacGqkFStdWRCKCy3ppUa8bjvFuWMFtT
0xf6 2iGzBbP92xdMWKrLQEPP9JbqvEFBCeaG9p2
0xf7 2igKnaVSKfopP9HUVFoiTnj7hrkS9JbwUcx
0xf8 2j5fPZbjcNzHFxicaHE3nGrPVVFh63anh7q
0xf9 2jUzzYi2u6Ak8n9kfJeP6kyfH7kx2hTXvgK
0xfa 2jtLbXpLBoMD1batkL4iRF6w4kGCyQLMba2
0xfb 2kHgCWvdUWXftR22qMV3jjECrNmTvC5pzrC
0xfc 2kh1oW2vmDi8mETAvNuP4DMUe1Girv1LG19
0xfd 2m6MQV9E3vtbe3tK1QKiNhUkRdmyocYZ2nq
0xfe 2mVh1UFXLe54WsKT6Rk3hBc2DGHEkJenPeS
0xff 2mu2cTMpdMFXPgkbBTAP1fjHztnVgxN7HX8
"""