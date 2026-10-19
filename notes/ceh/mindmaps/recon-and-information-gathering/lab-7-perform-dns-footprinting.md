---
title: lab-7-perform-dns-footprinting
tags: [ceh, mindmaps, recon-and-information-gathering, type/lab, phase/recon]
---

# Lab 7: Perform Dns Footprinting

## Task 1: Gather DNS Information using nslookup Command Line Utility and Online

```
nslookup

set type=a

www.certifiedhacker.com
```

### Get Authoratative Name Server

```
nslookup

set type=cname

certifiedhacker.com
```

1. DNSdumpster
2. DNS Records

Use the nslookup command-line utility to find the primary server of the website www.certifiedhacker.com 

ns1.bluehost.com

## Task 2: Perform Reverse DNS Lookup using Reverse IP Domain Check and DNSRecon

### DNSRecon

```
./dnsrecon.py -r 162.241.216.0-162.241.216.255
```

Perform a reverse DNS lookup using DNSRecon on IP range (162.241.216.0-162.241.216.255) to locate a DNS PTR record. Enter the DNS PTR record for IP address 162.241.216.11.

box.5331.bluehost.com

## Task 3: Gather Information of Subdomain and DNS Records using SecurityTrails

1. DNSChecker
2. DNSdumpster

Use SecurityTrails to gather information regarding the subdomains and DNS records of the certifiedhacker.com website. Enter YES if you find any NS records; else, enter NO.&#x20;

YES

Use SecurityTrails to gather information regarding the subdomains and DNS records of the certifiedhacker.com website. Enter YES if you find any AAAA records; else, enter NO.&#x20;

NO
