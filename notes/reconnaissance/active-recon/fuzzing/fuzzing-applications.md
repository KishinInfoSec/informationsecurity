---
title: fuzzing-applications
tags: [reconnaissance, active-recon, fuzzing, type/methodology, platform/linux, platform/web]
---

# Fuzzing Applications

## Introduction

Fuzz testing or fuzzing is a software testing technique, and it is a type of Security Testing. Fuzz Testing is a type of testing intended to discover coding errors and security loopholes in software, operating systems, or networks. This involves monitoring the target system by inputting invalid or random data called FUZZ to the system. where automated or semi-automated testing techniques are used.

    ../../      (231).png" alt=""><figcaption><p>Source: <a href="

## Fuzz Testing Steps

The steps for fuzzy testing include the basic testing steps-

* **Step 1)** Identify the target system
* **Step 2)** Identify inputs
* **Step 3)** Generate Fuzzed data
* **Step 4)** Execute the test using fuzzy data
* **Step 5)** Monitor system behavior
* **Step 6)** Log defects

## Existing Fuzzing Types

* Open Source
* Closed Source
* Network Protocol Fuzzing
* Parser Fuzzing
* Grammar-based Fuzzing
* Snapshot Fuzzing
* (Linux) Kernel Fuzzing
* Smart Contract Fuzzing

## Tools&#x20;

* AFL++
* Fuzzilli
* Jackalope
* Syzkaller
* Python3

## Writing a Fuzzer

* Sending random inputs to a target program.
* Creating a mutation engine.
* Monitor target state.
* Record crash and save interesting input cases.

## Code Coverage Fuzzing with AFL++

### Vim CVE-2019-20079&#x20;

Downloading the vulnerable version of Vim:

```
[+] Git clone VIM
cmd$ git clone  ; cd vim

[+] Compile and Make VIM with AFL++ 
cmd$ CC=afl-clang-fast CXX=afl-clang-fast++ ./configure --with-features=huge --enable-gui=none
cmd$ make -j4 ; cd src/

[+] Feed Corpus
cmd$ mkdir corpus ; mkdir output 
cmd$ echo "a*b\+\|[0-9]\|\d{1,9}" > corpus/1 ; echo "^\d{1,10}$" > corpus/2

[+] Fuzzing VIM
cmd$ afl-fuzz -m none -i corpus -o output ./vim -u NONE -X -Z -e -s -S @@ -c ':qa!'
```

The above options used -u NONE and -X is to speed up vim startup. Options -e -s are used to make vim silent and to avoid 'MORE' prompt which could block VIM, the option -Z disables the external commands which makes fuzzing safer. I've also created a small bash script which automates the above tasks for you \[vimfuzz.sh].\
\
While fuzzing, fuzz it on ram file system to avoid making too much I/O something like:  _sudo mount -t tmpfs -o size=6g tmpfs /home/afl-fuzz-user/afl-fuzz._ Aside you can use \[pack.sh] a script which contains some standard ubuntu packages so you dont get much dependence issues while compiling any target. Keep fuzzing :)

## Wfuzz

### Installation

```
pip3 install wfuzz
```

### Commands

```
wfuzz -w <wordlist.txt> 

[[Login]] bruteforce
wfuzz -z file,users.txt -d "username=FUZZ&password=FUZZ" 

[[Basic]] auth
wfuzz -z file,users.txt --basic FUZZ:FUZZ 
```

***

## REFERENCES

* 
* 
* 
* 
* 
* 
