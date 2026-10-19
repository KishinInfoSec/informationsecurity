---
title: ceh-engage-part-1
tags: [ceh, engage, type/walkthrough, phase/recon, phase/enumeration, platform/network]
---

# CEH Engage Part 1

Perform vulnerability scanning for the webserver hosting movies.cehorg.com using OpenVAS and identify the severity level of RPC vulnerability.

```
nmap -sn moves.cehorg.com
```

          (178) 

          (183) 

          (164) 

Perform vulnerability scanning for the Linux host in the 172.16.0.0/24 network using OpenVAS and find the number of vulnerabilities with severity level as medium.

          (179) 

          (165) 

You are performing reconnaissance for CEHORG and has been assigned a task to find out the physical location of one of their webservers hosting www.certifiedhacker.com. What are the GEO Coordinates of the webserver? Note: Provide answer as Latitude, Longitude.

#### BillCipher

          (199) 

          (180) 

Identify if the website www.certifiedhacker.com allows DNS zone transfer. (Yes/No)

```
dig www.certifiedhacker.com -axfr
```

          (181) 

Identify the number of live machines in 172.16.0.0/24 subnet.

```
nmap -sn -PE 172.16.0.0/24
```

          (182) 

While performing a security assessment against the CEHORG network, you came to know that one machine in the network is running OpenSSH and is vulnerable. Identify the version of the OpenSSH running on the machine. Note: Target network 192.168.0.0/24.

```
sudo nmap -sV -p 22 192.168.0.0/24
```

          (155) 

          (184) 

During a security assessment, it was found that a server was hosting a website that was susceptible to blind SQL injection attacks. Further investigation revealed that the underlying database management system of the site was MySQL. Determine the machine OS that hosted the database.

```
 sudo nmap -sV -O -A -p 3306 192.168.55
```

          (156) 

          (185) 

Find the IP address of the Domain Controller machine in 10.10.10.0/24.

```
nmap -sV -A -T4 10.10.10.0/24
```

          (200) 

          (192) 

Perform a host discovery scanning and identify the NetBIOS name of the host at 10.10.10.25.

```
nmap -sV -A -T4 10.10.10.25
```

          (193) 

          (152) 

Find the IP address of the machine which has port 21 open. Note: Target network 172.16.0.0/24

```
nmap -p 21 172.16.0.0/24
```

          (186) 

          (130) 

Perform an intense scan on 10.10.10.25 and find out the FQDN of the machine in the network.

```
nmap -sV -A -T4 10.10.10.25
```

          (153) 

          (194) 

What is the DNS Computer Name of the Domain Controller?

```
nmap -sV -A -T4 10.10.10.25
```

          (154) 

          (195) 

Perform LDAP enumeration on the target network and find out how many user accounts are associated with the domain.

```
ldapsearch -x -h 10.10.10.25 -b "DC=CEHORG,DC=com" "objectclass=user" cn
```

          (157) 

          (31) 

Perform an LDAP Search on the Domain Controller machine and find out the version of the LDAP protocol.

```
ldapsearch -h 10.10.10.25 -x -s base namingcontexts
```

          (196) 

What is the IP address of the machine that has NFS service enabled? Note: Target network 192.168.0.0/24.

```
sudo nmap -sV -p 2049 192.168.0.0/24
```

          (158) 

          (191) 

Perform a DNS enumeration on www.certifiedhacker.com and find out the name servers used by the domain.

```
dnsenum www.certifiedhacker.com
```

          (159) 

          (190) 

Find the IP address of the machine running SMTP service on the 192.168.0.0/24 network.

```
nmap -sV -T4 -p 25 192.168.0.0/25
```

          (160) 

          (189) 

![](

Perform an SMB Enumeration on 192.168.0.51 and check whether the Message signing feature is enabled or disabled. Give your response as Yes/No.

```
nmap -A -T4 192.168.0.51
```

          (162) 

          (188) 

Perform vulnerability scanning for the domain controller using OpenVAS and identify the number of vulnerabilities with severity level as "medium".

          (163) 

          (32) 

Perform a vulnerability research on CVE-2022-30171 and find out the base score and impact of the vulnerability.

          (187) 
