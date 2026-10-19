---
title: cis-iis-10
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/windows, platform/web, source/cis]
description: "CIS Microsoft IIS 10 Benchmark v1.2.1 checklist: site configuration, authentication, logging, TLS, with levels."
source_pdf: CIS_Microsoft_IIS_10_Benchmark_v1.2.1.pdf
---

# CIS Microsoft IIS 10 Benchmark v1.2.1 (07-17-2023)

## Overview

- **Product:** Microsoft IIS 10, intended for all versions of Microsoft Windows IIS 10; tested on Microsoft Windows Server 2022 Datacenter.
- **Benchmark version:** v1.2.1 (07-17-2023); initial release 03/31/2017 as v1.0.0.
- **Profiles:** Level 1 - IIS 10 and Level 2 - IIS 10. Level 2 extends Level 1 and is not a standalone profile.
- **Recommendations:** 55 total (43 Automated, 12 Manual; 40 Level 1, 15 Level 2).
- **Assessment status:** every recommendation is marked Automated (can be fully validated pass/fail, includes automation info) or Manual (all or some steps need manual validation; expected state can vary by environment).
- **Audit/remediation tooling:** each item gives AppCmd.exe and PowerShell commands plus IIS Manager GUI steps where applicable; protocol and cipher items are set via SCHANNEL registry keys.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Basic Configurations | 7 |
| 2 Configure Authentication and Authorization | 8 |
| 3 ASP.NET Configuration Recommendations | 12 |
| 4 Request Filtering and Other Restriction Modules | 11 |
| 5 IIS Logging Recommendations | 3 |
| 6 FTP Requests | 2 |
| 7 Transport Encryption | 12 |

## Profile applicability

- **Level 1 - IIS 10:** items apply to Microsoft IIS 10 running on Microsoft Windows Server 2016 and intend to be practical and prudent, provide a clear security benefit, and not inhibit the utility of the technology beyond acceptable means.
- **Level 2 - IIS 10:** extends the Level 1 profile; items apply to Microsoft IIS 10.0 running on Microsoft Windows Server 2016 and are intended for environments or use cases where security is paramount, act as a defense-in-depth measure, and may negatively inhibit the utility or performance of the technology.
- Level 2 items in this benchmark: forms authentication cookies (2.4), no credentials in config files (2.8), debug off (3.2), custom errors not off (3.3), stack tracing off (3.5), httpcookie session state (3.6), .NET 3.5 machineKey (3.8), X-Powered-By removal (3.11), Server header removal (3.12), request size/URL/query filters (4.1-4.4), HSTS header (7.1), cipher suite ordering (7.12).

## Recommendation checklist

Titles, levels and assessment status only; see the official benchmark for description, rationale, impact, audit and remediation steps.

### 1 Basic Configurations

- [ ] 1.1 (L1) Ensure 'Web content' is on non-system partition — Manual
- [ ] 1.2 (L1) Ensure 'Host headers' are on all sites — Automated
- [ ] 1.3 (L1) Ensure 'Directory browsing' is set to Disabled — Automated
- [ ] 1.4 (L1) Ensure 'application pool identity' is configured for all application pools — Automated
- [ ] 1.5 (L1) Ensure 'unique application pools' is set for sites — Automated
- [ ] 1.6 (L1) Ensure 'application pool identity' is configured for anonymous user identity — Automated
- [ ] 1.7 (L1) Ensure 'WebDav' feature is disabled — Automated

### 2 Configure Authentication and Authorization

- [ ] 2.1 (L1) Ensure 'global authorization rule' is set to restrict access — Manual
- [ ] 2.2 (L1) Ensure access to sensitive site features is restricted to authenticated principals only — Manual
- [ ] 2.3 (L1) Ensure 'forms authentication' require SSL — Automated
- [ ] 2.4 (L2) Ensure 'forms authentication' is set to use cookies — Automated
- [ ] 2.5 (L1) Ensure 'cookie protection mode' is configured for forms authentication — Automated
- [ ] 2.6 (L1) Ensure transport layer security for 'basic authentication' is configured — Automated
- [ ] 2.7 (L1) Ensure 'passwordFormat' is not set to clear — Automated
- [ ] 2.8 (L2) Ensure 'credentials' are not stored in configuration files — Automated

### 3 ASP.NET Configuration Recommendations

- [ ] 3.1 (L1) Ensure 'deployment method retail' is set — Manual
- [ ] 3.2 (L2) Ensure 'debug' is turned off — Automated
- [ ] 3.3 (L2) Ensure custom error messages are not off — Automated
- [ ] 3.4 (L1) Ensure IIS HTTP detailed errors are hidden from displaying remotely — Automated
- [ ] 3.5 (L2) Ensure ASP.NET stack tracing is not enabled — Automated
- [ ] 3.6 (L2) Ensure 'httpcookie' mode is configured for session state — Automated
- [ ] 3.7 (L1) Ensure 'cookies' are set with HttpOnly attribute — Automated
- [ ] 3.8 (L2) Ensure 'MachineKey validation method - .Net 3.5' is configured — Automated
- [ ] 3.9 (L1) Ensure 'MachineKey validation method - .Net 4.5' is configured — Automated
- [ ] 3.10 (L1) Ensure global .NET trust level is configured — Automated
- [ ] 3.11 (L2) Ensure X-Powered-By Header is removed — Manual
- [ ] 3.12 (L2) Ensure Server Header is removed — Manual

