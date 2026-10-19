---
title: lab-4-perform-website-footprinting
tags: [ceh, mindmaps, recon-and-information-gathering, type/lab, phase/recon]
---

# Lab 4: Perform Website Footprinting

## Task 1: Gather Information About a Target Website using Ping Command Line Utility

```
ping www.certifiedhacker.com
```

```
ping www.certifiedhacker.com -f -l 1500
```

\-f: specifies setting not fragmenting flag in packet

\-l: Specifies buffer size

```
ping www.certifiedhacker.com -i 3
```

\-i: sets the time to live value (MAX=255)

```
ping www.certifiedhacker.com -i 2 -n 1
```

\-n: specifies the number of echo requests  to be sent to the target

Use the ping command-line utility to test the reachability of the website www.eccouncil.org. Identify the maximum packet/frame size on this machine’s network.&#x20;

1472

## Task 2: Gather Information About a Target Website using Photon

```
python3 photon.py -h
```

```
python3 photon.py -u 
```

\-u: specifies the target website

```
python3 photon.py -u  -l 3 -t 200 --wayback
```

\-u: specifies the target website

\-l: specifies level to crawl (here 3)

\-t: specifies number of threads (here 200)

\--wayback: specifies using URLs from archive.org as seeds

Use Photon tool to crawl www.certifiedhacker.com website for internal, external and scripts URLs. What is the option that was used to specify the target website?&#x20;

\-u

Use Photon tool to crawl www.certifiedhacker.com website using URLs from archive.org. Enter the option that specifies using URLs from archive.org as seeds.&#x20;

\--wayback

## Task 3: Gather Information About a Target Website using Central Ops

Gather information about www.certifiedhacker.com website using Central Ops. Enter the IP address gathered under Address lookup section.&#x20;

162.241.216.11

## Task 4: Extract a Company's Data using Web Data Extractor

1. Web Data Extractor
2. Spiderfoot
3. ParseHub

In the Windows 11 machine, use Web Data Extractor web spidering tool to gather the target company‚Äôs data. Enter the target website that was used in this task to gather information.

## Task 5: Mirror a Target Website using HTTrack Web Site Copier

1. HTTrack Website Copier
2. Cyotek WebCopy

In the Windows 11 machine, use HTTrack Web Site Copier tool to mirror the entire website of the target organization ( Enter the newly created HTML file name, which allows you to view the webpage of the mirrored website on any browser.

index.html

## Task 6: Gather Information About a Target Website using GRecon

```
python3 grecon.py

certifiedhacker.com
```

Use GRecon¬†to search for available subdomains, sub-subdomains, login pages, directory listings, exposed documents, WordPress entries and pasting sites in target website. Enter the target that was used in this task to gather information.

certifiedhacker.com

## Task 7: Gather a Wordlist from the Target Website using CeWL

```
cewl -d 2 -m 5 www.certifiedhacker.com
```

\-d : represents the depth to spider the website

\-m : represents minimum word length

```
cewl -w wordlist.txt -d 2 -m 5 www.certifiedhacker.com
```

\-w : write the output to the file

Use CeWL ruby application to gather a wordlist from the target website ( Enter the command which allows you to gather a unique wordlist from the target website with a minimum word length of 6 and the depth of 3 to spider the target website.

cewl -d 3 -m 6 
