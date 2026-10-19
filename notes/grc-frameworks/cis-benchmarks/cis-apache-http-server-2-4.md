---
title: cis-apache-http-server-2-4
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/web, source/cis]
description: "CIS Apache HTTP Server 2.4 Benchmark v2.3.0 checklist: permissions, modules, logging, TLS, with levels."
source_pdf: CIS_Apache_HTTP_Server_2.4_Benchmark_V2.3.0.pdf
---

# CIS Apache HTTP Server 2.4 Benchmark v2.3.0 (09-23-2025)

## Overview

- **Benchmark version:** v2.3.0, published 09-23-2025; consensus-authored hardening checklist for Apache HTTP Server 2.4.
- **Recommendations:** 87 total — 44 Automated, 43 Manual, across 12 sections.
- **Profiles:** Level 1 (57 items) and Level 2 (30 items). Level 2 extends Level 1 and is not standalone.
- **Checklist legend:** L1/L2 = profile applicability; Auto/Manual = assessment status as labeled in the benchmark.

### Profile definitions

- **Level 1** items are practical and prudent, provide a clear security benefit, and do not inhibit the utility of the technology beyond acceptable means.
- **Level 2** items are intended for environments where security is paramount, act as a defense-in-depth measure, and may negatively inhibit utility or performance.

## Condensed checklist

Titles and key directive values only; see the official benchmark for rationale, audit and remediation steps.

### 1 Planning and Installation

- [ ] 1.1 Ensure the Pre-Installation Planning Checklist Has Been Implemented — L1 · Manual (firewalls, OS hardening, central log monitoring, log rotation, NIDS)
- [ ] 1.2 Ensure the Server Is Not a Multi-Use System — L1 · Manual
- [ ] 1.3 Ensure Apache Is Installed From the Appropriate Binaries — L1 · Manual (prefer vendor-supplied packages)

### 2 Minimize Apache Modules

Minimal, business-required module set; disable the rest by removing or commenting out `LoadModule` lines (audited via `httpd -M`).

- [ ] 2.1 Ensure Only Necessary Authentication and Authorization Modules Are Enabled — L1 · Manual
- [ ] 2.2 Ensure the Log Config Module Is Enabled — L1 · Auto (`LoadModule log_config_module modules/mod_log_config.so`)
- [ ] 2.3 Ensure the WebDAV Modules Are Disabled — L1 · Auto (`##LoadModule dav_module`, `##LoadModule dav_fs_module`)
- [ ] 2.4 Ensure the Status Module Is Disabled — L1 · Auto (`##LoadModule status_module` — enabled by default in source builds)
- [ ] 2.5 Ensure the Autoindex Module Is Disabled — L1 · Auto (`##LoadModule autoindex_module` — enabled by default)
- [ ] 2.6 Ensure the Proxy Modules Are Disabled if not in use — L1 · Auto (`mod_proxy` and all `mod_proxy_*` modules)
- [ ] 2.7 Ensure the User Directories Module Is Disabled — L1 · Auto (`##LoadModule userdir_module`)
- [ ] 2.8 Ensure the Info Module Is Disabled — L1 · Auto (`##LoadModule info_module`)
- [ ] 2.9 Ensure the Basic and Digest Authentication Modules are Disabled — L1 · Auto (when unused)

### 3 Principles, Permissions, and Ownership

- [ ] 3.1 Ensure the Apache Web Server Runs As a Non-Root User — L1 · Auto (unique system account, e.g. `User apache` / `Group apache`; not `daemon`/`nobody`)
- [ ] 3.2 Ensure the Apache User Account Has an Invalid Shell — L1 · Auto (`/sbin/nologin` or `/dev/null`)
- [ ] 3.3 Ensure the Apache User Account Is Locked — L1 · Auto (`passwd -l apache`)
- [ ] 3.4 Ensure Apache Directories and Files Are Owned By Root — L1 · Auto (`chown -R root $APACHE_PREFIX`)
- [ ] 3.5 Ensure the Group Is Set Correctly on Apache Directories and Files — L1 · Auto
- [ ] 3.6 Ensure Other Write Access on Apache Directories and Files Is Restricted — L1 · Auto
- [ ] 3.7–3.10 Ensure the Core Dump Directory, Lock File, Pid File and ScoreBoard File Are Secured — L1 · Manual (`chown root:apache`, `chmod o-rwx`)
- [ ] 3.11–3.13 Ensure Group Write Access and Application Writable Directories Are Properly Restricted — L1 · Manual (`chown root`, `chmod o-w`)

### 4 Apache Access Control

