---
title: gmail-address
tags: [reconnaissance, doxing, type/tool, phase/recon]
---

# Gmail Address

## Introduction

Doxing is essentially gathering sensitive information about a target that they generally wouldn't want or expect disclosed. These details include everything from their name, email address, ZIP code, and even home and work addresses.

## GHunt

GHunt (v2) is an offensive Google framework, designed to evolve efficiently. It's currently focused on OSINT, but any use related with Google is possible

### Features

* CLI usage and modules
* Python library usage
* Fully async
* JSON export
* Browser extension to ease login

### Installation

```
$ pip3 install pipx
$ pipx ensurepath
$ pipx install ghunt
```

### Usage

First, launch the listener by doing `ghunt login` and choose between 1 of the 2 first methods:&#x20;

```
$ ghunt login

[1] (Companion) Put GHunt on listening mode (currently not compatible with docker)
[2] (Companion) Paste base64-encoded cookies
[3] Enter manually all cookies

Choice =>
```

Then, use GHunt Companion to complete the login.

The extension is available on the following stores :\
\
![Firefox](   ![Chrome](

Copy the base64-encoded cookies and paste it in the ghunt terminal after choosing the option 2.

#### Getting Information of an Email

```
$ ghunt email <email_address>
```

***

## REFERENCES

* 
* 
* 
* 
