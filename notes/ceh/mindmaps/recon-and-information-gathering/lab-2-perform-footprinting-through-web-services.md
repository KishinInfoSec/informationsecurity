---
title: lab-2-perform-footprinting-through-web-services
tags: [ceh, mindmaps, recon-and-information-gathering, type/lab, phase/recon]
---

# Lab 2: Perform Footprinting Through Web Services

## Task 1: Find the Company's Domains and Sub-domains using Netcraft

Search for www.eccouncil.org on Netcraft ( and identify the operating system of the web server hosting the website www.eccouncil.org.&#x20;

## Task 2: Gather Personal Information using PeekYou Online People Search Service

Gather personal information about Satya Nadella (CEO of Microsoft) using PeekYou ( an online people search service. Enter the name of the university where Satya Nadella studied MBA.&#x20;

University of Chicago

## Task 3: Gather an Email List using theHarvester

Use theHarvester tool to gather the list of email IDs related to Microsoft (www.microsoft.com) organization from the Baidu search engine. Enter the option that specifies the domain or company name to search.&#x20;

```
theHarvester -d microsoft.com -l 200 -b baidu
```

\-d: specifies the domain or company name

\-l: specifies the number of results to be retrieved

\-b: specifies the data source

## Task 4: Gather Information using Deep and Dark Web Searching

Use Tor Browser to perform searches on the deep and dark web. Identify the search engine Tor Browser uses to perform a dark web search.

DuckDuckGo

## Task 5: Determine Target OS Through Passive Footprinting

Use Censys ( to perform the passive footprinting of www.eccouncil.org. Flag submission is not required for this task, enter "No flag" as the answer.
