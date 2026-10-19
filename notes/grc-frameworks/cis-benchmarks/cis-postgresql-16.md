---
title: cis-postgresql-16
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS PostgreSQL 16 Benchmark v1.1.0 checklist: installation, logging, access, replication, with levels."
source_pdf: CIS_PostgreSQL_16_Benchmark_v1.1.0.pdf
---

# CIS PostgreSQL 16 Benchmark v1.1.0 (06-30-2025)

## Overview

- **Product:** PostgreSQL 16
- **Benchmark version:** v1.1.0 (2025-06-30)
- **Profiles:** Level 1 - PostgreSQL and Level 1 - PostgreSQL on Linux. There is no Level 2 profile in this version.
- **Recommendations:** 71 total (41 Automated, 30 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Installation and Patches | 7 |
| 2 Directory and File Permissions | 4 |
| 3 Logging And Auditing | 26 |
| 4 User Access and Authorization | 9 |
| 5 Connection and Login | 6 |
| 6 PostgreSQL Settings | 11 |
| 7 Replication | 5 |
| 8 Special Configuration Considerations | 3 |

## Lab relevance

- **Network exposure (5.2, 5.3, 5.4):** `listen_addresses` bound deliberately and `pg_hba.conf` entries tight for local socket and host TCP; in the Docker host this means reachable only from the Gitea container/network.
- **Authentication (5.6, 6.8, 6.9, 6.10):** strong password hashing and complexity, TLS enabled for client connections, TLS 1.0/1.1 and weak ciphers disabled.
- **Credentials hygiene (1.6, 1.7, 5.1, 2.4):** no PGPASSWORD in profiles or environment, no passwords on the command line or in the service file; use `.pgpass`/secrets mounts for Gitea's DB credentials.
- **Least privilege (4.1-4.9):** revoke excessive admin, function and DML privileges, consider RLS (4.7) and `set_user` (4.8); give Gitea a dedicated non-superuser role.
- **Logging (section 3, 26 items):** log destinations, collector, file permissions and rotation, connection/disconnection and statement error logging.
- **Backups and replication (7.3, 7.4, 8.2):** base backups, WAL archiving and pgBackRest (the `L1 on Linux` items) to protect the Gitea repositories' metadata.
- **Files and patching (2.1-2.3, 1.5):** file permission mask, extension directory ownership and security updates; if PostgreSQL runs in a container, map these to the image and data volume instead.

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Installation and Patches

- [ ] 1.1 Ensure packages are obtained from authorized repositories — L1 on Linux · Manual
- [ ] 1.2 Install only required packages — L1 · Manual
- [ ] 1.3 Ensure systemd Service Files Are Enabled — L1 on Linux · Automated
- [ ] 1.4 Ensure Data Cluster Initialized Successfully — L1 on Linux · Automated
- [ ] 1.5 Ensure the Latest Security Patches are Applied — L1 · Manual
- [ ] 1.6 Verify That 'PGPASSWORD' is Not Set in Users' Profiles — L1 · Automated
- [ ] 1.7 Verify That the 'PGPASSWORD' Environment Variable is Not in Use — L1 · Automated

### 2 Directory and File Permissions

- [ ] 2.1 Ensure the file permissions mask is correct — L1 on Linux · Manual
- [ ] 2.2 Ensure extension directory has appropriate ownership and permissions — L1 · Automated
- [ ] 2.3 Disable PostgreSQL Command History — L1 · Automated
- [ ] 2.4 Ensure Passwords are Not Stored in the service file — L1 · Manual

### 3 Logging And Auditing

#### 3.1 PostgreSQL Logging

- [ ] 3.1.2 Ensure the log destinations are set correctly — L1 · Automated
- [ ] 3.1.3 Ensure the logging collector is enabled — L1 · Automated
- [ ] 3.1.4 Ensure the log file destination directory is set correctly — L1 · Automated
- [ ] 3.1.5 Ensure the filename pattern for log files is set correctly — L1 · Automated
- [ ] 3.1.6 Ensure the log file permissions are set correctly — L1 · Automated
- [ ] 3.1.7 Ensure 'log_truncate_on_rotation' is enabled — L1 · Automated
- [ ] 3.1.8 Ensure the maximum log file lifetime is set correctly — L1 · Automated
- [ ] 3.1.9 Ensure the maximum log file size is set correctly — L1 · Automated
- [ ] 3.1.10 Ensure the correct syslog facility is selected — L1 · Manual
- [ ] 3.1.11 Ensure syslog messages are not suppressed — L1 · Automated
- [ ] 3.1.12 Ensure syslog messages are not lost due to size — L1 · Automated
- [ ] 3.1.13 Ensure the program name for PostgreSQL syslog messages is correct — L1 · Automated
- [ ] 3.1.14 Ensure the correct messages are written to the server log — L1 · Automated
- [ ] 3.1.15 Ensure the correct SQL statements generating errors are recorded — L1 · Automated
- [ ] 3.1.16 Ensure 'debug_print_parse' is disabled — L1 · Automated
- [ ] 3.1.17 Ensure 'debug_print_rewritten' is disabled — L1 · Automated
- [ ] 3.1.18 Ensure 'debug_print_plan' is disabled — L1 · Automated
- [ ] 3.1.19 Ensure 'debug_pretty_print' is enabled — L1 · Automated
- [ ] 3.1.20 Ensure 'log_connections' is enabled — L1 · Automated
- [ ] 3.1.21 Ensure 'log_disconnections' is enabled — L1 · Automated
- [ ] 3.1.22 Ensure 'log_error_verbosity' is set correctly — L1 · Automated
- [ ] 3.1.23 Ensure 'log_hostname' is set correctly — L1 · Automated
- [ ] 3.1.24 Ensure 'log_line_prefix' is set correctly — L1 · Automated
- [ ] 3.1.25 Ensure 'log_statement' is set correctly — L1 · Automated
- [ ] 3.1.26 Ensure 'log_timezone' is set correctly — L1 · Automated
- [ ] 3.2 Ensure the PostgreSQL Audit Extension (pgAudit) is enabled — L1 · Automated

### 4 User Access and Authorization

- [ ] 4.1 Ensure Interactive Login is Disabled — L1 · Manual
- [ ] 4.2 Ensure sudo is configured correctly — L1 on Linux · Manual
- [ ] 4.3 Ensure excessive administrative privileges are revoked — L1 · Manual
- [ ] 4.4 Lock Out Accounts if Not Currently in Use — L1 · Manual
- [ ] 4.5 Ensure excessive function privileges are revoked — L1 · Automated
- [ ] 4.6 Ensure excessive DML privileges are revoked — L1 · Manual
- [ ] 4.7 Ensure Row Level Security (RLS) is configured correctly — L1 · Manual
- [ ] 4.8 Ensure the set_user extension is installed — L1 · Automated
- [ ] 4.9 Make use of predefined roles — L1 · Manual

### 5 Connection and Login

- [ ] 5.1 Do Not Specify Passwords in the Command Line — L1 · Manual
- [ ] 5.2 Ensure PostgreSQL is Bound to an IP Address — L1 · Manual
- [ ] 5.3 Ensure login via "local" UNIX Domain Socket is configured correctly — L1 on Linux · Manual
- [ ] 5.4 Ensure login via "host" TCP/IP Socket is configured correctly — L1 on Linux · Manual
- [ ] 5.5 Ensure per-account connection limits are used — L1 · Automated
- [ ] 5.6 Ensure Password Complexity is configured — L1 · Manual

### 6 PostgreSQL Settings

- [ ] 6.1 Understanding attack vectors and runtime parameters — L1 · Manual
- [ ] 6.2 Ensure 'backend' runtime parameters are configured correctly — L1 · Automated
- [ ] 6.3 Ensure 'Postmaster' Runtime Parameters are Configured — L1 · Manual
- [ ] 6.4 Ensure 'SIGHUP' Runtime Parameters are Configured — L1 · Manual
- [ ] 6.5 Ensure 'Superuser' Runtime Parameters are Configured — L1 · Manual
- [ ] 6.6 Ensure 'User' Runtime Parameters are Configured — L1 · Manual
- [ ] 6.7 Ensure FIPS 140-2 OpenSSL Cryptography Is Used — L1 on Linux · Automated
- [ ] 6.8 Ensure TLS is enabled and configured correctly — L1 · Automated
- [ ] 6.9 Ensure the TLSv1.0 and TLSv1.1 Protocols are Disabled — L1 · Automated
- [ ] 6.10 Ensure Weak SSL/TLS Ciphers Are Disabled — L1 on Linux · Automated
- [ ] 6.11 Ensure the pgcrypto extension is installed and configured correctly — L1 · Manual

### 7 Replication

- [ ] 7.1 Ensure a replication-only user is created and used for streaming replication — L1 · Manual
- [ ] 7.2 Ensure logging of replication commands is configured — L1 · Manual
- [ ] 7.3 Ensure base backups are configured and functional — L1 · Manual
- [ ] 7.4 Ensure WAL archiving is configured and functional — L1 on Linux · Automated
- [ ] 7.5 Ensure streaming replication parameters are configured correctly — L1 · Manual

### 8 Special Configuration Considerations

- [ ] 8.1 Ensure PostgreSQL subdirectory locations are outside the data cluster — L1 · Manual
- [ ] 8.2 Ensure the backup and restore tool, 'pgBackRest', is installed and configured — L1 on Linux · Automated
- [ ] 8.3 Ensure miscellaneous configuration settings are correct — L1 · Manual

## Source

CIS PostgreSQL 16 Benchmark v1.1.0 (06-30-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[hacking-cheat-sheets/sql-injection-cheat-sheet]]
- [[owasp-top-10/web/a03-2021-injection]]
- [[owasp-top-10/web/a05-2021-security-misconfiguration]]
- [[enumeration/protocols-and-ports/3306-mysql]]
- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
- [[grc-frameworks/cis-benchmarks/cis-docker]]
