from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
        noblecoin=math.Object(
        PARENT=networks.nets['noblecoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='e021a7b8c322482a'.decode('hex'),
        PREFIX='e280193ae6a4927a'.decode('hex'),
        P2P_PORT=9184,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9188,
        BOOTSTRAP_ADDRS='p2pool-us.coin-project.org p2pool-eu.coin-project.org p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org taken.pl polishcoin.info pcc.paybtc.pl us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
