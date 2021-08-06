from constant import *
import subprocess
import os
import json
import bit 
from bit.network import NetworkAPI
from bit import PrivateKeyTestnet
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from dotenv import load_dotenv

load_dotenv("C:\\Users\\thebe\\Fintech\\work_here\\mnemonic.env")
mnemonic = os.getenv('mnemonic')

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={depth} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return json.loads(output)

coins = {
    ETH: derive_wallets(coin=ETH),  
    BTCTEST: derive_wallets(coin=BTCTEST)
}
    
def priv_key_to_account(coin, priv_key):
    print(coin)
    print(priv_key)
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return bit.PrivateKeyTestnet(priv_key)
    
    
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        value = w3.toWei(amount, 'ether')
        return {
            "chainId": 123, # Eth.chain_id
            "value": value, 
            "from": account.address,
            "to": to, 
            "gasPrice": w3.eth.gasPrice, 
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address,[(to, amount, BTC)])
 
    
def send_tx(coin, account, to, amount): 
    raw_tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(raw_tx)
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex() 
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)