- [ ] 4.1 Ensure Access to OS Root Directory Is Denied By Default — L1 · Auto (`Require all denied` in root `<Directory>`; Order/Deny/Allow deprecated but accepted)
- [ ] 4.2 Ensure Appropriate Access to Web Content Is Allowed — L1 · Manual (allow web content explicitly with `Require`/`Allow`)
- [ ] 4.3 Ensure OverRide Is Disabled for the OS Root Directory — L1 · Auto (`AllowOverride None`, no `AllowOverrideList`)
- [ ] 4.4 Ensure OverRide Is Disabled for All Directories — L1 · Auto (centralized config; `.htaccess` ignored entirely)

### 5 Minimize Features, Content and Options

- [ ] 5.1 Ensure Options for the OS Root Directory Are Restricted — L1 · Auto (`Options None` in root `<Directory>`; default is `Indexes FollowSymLinks`)
- [ ] 5.2 Ensure Options for the Web Root Directory Are Restricted — L2 · Auto (`Options None` or `Multiviews`)
- [ ] 5.3 Ensure Options for Other Directories Are Minimized — L2 · Auto
- [ ] 5.4 Ensure Default HTML Content Is Removed — L1 · Manual
- [ ] 5.5–5.6 Ensure the Default CGI Content printenv / test-cgi Scripts Are Removed — L2 · Manual
- [ ] 5.7 Ensure HTTP Request Methods Are Restricted — L2 · Manual (`<LimitExcept GET POST OPTIONS> Require all denied </LimitExcept>`, or experimental `AllowMethods`)
- [ ] 5.8 Ensure the HTTP TRACE Method Is Disabled — L1 · Auto (`TraceEnable off` at server level; default TRACE enabled)
- [ ] 5.9 Ensure Old HTTP Protocol Versions Are Disallowed — L1 · Auto (`RewriteCond %{THE_REQUEST} !HTTP/1\.1$` + `RewriteRule .* - [F]` via mod_rewrite or mod_security)
- [ ] 5.10 Ensure Access to .ht* Files Is Restricted — L1 · Auto (`<FilesMatch "^\.ht"> Require all denied </FilesMatch>`)
- [ ] 5.11–5.12 Ensure Access to .git / .svn Files Is Restricted — L1 · Manual
- [ ] 5.13 Ensure Access to Inappropriate File Extensions Is Restricted — L2 · Manual
- [ ] 5.14 Ensure IP Address Based Requests Are Disallowed — L2 · Auto (mod_rewrite rejects bare-IP URLs)
- [ ] 5.15 Ensure the IP Addresses for Listening for Requests Are Specified — L2 · Auto (`Listen 10.1.2.3:80`, never bare `Listen 80` or `0.0.0.0`)
- [ ] 5.16 Ensure Browser Framing Is Restricted — L2 · Auto (`Header always set X-Frame-Options SAMEORIGIN` or CSP frame-ancestors)
- [ ] 5.17 Ensure HTTP Header Referrer-Policy is set appropriately — L2 · Manual (`Header set Referrer-Policy "<Directive>"`)
- [ ] 5.18 Ensure HTTP Header Permissions-Policy is set appropriately — L2 · Manual (`Header set Permissions-Policy "<Directive> <allowlist>"`)

### 6 Operations – Logging, Monitoring and Maintenance

- [ ] 6.1 Ensure the Error Log Filename and Severity Level Are Configured Correctly — L1 · Auto (`ErrorLog "logs/error_log"`, `LogLevel notice core:info` so 404s are captured)
- [ ] 6.2 Ensure a Syslog Facility Is Configured for Error Logging — L2 · Manual
- [ ] 6.3 Ensure the Server Access Log Is Configured Correctly — L1 · Manual (`LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"" combined` + `CustomLog log/access_log combined`; `%{X-Forwarded-For}i` behind load balancers)
- [ ] 6.4 Ensure Log Storage and Rotation Is Configured Correctly — L1 · Manual (retain at least 3 months / 13 weeks without central logging)
- [ ] 6.5 Ensure Applicable Patches Are Applied — L1 · Manual
- [ ] 6.6 Ensure ModSecurity Is Installed and Enabled — L2 · Auto (WAF without a rule set adds no protection)
- [ ] 6.7 Ensure the OWASP ModSecurity Core Rule Set Is Installed and Enabled — L2 · Manual

### 7 SSL/TLS Configuration

