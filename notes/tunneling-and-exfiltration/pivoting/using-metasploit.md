---
title: using-metasploit
tags: [tunneling-and-exfiltration, pivoting, type/cheatsheet, phase/lateral-movement]
---

# Using Metasploit

  
Well, this is a post exploitation technique. Which means you should have the connection to the victim's system. Maybe a meterpreter shell.
   

## Commands

```
# Add a route
meterpreter> run autoroute -h

# Specify the subnet
meterpreter> run autoroute -s <IP address/cidr>

# Print the routes
route print
```

## Metasploit Autoroute Module

```
run post/multi/manage/autoroute
route print

# Scan open ports
use auxiliary/scanner/portscan/tcp
set RHOSTS 10.0.2.0/24
set PORTS 1-100
run
```

          (211).png" alt=""><figcaption><p>Pivoting Output</p></figcaption></figure>



***

## Reverse Relays - Metasploit

## REFERENCES

* 
* 

