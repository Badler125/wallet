# Multi-Blockchain Wallet in Python

## Background and Wallet description
Say your new startup is focusing on building a portfolio management system that supports crypto, the problem is, there are so many coins out there! Thankfully you can use `hd-wallet-derive`, a command line tool that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today. 

Once you've intgrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving you a serious esge against the competition.

For this demonstration we will just get 2 coins working: Ethereum and Bitcoin Testnet. Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.

## Dependencies
The following dependencies are required for this assignement

Important: If you have not already installed the dependencies listed below, you may do so by following the instructions found in the following guides:

* https://columbia.bootcampcontent.com/columbia-bootcamp/cu-nyc-virt-fin-pt-03-2021-u-c/-/blob/master/02-Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md

* https://columbia.bootcampcontent.com/columbia-bootcamp/cu-nyc-virt-fin-pt-03-2021-u-c/-/blob/master/02-Homework/19-Blockchain-Python/Instructions/Resources/Blockchain_TX_Install_Guide.md

### Dependencies List:
* PHP must be installed on your operating system.
* you will need to clone the `hd-wallet-derive` tool.
* `bit` Python Bitcoin library.
* `web3.py` Python Ethereum library.


