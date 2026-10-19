---
title: r-code-execution
tags: [ctfs, real-world, type/reference, phase/exploitation]
---

# R: Code Execution

## Theory

R is a language and environment for statistical computing and graphics. It is a GNU project which is similar to the S language and environment which was developed at Bell Laboratories (formerly AT\&T, now Lucent Technologies) by John Chambers and colleagues.

***

## Practical

### System Commands

```
# System()
system("ls -l") # Executes the ls -l command in Unix-like systems

# System2()
output <- system2("ls", args = "-l", stdout = TRUE)
output

# Shell()
shell("ls -l")
```

### File Reading

```
# read.csv()
data <- read.csv("file.csv")

# read.table()
data <- read.table("file.txt", sep = "\t", header = TRUE)

# readLines()
lines <- readLines("/etc/passwd")

# scan()
data <- scan("file.txt", what = "character", sep = ",")

# file()
con <- file("file.txt", "r")
```

### List Directory Contents

```
# dir()
files <- dir()
print(files)

# file.access()
file.access(dir("/etc/"))
```

* 0: No access permissions.
* 1: Execute access.
* 2: Write access.
* 4: Read access.
* 6: Read and write access.
* 7: Read, write, and execute access.

***

## REFERENCES

* 
* 
* 
* 
