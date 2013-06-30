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
    CosmosCoin=math.Object(
        P2P_PREFIX='e4e8e9e5'.decode('hex'),
        P2P_PORT=19990,//add by ComosCoin-DEV
        ADDRESS_VERSION=27,//add by ComosCoin-DEV
        RPC_PORT=19991,//add by ComosCoin-DEV
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'CosmosCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda target: get_subsidy(6, 100, target),
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=60, # s 1 minute
        SYMBOL='CMC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CosmosCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CosmosCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CosmosCoin'), 'CosmosCoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://cosmoscoin.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://cosmoscoin.com/address/',
        SANE_TARGET_RANGE=(2**256//2**20//1000 - 1, 2**256//2**20 - 1),
    ),
    
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
