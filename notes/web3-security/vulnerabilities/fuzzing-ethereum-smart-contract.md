---
title: fuzzing-ethereum-smart-contract
tags: [web3-security, vulnerabilities, type/tool, platform/blockchain]
---

# Fuzzing Ethereum Smart Contract

## Introduction

Fuzzing is known as one of the most efficient techniques to find bugs in software. Sadly, when dealing with Ethereum smart contracts, the number of fuzzers and documentation available is really limited.

## Echidna

Echidna is a weird creature that eats bugs and is highly electrosensitive (with apologies to Jacob Stanley)

More seriously, Echidna is a Haskell program designed for fuzzing/property-based testing of Ethereum smart contracts. It uses sophisticated grammar-based fuzzing campaigns based on a contract ABI to falsify user-defined predicates or Solidity assertions. It is  designed with modularity in mind, so it can be easily extended to include new mutations or test specific contracts in specific cases.

### Installation

```
wget 

tar -xf echidna-2.2.5-x86_64-linux.tar.gz

./echidna
```

### Usage

#### Example Solidity File

flags.sol

```solidity
contract Test {
  event Flag(bool);

  bool private flag0 = true;
  bool private flag1 = true;

  function set0(int val) public returns (bool){
    if (val % 100 == 0) 
      flag0 = false;
  }

  function set1(int val) public returns (bool){
    if (val % 10 == 0 && !flag0) 
      flag1 = false;
  }

  function echidna_alwaystrue() public returns (bool){
    return(true);
  }

  function echidna_revert_always() public returns (bool){
    revert();
  }

  function echidna_sometimesfalse() public returns (bool){
    emit Flag(flag0);
    emit Flag(flag1);
    return(flag1);
  }

}
```

#### Running Echidna

```
./echidna ~/Desktop/solidity/flags.sol
```

***

## REFERENCES

* 
* 
* 
* 
* 
* 
* 