### 4 Request Filtering and Other Restriction Modules

Request Filtering (introduced in IIS 7.0) provides configurable rules to allow or reject request types at server, web site, or web application levels; core UrlScan features were incorporated into it. Request Filtering and IP and Domain Restrictions must be enabled as a role service under IIS.

- [ ] 4.1 (L2) Ensure 'maxAllowedContentLength' is configured — Manual
- [ ] 4.2 (L2) Ensure 'maxURL request filter' is configured — Automated
- [ ] 4.3 (L2) Ensure 'MaxQueryString request filter' is configured — Automated
- [ ] 4.4 (L2) Ensure non-ASCII characters in URLs are not allowed — Automated
- [ ] 4.5 (L1) Ensure Double-Encoded requests will be rejected — Automated
- [ ] 4.6 (L1) Ensure 'HTTP Trace Method' is disabled — Manual
- [ ] 4.7 (L1) Ensure Unlisted File Extensions are not allowed — Automated
- [ ] 4.8 (L1) Ensure Handler is not granted Write and Script/Execute — Manual
- [ ] 4.9 (L1) Ensure 'notListedIsapisAllowed' is set to false — Automated
- [ ] 4.10 (L1) Ensure 'notListedCgisAllowed' is set to false — Automated
- [ ] 4.11 (L1) Ensure 'Dynamic IP Address Restrictions' is enabled — Manual

### 5 IIS Logging Recommendations

- [ ] 5.1 (L1) Ensure Default IIS web log location is moved — Automated
- [ ] 5.2 (L1) Ensure Advanced IIS logging is enabled — Automated
- [ ] 5.3 (L1) Ensure 'ETW Logging' is enabled — Manual

### 6 FTP Requests

- [ ] 6.1 (L1) Ensure FTP requests are encrypted — Manual
- [ ] 6.2 (L1) Ensure FTP Logon attempt restrictions is enabled — Manual

### 7 Transport Encryption

For SSL/TLS there are two registry paths controlling a protocol state: TLS client and TLS server. A web server normally acts as the TLS server; where it acts as a client (for example dynamic content generation from a remote database), server protocol and cipher suite preferences take precedence. `Enabled = 0` disables a protocol in a way that cannot be overridden by application settings; `DisabledByDefault` only stops the Hello over that protocol and can be overridden by application-specific TLS code.

- [ ] 7.1 (L2) Ensure HSTS Header is set — Manual
- [ ] 7.2 (L1) Ensure SSLv2 is Disabled — Automated
- [ ] 7.3 (L1) Ensure SSLv3 is Disabled — Automated
- [ ] 7.4 (L1) Ensure TLS 1.0 is Disabled — Automated
- [ ] 7.5 (L1) Ensure TLS 1.1 is Disabled — Automated
- [ ] 7.6 (L1) Ensure TLS 1.2 is Enabled — Automated
- [ ] 7.7 (L1) Ensure NULL Cipher Suites is Disabled — Automated
- [ ] 7.8 (L1) Ensure DES Cipher Suites is Disabled — Automated
- [ ] 7.9 (L1) Ensure RC4 Cipher Suites is Disabled — Automated
- [ ] 7.10 (L1) Ensure AES 128/128 Cipher Suite is Disabled — Automated
- [ ] 7.11 (L1) Ensure AES 256/256 Cipher Suite is Enabled — Automated
- [ ] 7.12 (L2) Ensure TLS Cipher Suite ordering is Configured — Automated

## Notable defaults (from the benchmark)

- Directory browsing is disabled by default in IIS; host headers are not required or set up automatically.
- DefaultAppPool uses the ApplicationPoolIdentity account; the default anonymous user identity is the IUSR virtual account.
- WebDAV Publishing is disabled by default; the default handlers accessPolicy is `Read, Script`.
- `<deployment retail>` is not in machine.config by default; ASP.NET web applications run under full trust by default; the default customErrors mode is `RemoteOnly`; ASP.NET 2.0 does not force cookies to httpOnly.
- Machine key validation defaults: SHA1 for .NET 3.5, SHA256 for .NET 4.5.
- Request Filtering defaults: maxAllowedContentLength 30000000 (~28.6 MB), maxURL 4096; unlisted file extensions are allowed, high-bit characters are allowed, double-escaping is disallowed, and the TRACE verb is not filtered.
- Default web log location is `%SystemDrive%\inetpub\logs\LogFiles`; IIS Advanced Logging is enabled by default; Dynamic IP Restrictions are not enabled by default.
- FTP sites are not SSL enabled by default; FTP logon attempt restrictions are not enabled when FTP is installed.
- The server header default is `Microsoft-IIS/10.0`; TLS 1.2 is the most recent and mature protocol for protecting HTTP traffic per this benchmark; recommended HSTS max-age is 480 seconds or greater.

## Source

CIS Microsoft IIS 10 Benchmark v1.2.1 (07-17-2023), Center for Internet Security.

## Related

- [[grc-frameworks/cis-benchmarks/cis-windows-11-enterprise]]
