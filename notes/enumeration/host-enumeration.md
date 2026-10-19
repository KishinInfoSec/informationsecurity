---
title: host-enumeration
tags: [enumeration, type/cheatsheet, phase/enumeration, phase/privesc, platform/windows, platform/linux]
---

# Host Enumeration

## Windows

### Searching Commands

#### dir

```
# help
dir /?

# search for all .txt files
dir *.txt /s

# pause when the screen is full
dir *.txt /s /b

# list directories only
dir /a:d

# list contents except directories
dir /a:-d

# display hidden directories
dir /a:h
```

#### find

```
# help 
find /?

# Search for words in a file
find "hello" story.txt

# Ignore the character case
find /i "Hello" story.txt

# Count number of empty strings
type story.txt | find " " /v /c
```

### WinPEAS

## Linux

### LinPEAS

```
curl -L  | sh
```
