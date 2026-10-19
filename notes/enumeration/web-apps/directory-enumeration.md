---
title: directory-enumeration
tags: [enumeration, web-apps, type/cheatsheet, phase/enumeration, platform/web]
---

# Directory Enumeration

## Introduction

Directory Enumeration is a technique to find or identifying and listing the files and directories. directories enumeration can get the information about hidden file structure or sub directories.

Directory Enumeration can be performed by using dirb, dirbuster, gobuster and dirsearch.

## Gobuster

```
gobuster dir -u  -x php -w /usr/share/wordlists/dirb/common.txt
```

## Dirb

```
dirb  /usr/share/wordlists/dirb/common.txt
```

## Wfuzz

```
wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc=404 
```

***

## REFERENCES

* 
* 
