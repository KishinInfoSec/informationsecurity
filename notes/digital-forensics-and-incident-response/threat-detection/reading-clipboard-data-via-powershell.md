---
title: reading-clipboard-data-via-powershell
tags: [digital-forensics-and-incident-response, threat-detection, type/reference, phase/detection, platform/windows, platform/macos, platform/linux]
---

# Reading Clipboard Data via Powershell

## Clipboard Data

Adversaries may collect data stored in the clipboard from users copying information within or between applications.

For example, on Windows adversaries can access clipboard data by using `clip.exe` or `Get-Clipboard`.[\[1\]]( Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., Transmitted Data Manipulation).[\[4\]](

macOS and Linux also have commands, such as `pbpaste`, to grab clipboard contents.[\[5\]](

{% hint style="success" %}
ID: T1115Sub-techniques:  No sub-techniques

Tactic: Collection

Platforms: Linux, Windows, macOSVersion: 1.2

Created: 31 May 2017

Last Modified: 14 April 2023

## Commands

**Windows**

* `clip`
* `echo "New Clipboard Text" | clip`
* `Get-Clipboard`

**macOS**

* `pbpaste`

**Linux**

* `xclip -o`
* `echo "New Clipboard Text" | xclip`
* `xsel --clipboard --output`
* `echo "New Clipboard Text" | xsel --clipboard --input`

***

## REFERENCES

* 
