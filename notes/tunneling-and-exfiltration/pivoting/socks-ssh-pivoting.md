---
title: socks-ssh-pivoting
tags: [tunneling-and-exfiltration, pivoting, type/cheatsheet, phase/lateral-movement, platform/linux, platform/network]
---

# SOCKS, SSH - Pivoting

## Edit proxychains4.conf

```
sudo nano /etc/proxychains4.conf

# Uncomment or add "socks4 127.0.0.1 9050"
```

## SSH Tunneling

```
ssh -d 9050 <username>@<ip address machine within network>
```

## Change Proxy Settings in Browser

* Add a proxy as: manual
* Add SOCKS Host as 127.0.0.1
* Add Port as 9050
* Select SOCKSv4

## Proxychains

```
proxychains nmap -p21 <outside machines ip address>

proxychains firefox <outside machines ip address>

proxy
```

## Remote Port Forwarding

```
ssh -R <Windows 11 IP Addr>127.0.0.1:1234
ssh -R <IP address><attacker ip>:1234 <username>@<ip address>
```

## REFERENCES

