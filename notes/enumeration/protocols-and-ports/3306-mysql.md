---
title: 3306-mysql
tags: [enumeration, protocols-and-ports, type/cheatsheet, phase/enumeration, platform/network]
---

# 3306 - Mysql

## Theory

The MySQL database server uses TCP port 3306

* Brute‐forcing credentials&#x20;
* Identifying if the installed version is exploitable

***

## Practical

### Basic Nmap Scan

```
nmap ‐sV ‐O ‐sC ‐p 3306 [IP Address]
```

### Advanced Nmap Scan

```
nmap ‐sV ‐O ‐p 3306 ‐‐script=mysql* [IP Address]
```

### Brute Force

```
hydra ‐L [users file] ‐P [passwords file] MySQL://[IP]
```

***

## REFERENCES

* 
* 
