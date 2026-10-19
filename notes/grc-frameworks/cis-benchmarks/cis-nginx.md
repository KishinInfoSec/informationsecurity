---
title: cis-nginx
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/web, source/cis]
description: "CIS NGINX Benchmark v3.0.0 checklist: modules, accounts, TLS, request limits, headers, with levels."
source_pdf: CIS_NGINX_Benchmark_v3.0.0.pdf
---

# CIS NGINX Benchmark v3.0.0 (12-24-2025)

## Overview

- **Product:** NGINX 1.28.x on systemd-based Linux
- **Benchmark version:** v3.0.0 (2025-12-24)
- **Profiles:** Level 1 and Level 2, each for the Webserver (Web), Proxy and Loadbalancer (LB) roles. All items are manual assessments in this version.
- **Recommendations:** 44 total (0 Automated, 44 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Initial Setup | 3 |
| 2 Basic Configuration | 15 |
| 3 Logging | 4 |
| 4 Encryption | 12 |
| 5 Request Filtering and Restrictions | 10 |
| 6 Mandatory Access Control | 0 |

## Lab relevance

- **Caddy is the actual front end, NGINX is not installed:** use this benchmark as a requirements list and translate each item to Caddy (automatic TLS, `header`, `request_body max_size`, `servers { timeouts }` and so on).
- **Information disclosure (2.5.1-2.5.4):** hide version tokens and server banners, remove default pages, block hidden files, strip upstream headers; Caddy's `-Server` header directive covers the first.
- **TLS (4.1.1-4.1.8):** HTTP to HTTPS redirect, trusted chain, restricted key permissions, modern protocols and ciphers, OCSP stapling and HSTS; Caddy defaults to TLS 1.2+/1.3 and enables OCSP stapling, so add HSTS explicitly.
- **Request limits (5.2.x, L2 for rate limiting):** header/body timeouts, max body size (Gitea uploads need a higher but bounded limit), per-IP connections and rate limits.
- **Reverse-proxy behaviour (3.4, 2.5.4, 4.1.9):** pass the real client IP to Gitea/upstreams, avoid leaking upstream information, authenticate upstream traffic with client certificates if you proxy to remote nodes.
- **Unknown hosts (2.4.2):** reject requests for unknown host names so direct-IP scans and host-header tricks do not reach Gitea.
- **Browser headers (5.3.1-5.3.3):** X-Content-Type-Options, CSP and Referrer-Policy on pages Caddy serves.

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Initial Setup

#### 1.1 Installation

- [ ] 1.1.1 Ensure NGINX is installed — L1 · Manual

#### 1.2 Configure Software Updates

- [ ] 1.2.1 Ensure package manager repositories are properly configured — L1 · Manual
- [ ] 1.2.2 Ensure the latest software package is installed — L1 · Manual

### 2 Basic Configuration

#### 2.1 Minimize NGINX Modules

- [ ] 2.1.1 Ensure only required dynamic modules are loaded — L1 · Manual

#### 2.2 Account Security

- [ ] 2.2.1 Ensure that NGINX is run using a non-privileged, dedicated service account — L1 · Manual
- [ ] 2.2.2 Ensure the NGINX service account is locked — L1 · Manual
- [ ] 2.2.3 Ensure the NGINX service account has an invalid shell — L1 · Manual

#### 2.3 Permissions and Ownership

- [ ] 2.3.1 Ensure NGINX directories and files are owned by root — L1 · Manual
- [ ] 2.3.2 Ensure access to NGINX directories and files is restricted — L1 · Manual
- [ ] 2.3.3 Ensure the NGINX process ID (PID) file is secured — L1 · Manual

#### 2.4 Network Configuration

- [ ] 2.4.1 Ensure NGINX only listens for network connections on authorized ports — L1 · Manual
- [ ] 2.4.2 Ensure requests for unknown host names are rejected — L1 · Manual
- [ ] 2.4.3 Ensure keepalive_timeout is 10 seconds or less, but not 0 — L1 · Manual
- [ ] 2.4.4 Ensure send_timeout is set to 10 seconds or less, but not 0 — L1 · Manual

#### 2.5 Information Disclosure

- [ ] 2.5.1 Ensure server_tokens directive is set to `off` — L1 · Manual
- [ ] 2.5.2 Ensure default error and index.html pages do not reference NGINX — L1 · Manual
- [ ] 2.5.3 Ensure hidden file serving is disabled — L1 · Manual
- [ ] 2.5.4 Ensure the NGINX reverse proxy does not enable information disclosure — L1 LB/Proxy · Manual

### 3 Logging

- [ ] 3.1 Ensure detailed logging is enabled — L1 · Manual
- [ ] 3.2 Ensure access logging is enabled — L1 · Manual
- [ ] 3.3 Ensure error logging is enabled and set to the info logging level — L1 · Manual
- [ ] 3.4 Ensure proxies pass source IP information — L1 LB/Proxy · Manual

### 4 Encryption

#### 4.1 TLS / SSL Configuration

- [ ] 4.1.1 Ensure HTTP is redirected to HTTPS — L1 · Manual
- [ ] 4.1.2 Ensure a trusted certificate and trust chain is installed — L1 · Manual
- [ ] 4.1.3 Ensure private key permissions are restricted — L1 · Manual
- [ ] 4.1.4 Ensure only modern TLS protocols are used — L1 · Manual
- [ ] 4.1.5 Disable weak ciphers — L1 · Manual
- [ ] 4.1.6 Ensure awareness of TLS 1.3 new Diffie-Hellman parameters — L1 · Manual
- [ ] 4.1.7 Ensure Online Certificate Status Protocol (OCSP) stapling is enabled — L1 · Manual
- [ ] 4.1.8 Ensure HTTP Strict Transport Security (HSTS) is enabled — L1 · Manual
- [ ] 4.1.9 Ensure upstream server traffic is authenticated with a client certificate — L1 LB/Proxy · Manual
- [ ] 4.1.10 Ensure the upstream traffic server certificate is trusted — L2 LB/Proxy · Manual
- [ ] 4.1.11 Ensure Secure Session Resumption is Enabled — L1 · Manual
- [ ] 4.1.12 Ensure HTTP/3.0 is used — L2 Web · Manual

### 5 Request Filtering and Restrictions

#### 5.1 Access Control

- [ ] 5.1.1 Ensure allow and deny filters limit access to specific IP addresses — L2 · Manual
- [ ] 5.1.2 Ensure only approved HTTP methods are allowed — L1 · Manual

#### 5.2 Request Limits

- [ ] 5.2.1 Ensure timeout values for reading the client header and body are set correctly — L1 · Manual
- [ ] 5.2.2 Ensure the maximum request body size is set correctly — L1 · Manual
- [ ] 5.2.3 Ensure the maximum buffer size for URIs is defined — L1 · Manual
- [ ] 5.2.4 Ensure the number of connections per IP address is limited — L2 · Manual
- [ ] 5.2.5 Ensure rate limits by IP address are set — L2 · Manual

#### 5.3 Browser Security

- [ ] 5.3.1 Ensure X-Content-Type-Options header is configured and enabled — L1 Web · Manual
- [ ] 5.3.2 Ensure that Content Security Policy (CSP) is enabled and configured properly — L2 Web · Manual
- [ ] 5.3.3 Ensure the Referrer Policy is enabled and configured properly — L2 Web · Manual

## Source

CIS NGINX Benchmark v3.0.0 (12-24-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[enumeration/protocols-and-ports/80-443-http-https]]
- [[owasp-top-10/web/a05-2021-security-misconfiguration]]
- [[owasp-top-10/owasp-top-10]]
- [[web-app-pentesting-notes/host-header-attacks/web-cache-poisoning]]
- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
- [[grc-frameworks/cis-benchmarks/cis-docker]]
