---
title: api-hacking-basics
tags: [api-testing, api-hacking-basics, type/reference, phase/recon, phase/enumeration, platform/api]
---

# API Hacking Basics

## What is an API

### Definition:

* Application Programming Interface
* Sometimes apps need to communicate
* Can be on different levels - OS, Web...
* We will focus on web APIs

The importance of APIs in today's digital age

## Types of API

* Web APIs (e.g. REST, SOAP, GraphQL)
* Database APIs
* Operating System APIs
* Library & Framework APIs

## How APIs work

* Request & Response Model.
* HTTP Methods (GET, POST, PUT, DELETE).
* Status Codes.

## API components

* Endpoints
* Parameters
* Headers
* Payload/Body

## AUTHENTICATION & AUTHORIZATION

* API Keys.
* OAuth.
* JWT (JSON Web Tokens).
* Basic Authentication.

## Common use cases of APIs

* Integration between software applications.
* Mobile apps fetching data.
* Web apps interacting with backend servers.
* Third-party integrations.

## Benefits of using APIs

* Scalability.
* Modularity.
* Time-saving.
* Integration capabilities.

## Potential risks

* Brief introduction to why API security is crucial (this will set the stage for subsequent lessons in pentesting).

## API documentation & testing tools

* Imortance of clear API documentation.
* Introduction to tools like Postman & Swagger.

**Visit:** 

## OWASP API Top 10

TOP 10

## Practicals

### Communicating with APIs

Scanning with namp

```
nmap -sV 172.105.55.98
```

Fuzzing with ffuf

```
ffuf -w params.txt:PARAM -w values.txt:VAL -u  -mr "VAL" -c
```
