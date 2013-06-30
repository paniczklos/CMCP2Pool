screen -d -m -S CMCP2Pool python /root/cosmoscoin/CMCP2Pool/run_p2pool.py --net CosmosCoin -f 0.5 --give-author 0

screen -x CMCP2Pool
Ctrl+A Ctrl+D

python run_p2pool.py --net CosmosCoin -f 0.5 --give-author 0