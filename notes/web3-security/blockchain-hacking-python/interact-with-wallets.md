---
title: interact-with-wallets
tags: [web3-security, blockchain-hacking-python, type/reference, phase/recon, platform/blockchain]
---

# Interact with Wallets

Pulling back balances and bytecode from wallets and contracts and understanding more about ERC Standards.

```python
from web3 import Web3

INFURA = ' KEY>'

# Connect to Blockchain

web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')


# Connect to contract

target_address = web3.to_checksum_address("0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97")

print(web3.from_wei(web3.eth.get_balance(target_address), 'ether'))

print(web3.eth.get_code(target_address))

```

## REFERENCES

* 
* 
