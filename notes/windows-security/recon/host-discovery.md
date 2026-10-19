---
title: host-discovery
tags: [windows-security, recon, type/cheatsheet, phase/recon, platform/windows, platform/network]
---

# Host Discovery

## Powershell Network  Scanner

```
PS> .\IPv4NetworkScan.ps1 -IPv4Address 192.168.178.0 -Mask 255.255.255.0 -DisableDNSResolving
```

```
PS> .\IPv4NetworkScan.ps1 -IPv4Address 192.168.178.0 -CIDR 20
```

***

## Zenmap

***

## Nmap

```
nmap -Pn <IP address>
```

```
nmap -Pn -p 80 <IP address>
```

```
nmap -Pn -p 80 -sV <IP address>
```

