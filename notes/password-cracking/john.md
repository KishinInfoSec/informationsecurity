---
title: john
tags: [password-cracking, type/tool, phase/credential-access, platform/linux]
---

# John

## Commands

### Formats

```
john --list=formats
```

### Crack SHA1

```
john  --format=raw-sha1 hash.txt
```

### Crack MD5

```
john --format=raw-md5 hash.txt
```

### Cracking Shadow Files

<pre><code># Unshadow
unshadow passwd.txt shadow.txt > unshadowed.txt

# John
john /etc/shadow

<strong># Wordlist
</strong>john --wordlist=&#x3C;password.txt> /etc/shadow
</code></pre>

### Cracking Zip Files

```
# Zip to John
zip2john file.zip > ziphash.txt

# John
john --format=zip ziphash.txt
```

### Crack .pfx File

```
pfx2john <pfx file> > hash.txt

john hash.txt --wordlist=<wordlist location>
```

### Crack GPG Passphrase

**Read More** Here

```
gpg2john priv.key > hash 

john hash --wordlist=/usr/share/wordlists/rockyou.txt 
```

### Crack SSH Passphrase

```
ssh2john /home/chinju/.ssh/id_rsa > ssh_hash.txt

john ssh_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

***

## Hashing

### Identifying Hashes

#### Hash Identifier

```
hash-identifier

<paste the hash>
```

#### Hash ID

```
hashid <hash value>
```

### Cracking Hashes

#### Crack Station

*    &#x20;

#### Decode FR

* 

## REFERENCES

* 
* 
* 
* 