- [ ] 7.1 Ensure mod_ssl and/or mod_nss Is Installed — L1 · Auto (`httpd -M | egrep 'ssl_module|nss_module'`)
- [ ] 7.2 Ensure a Valid Trusted Certificate Is Installed — L1 · Manual (CA-signed, unexpired, matching CN/SAN; no MD5/SHA1 signatures)
- [ ] 7.3 Ensure the Server's Private Key Is Protected — L1 · Manual (`SSLCertificateFile` / `SSLCertificateKeyFile`; key readable only by root)
- [ ] 7.4 Ensure the TLSv1.0 and TLSv1.1 Protocols are Disabled — L1 · Manual (`SSLProtocol +TLSv1.2 +TLSv1.3`; default `SSLProtocol all`)
- [ ] 7.5 Ensure Weak SSL/TLS Ciphers Are Disabled — L1 · Manual (`SSLHonorCipherOrder On`, `SSLCipherSuite ALL:!EXP:!NULL:!LOW:!SSLv2:!RC4:!aNULL`)
- [ ] 7.6 Ensure Insecure SSL Renegotiation Is Not Enabled — L1 · Manual (`SSLInsecureRenegotiation off`)
- [ ] 7.7 Ensure SSL Compression is not Enabled — L1 · Manual (`SSLCompression off`; CRIME attack)
- [ ] 7.8 Ensure Medium Strength SSL/TLS Ciphers Are Disabled — L1 · Manual (extend suite with `!3DES!IDEA`)
- [ ] 7.9 Ensure All Web Content is Accessed via HTTPS — L1 · Manual (`Redirect permanent / https://…`; HTTP must not serve significant content)
- [ ] 7.10 Ensure OCSP Stapling Is Enabled — L2 · Manual (`SSLUseStapling On` + `SSLStaplingCache "shmcb:logs/ssl_staple_cache(512000)"`)
- [ ] 7.11 Ensure HTTP Strict Transport Security Is Enabled — L2 · Manual (`Header always set Strict-Transport-Security "max-age=600"` or with `includeSubDomains; preload`)
- [ ] 7.12 Ensure Only Cipher Suites That Provide Forward Secrecy Are Enabled — L2 · Manual (`SSLCipherSuite ECDHE:DHE:!NULL:!SSLv2:!RC4:!aNULL:!3DES:!IDEA`; verify with sslscan or SSL Labs that all accepted ciphers start with ECDHE-/DHE-)

### 8 Information Leakage

- [ ] 8.1 Ensure ServerTokens is Set to 'Prod' or 'ProductOnly' — L1 · Auto (banner shows only "Apache")
- [ ] 8.2 Ensure ServerSignature Is Not Enabled — L1 · Auto (`ServerSignature Off`)
- [ ] 8.3 Ensure All Default Apache Content Is Removed — L2 · Manual
- [ ] 8.4 Ensure ETag Response Header Fields Do Not Include Inodes — L2 · Auto (`FileETag None` or `MTime Size`; never `inode`/`all`)

### 9 Denial of Service Mitigations

- [ ] 9.1 Ensure the TimeOut Is Set to 10 or Less — L1 · Auto (`Timeout 10`; default 60)
- [ ] 9.2 Ensure KeepAlive Is Enabled — L1 · Auto (`KeepAlive On`)
- [ ] 9.3 Ensure MaxKeepAliveRequests is Set to a Value of 100 or Greater — L1 · Auto (default 100)
- [ ] 9.4 Ensure KeepAliveTimeout is Set to a Value of 15 or Less — L1 · Auto
- [ ] 9.5 Ensure the Timeout Limits for Request Headers is Set to 40 or Less — L1 · Manual
- [ ] 9.6 Ensure Timeout Limits for the Request Body is Set to 20 or Less — L1 · Manual

### 10 Request Limits (all L2, Automated)

- [ ] 10.1 Ensure the LimitRequestLine directive is Set to 8190 or less but not 0
- [ ] 10.2 Ensure the LimitRequestFields Directive is Set to 100 or Less but not 0
- [ ] 10.3 Ensure the LimitRequestFieldsize Directive is Set to 8190 or Less
- [ ] 10.4 Ensure the LimitRequestBody Directive is Set to 102400 or Less but not 0

### 11 Enable SELinux to Restrict Apache Processes (all L2)

- [ ] 11.1 Ensure SELinux Is Enabled in Enforcing Mode — Auto (`SELINUX=enforcing` in `/etc/selinux/config`, `setenforce 1`)
- [ ] 11.2 Ensure Apache Processes Run in the httpd_t Confined Context — Manual
- [ ] 11.3 Ensure the httpd_t Type is Not in Permissive Mode — Auto
- [ ] 11.4 Ensure Only the Necessary SELinux Booleans are Enabled — Manual

### 12 Enable AppArmor to Restrict Apache Processes (all L2)

- [ ] 12.1 Ensure the AppArmor Framework Is Enabled — Auto (`aa-status --enabled`)
- [ ] 12.2 Ensure the Apache AppArmor Profile Is Configured Properly — Manual
- [ ] 12.3 Ensure Apache AppArmor Profile is in Enforce Mode — Auto

Note: SELinux and AppArmor provide similar controls and it is not recommended to use both on the same system; distribution determines which applies.

## Related

- [[grc-frameworks/cis-benchmarks/cis-nginx]]
