---
title: linux-kernel-fuzzing
tags: [reconnaissance, active-recon, fuzzing, type/tool, platform/linux]
---

# Linux Kernel Fuzzing

## Introduction

syzkaller is an unsupervised coverage-guided kernel fuzzer

## Setup: Ubuntu host, QEMU vm, x86-64 kernel

These are the instructions on how to fuzz the x86-64 kernel in a QEMU with Ubuntu on the host machine and Debian Bullseye in the QEMU instances.

In the instructions below, the `$VAR` notation (e.g. `$GCC`, `$KERNEL`, etc.) is used to denote paths to directories that are either created when executing the instructions (e.g. when unpacking GCC archive, a directory will be created), or that you have to create yourself before running the instructions. Substitute the values for those variables manually.

```
sudo apt update
sudo apt install make gcc flex bison libncurses-dev libelf-dev libssl-dev
```

If your distro's GCC is older, it's preferable to get the latest GCC from this list. Download and unpack into `$GCC`, and you should have GCC binaries in `$GCC/bin/`

> **Ubuntu 20.04 LTS**: You can ignore this section. GCC is up-to-date.

```
ls $GCC/bin/
# Sample output:
# cpp     gcc-ranlib  x86_64-pc-linux-gnu-gcc        x86_64-pc-linux-gnu-gcc-ranlib
# gcc     gcov        x86_64-pc-linux-gnu-gcc-9.0.0
# gcc-ar  gcov-dump   x86_64-pc-linux-gnu-gcc-ar
# gcc-nm  gcov-tool   x86_64-pc-linux-gnu-gcc-nm
```

### See This Guide

***

## REFERENCES

* 
* 
* 
* 
* 
* 
