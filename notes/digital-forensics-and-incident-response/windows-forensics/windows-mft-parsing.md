---
title: windows-mft-parsing
tags: [digital-forensics-and-incident-response, windows-forensics, type/tool, phase/forensics, platform/windows]
---

# Windows MFT Parsing

## Introduction

In computer forensics, the Master File Table (MFT) is a crucial component of the Windows operating system. It is a database that contains essential information about every file and directory on a computer's hard drive. The MFT keeps track of a file's location on the hard drive and manages other attributes. It contains metadata about each file, such as its name, size, creation date, and access permissions. They understand this data is critical for any computer forensics examination.

## Tools to Extract MFT

Jeff Bryner - MFT Grabber

NTFS Walk

Eric Zimmerman - MFTECmd

## MFTECmd

```
MFTECmd.exe -f "C:\Temp\SomeMFT" --csv "c:\temp\out" --csvf MyOutputFile.csv
MFTECmd.exe -f "C:\Temp\SomeMFT" --csv "c:\temp\out"
MFTECmd.exe -f "C:\Temp\SomeMFT" --json "c:\temp\jsonout"
MFTECmd.exe -f "C:\Temp\SomeMFT" --body "c:\temp\bout" --bdl c
MFTECmd.exe -f "C:\Temp\SomeMFT" --de 5-5
```

***

## REFERENCES

* 
* 
* 
* 
