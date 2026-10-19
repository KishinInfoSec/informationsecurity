---
title: investigating-favicon-hashes
tags: [digital-forensics-and-incident-response, web-investigations, type/tool, phase/recon, platform/web]
---

# Investigating Favicon Hashes

## Introduction

Favicons are small icons in modern web applications that could be very useful for us in our day-to-day hunting activities, especially when we combine these icons with modern search engines to find assets on the internet.

## FaviHunter

This project aims to help a security professional find assets on the internet using favicon hashes on search engines such as FOFA, Shodan, Censys, Zoomeye, Criminal IP, and ODIN. The program returns a table with the custom queries of each search engine and their shortened URL with the query applied.

### Installation

```
git clone 

pip3 install -r requirements.txt
```

### Commands

```
# Help Menu
python3 favihunter.py --help

# Analyze a specific URL
python3 favihunter.py --url <url address>

# Analyze a file with URLs
python3 favihunter.py --urls-file <file path>

# Analyze a local favicon image
python3 favihunter.py --favicon <file path>

# Clean the local favicon directory
python3 favihunter.py --remove-favicons
```

    ../      (2) (1) (1) (1) (1).png" alt=""><figcaption><p>Output</p></figcaption></figure>

***

## REFERENCES

* 
