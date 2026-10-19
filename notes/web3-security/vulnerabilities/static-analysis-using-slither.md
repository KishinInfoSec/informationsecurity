---
title: static-analysis-using-slither
tags: [web3-security, vulnerabilities, type/tool, phase/detection, platform/blockchain]
---

# Static Analysis using Slither

          (1) (1) (1) (1).png" alt="" width="375"><figcaption><p>Slither</p></figcaption></figure>

## Introduction

Smart contract development is one of the integral highlights of the blockchain and web3 ecosystem. The arrival of new tools, such as static analyzers, has been one of the prominent highlights of progress in blockchain. One of the most popular frameworks for static analysis of smart contracts emerged in 2018. Trail by Bits introduced Slither as a static analysis framework for Solidity, and the Slither Solidity interplay gained formidable traction.

Slither has the capability to run a collection of vulnerability detectors and print visual information regarding contract details. Furthermore, you could also notice that Slither offers an API for easier scripting of custom analysis tasks. It is a powerful tool for helping developers identify vulnerabilities and improve their understanding of code. The following post offers you an introduction to Slither and its capabilities, along with a description of its working.&#x20;

## Installation

```
pipx install slither-analyzer

pipx install solc-select

solc-select install 0.4.25

solc-select use 0.4.25
```

## Running Slither

**Vulnerable Code:** **

```
slither reentrancy.sol
```

### Output

```solidity
'solc --version' running
'solc reentrancy.sol --combined-json abi,ast,bin,bin-runtime,srcmap,srcmap-runtime,userdoc,devdoc,hashes,compact-format --allow-paths .,/home/kali/Desktop/solidity' running
Compilation warnings/errors on reentrancy.sol:
reentrancy.sol13: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
            throw;
            ^---^
reentrancy.sol13: Warning: "throw" is deprecated in favour of "revert()", "require()" and "assert()".
            throw;
            ^---^
reentrancy.sol5: Warning: No visibility specified. Defaulting to "public". 
    function getBalance(address u) constant returns(uint){
    ^ (Relevant source part starts here and spans across multiple lines).
reentrancy.sol5: Warning: No visibility specified. Defaulting to "public". 
    function addToBalance() payable{
    ^ (Relevant source part starts here and spans across multiple lines).
reentrancy.sol5: Warning: No visibility specified. Defaulting to "public". 
    function withdrawBalance(){
    ^ (Relevant source part starts here and spans across multiple lines).
reentrancy.sol5: Warning: No visibility specified. Defaulting to "public". 
    function withdrawBalance_fixed(){
    ^ (Relevant source part starts here and spans across multiple lines).
reentrancy.sol5: Warning: No visibility specified. Defaulting to "public". 
    function withdrawBalance_fixed_2(){
    ^ (Relevant source part starts here and spans across multiple lines).

INFO:Detectors:
Reentrancy in Reentrance.withdrawBalance() (reentrancy.sol#14-21):                                                  
        External calls:                                                                                             
        - ! (msg.sender.call.value(userBalance[msg.sender])()) (reentrancy.sol#17)                                  
        State variables written after the call(s):                                                                  
        - userBalance[msg.sender] = 0 (reentrancy.sol#20)                                                           
        Reentrance.userBalance (reentrancy.sol#4) can be used in cross function reentrancies:                       
        - Reentrance.addToBalance() (reentrancy.sol#10-12)                                                          
        - Reentrance.getBalance(address) (reentrancy.sol#6-8)                                                       
        - Reentrance.withdrawBalance() (reentrancy.sol#14-21)                                                       
        - Reentrance.withdrawBalance_fixed() (reentrancy.sol#23-31)                                                 
        - Reentrance.withdrawBalance_fixed_2() (reentrancy.sol#33-40)                                               
Reference:                  
INFO:Detectors:
Deprecated standard detected THROW (reentrancy.sol#18):                                                             
        - Usage of "throw" should be replaced with "revert()"                                                       
Deprecated standard detected THROW (reentrancy.sol#29):                                                             
        - Usage of "throw" should be replaced with "revert()"                                                       
Reference:                        
INFO:Detectors:
Version constraint ^0.4.15 contains known severe issues (       
        - DirtyBytesArrayToStorage                                                                                  
        - KeccakCaching                                                                                             
        - EmptyByteArrayCopy                                                                                        
        - DynamicArrayCleanup                                                                                       
        - ImplicitConstructorCallvalueCheck                                                                         
        - TupleAssignmentMultiStackSlotComponents                                                                   
        - MemoryArrayCreationOverflow                                                                               
        - privateCanBeOverridden                                                                                    
        - SignedArrayStorageCopy                                                                                    
        - UninitializedFunctionPointerInConstructor_0.4.x                                                           
        - IncorrectEventSignatureInLibraries_0.4.x                                                                  
        - ExpExponentCleanup                                                                                        
        - NestedArrayFunctionCallDecoder                                                                            
        - ZeroFunctionSelector.                                                                                     
It is used by:                                                                                                      
        - ^0.4.15 (reentrancy.sol#1)                                                                                
solc-0.4.25 is an outdated solc version. Use a more recent version (at least 0.8.0), if possible.                   
Reference:              
INFO:Detectors:
Low level call in Reentrance.withdrawBalance() (reentrancy.sol#14-21):                                              
        - ! (msg.sender.call.value(userBalance[msg.sender])()) (reentrancy.sol#17)                                  
Low level call in Reentrance.withdrawBalance_fixed() (reentrancy.sol#23-31):                                        
        - ! (msg.sender.call.value(amount)()) (reentrancy.sol#28)                                                   
Reference:                             
INFO:Detectors:
Function Reentrance.withdrawBalance_fixed() (reentrancy.sol#23-31) is not in mixedCase                              
Function Reentrance.withdrawBalance_fixed_2() (reentrancy.sol#33-40) is not in mixedCase                            
Reference:  
INFO:Detectors:
Reentrancy in Reentrance.withdrawBalance_fixed_2() (reentrancy.sol#33-40):                                          
        External calls:                                                                                             
        - msg.sender.transfer(userBalance[msg.sender]) (reentrancy.sol#38)                                          
        State variables written after the call(s):                                                                  
        - userBalance[msg.sender] = 0 (reentrancy.sol#39)                                                           
Reference:                
INFO:Slither:reentrancy.sol analyzed (1 contracts with 93 detectors), 10 result(s) found

```

***

* 
* 
* 
* 
* 
* 
