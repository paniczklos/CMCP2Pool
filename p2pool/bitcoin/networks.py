import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack
from operator import *

def get_subsidy(nCap, nMaxSubsidy, bnTarget):		
	#nSubsidy=3.5#add by ComosCoin-DEV	
    return int(3.5 * 1000000)
	
	

nets = dict(
    noblecoin=math.Object(
        P2P_PREFIX='c0dbf1fd'.decode('hex'),
        P2P_PORT=55884,
        ADDRESS_VERSION=21,
        RPC_PORT=55883,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'noblecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
	#SUBSIDY_FUNC=lambda target: get_subsidy(6, 100, target),
        SUBSIDY_FUNC=lambda height: 5000*100000000,
	BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s targetspacing
        SYMBOL='NOBLE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'noblecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/zeitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.zeitcoin'), 'zeitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://cryptexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://cryptexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://cryptexplorer.com/transaction/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
