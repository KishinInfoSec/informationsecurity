---
title: scheduled-tasks
tags: [windows-security, persistence-post, type/reference, phase/persistence, platform/windows]
---

# Scheduled Tasks

### Theory

This mechanism is scheduled tasks and is documented as T1053.005 in the MITRE ATT\&CK knowledge base. Scheduled tasks enable users and/or administrators to persistently execute applications on Windows systems. Scheduled tasks can be created using the Task Scheduler, programmatically or using the native Windows utility schtasks.exe from the command prompt.

### Practical

#### Schedule Tasks: Schtasks

Windows native tool for managing scheduled tasks

```
[[Help]] menu
schtasks /?

[[List]] scheduled tasks
schtasks /query

[[Create]] a new task
schtasks /CREATE /SC DAILY /TN "Persistent Notepad" /TR "C:\Windows\System32\notepad.exe" /RU SYSTEM

```

***

## References

* 
* 
* 
