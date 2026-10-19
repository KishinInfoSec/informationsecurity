---
title: smart-contract-template
tags: [web3-security, blockchain-hacking-python, type/reference, platform/blockchain]
---

# Smart Contract Template

I have created this simple template to connect with the blockchain and repeatedly use it with other smart contract codes.

```python
from web3 import Web3

INFURA = ' KEY>'

# Connect to Blockchain

web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')


# Connect to contract

target_address = web3.to_checksum_address("")
target_ABI = ''

target = web.eth.contract(address=target_address, abi=target_ABI)

```

## REFERENCES

* 
* 
* 
* 
