---
title: 1521-oracle-db-server
tags: [enumeration, protocols-and-ports, type/cheatsheet, phase/enumeration, platform/network]
---

# 1521 - Oracle DB Server

## Theory

The Oracle database server uses TCP port 1521, and the same concepts apply to it as Microsoft SQL Server when it comes to enumeration:

* Brute‐forcing credentials
* Identifying if the installed version is exploitable

***

## Practical

### Basic Nmap Scan

```
nmap ‐sV ‐O ‐sC ‐p 1521 [IP Address]
```

### Advanced Nmap Scan

```
nmap ‐sV ‐O ‐p 1521 ‐‐script=oracle* [IP Address]
```

### Brute Force

#### Hydra

```
hydra ‐s 1521 ‐L [users file] ‐P [passwords file] [IP]
```

***

## REFERENCES

* 
* 
