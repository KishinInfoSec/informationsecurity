---
title: cis-mongodb-8
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS MongoDB 8 Benchmark v1.0.0 checklist: authentication, encryption, auditing, network exposure, with levels."
source_pdf: CIS_MongoDB8_Benchmark_v1.0.0.pdf
---

# CIS MongoDB 8 Benchmark v1.0.0 (08-11-2025)

## Overview

- **Product:** MongoDB 8
- **Benchmark version:** v1.0.0 (cover date 08-11-2025)
- **Profiles:** Level 1 - MongoDB and Level 2 - MongoDB
- **Recommendations:** 22 total across 7 sections; each is marked Automated or Manual
- Most checks audit `/etc/mongod.conf` (Ubuntu `cat`/`grep`, Windows `type`/`findstr`) and remediate by editing that file and restarting the instance.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Installation and Patching | 1.1 |
| 2 Authentication | 2.1-2.3 |
| 3 Authorization | 3.1-3.5 |
| 4 Data Encryption | 4.1-4.5 |
| 5 Audit Logging | 5.1-5.4 |
| 6 Operating System Hardening | 6.1-6.3 |
| 7 File Permissions | 7.1-7.2 |

## Profile applicability

- **Level 1 - MongoDB:** practical and prudent; provides a clear security benefit; does not inhibit the utility of the technology beyond acceptable means.
- **Level 2 - MongoDB:** extends Level 1 (not a standalone profile); items apply where security is paramount, act as a defense-in-depth measure, or may negatively inhibit utility or performance.
- Level 2 items in this benchmark: 2.3 (sharded cluster auth), 3.5 (superuser/admin role review), 4.1 (legacy TLS disabled), 4.4 (FIPS), 4.5 (encryption at rest), 5.2 (audit filters), 5.3 (`SystemLog.quiet` off), 5.4 (`systemLog.logAppend`), 6.2 (OS resource limits), 6.3 (server-side scripting disabled).

## Installation and patching

- **1.1 Ensure the appropriate MongoDB software version/patches are installed (Manual, L1):** install the most recent version compatible with operational needs and track minor security patches/CVE fixes; at a minimum the version must be supported. Audit with `mongo --version` / `db.version()` (or `mongod.exe --version` on Windows). Default: patches are not installed by default.

## Authentication and authorization

- **2.1 Ensure Authentication is configured (Automated, L1):** all clients, users, and servers must authenticate before access. Enable access control in `mongod.conf`:
  ```yaml
  security:
      authorization: "enabled"
  ```
  Default is disabled. Supported mechanisms: SCRAM (default) and x.509; MongoDB Enterprise adds LDAP proxy and Kerberos. Create the system user administrator (e.g. `root` role on `admin`) *before* enabling authorization, with organizationally defined password length/complexity — MongoDB has no intrinsic password complexity check and no lockout after failed logins, so it is prone to brute force.
- **2.2 Ensure that MongoDB does not bypass authentication via the localhost exception (Automated, L1):** the localhost exception gives all connections from localhost full access while no users exist; it must be disabled once the first user is created:
  ```yaml
  setParameter:
    enableLocalhostAuthBypass: false
  ```
  Or `mongod --setParameter enableLocalhostAuthBypass=0`. Default is true.
- **2.3 Ensure authentication is enabled in the sharded cluster (Automated, L2):** every component of a sharded cluster must authenticate to every other component. For production use x.509 certificate authentication over TLS (`clusterAuthMode: x509`, `authenticationMechanisms: MONGODB-X509`, with `PEMKeyFile`, `clusterFile`, `CAFile` configured). Keyfile authentication (`keyFile`) is a bare-minimum form of security suited only for testing/development.
- **3.1 Ensure least privilege for database accounts (Manual, L1):** do not leave `dbOwner`, `userAdmin`, or `userAdminAnyDatabase` scoped to the `admin` database — holders can assign themselves any privilege on any database. Audit:
  ```
  db.system.users.find(
    {"roles.role":{$in:["dbOwner","userAdmin","userAdminAnyDatabase"]},"roles.db":"admin"} )
  ```
- **3.2 Ensure that role-based access control is enabled and configured appropriately (Manual, L1):** establish roles, assign privileges to roles, assign users to roles, and remove any individual privileges now covered by roles. Outside role assignments a user has no access; RBAC is not enabled by default.
- **3.3 Ensure that MongoDB is run using a non-privileged, dedicated service account (Manual, L1):** never run as `root`. Audit with `ps -ef | grep -E "mongos|mongod"`. Set data files, keyfile, and SSL private key readable only by the mongod/mongos user; log files writable only by that user and readable only by root.
- **3.4 Ensure that each role for each MongoDB database is needed and grants only the necessary privileges (Manual, L1):** periodically review and drop unneeded roles/privileges. Audit with `db.runCommand({ rolesInfo: 1, showPrivileges: true, showBuiltinRoles: true })`.
- **3.5 Review Superuser/Admin Roles (Manual, L2):** review holders of `dbOwner`, `userAdmin`, `userAdminAnyDatabase` and the `root` composite (readWriteAnyDatabase, dbAdminAnyDatabase, userAdminAnyDatabase, clusterAdmin, restore) plus cluster admin roles such as `hostManager` to minimize privileged unwanted access.

## Encryption at rest and in transit

- **4.1 Ensure legacy TLS protocols are disabled (Automated, L2):** remove SSL 3.0, TLS 1.0, and 1.1; enable TLS 1.2 and 1.3:
  ```yaml
  net:
    tls:
      mode: requireTLS
      certificateKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
      disabledProtocols: TLS1_0,TLS1_1
  ```
- **4.2 Ensure Weak Protocols are Disabled (Automated, L1):** set `net.ssl.disabledProtocols` (or `net.tls.disabledProtocols`) to include `TLS1_0,TLS1_1`. TLS 1.0 is vulnerable to BEAST in CBC mode; TLS 1.1 lacks AEAD; NIST SP 800-52r2 requires TLS 1.2 with FIPS-based cipher suites and TLS 1.3 support. Disabled-protocol connections fail, which may break older clients.
- **4.3 Ensure Encryption of Data in Transit TLS or SSL (Transport Encryption) (Automated, L1):** protect all incoming/outgoing connections, including mongod-to-mongos and application-to-MongoDB:
  ```yaml
  net:
    tls:
      mode: requireTLS
      certificateKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
  ```
  `net.tls.mode` values: `disabled`, `allowTLS`, `preferTLS`, `requireTLS` (server uses and accepts only TLS). SSL was deprecated as of MongoDB 4.2. Prevents sniffing and MITM of cleartext traffic.
- **4.4 Ensure Federal Information Processing Standard (FIPS) is enabled (Automated, L2):** run with a FIPS 140-2 certified OpenSSL library; ensure the certificate is FIPS compliant:
  ```yaml
  net:
    tls:
      FIPSMode: true
  ```
  Verify the log message `FIPS 140-2 mode activated`. FIPS is a property of the encryption system, not access control — the access control system must also use FIPS-compliant encryption.
- **4.5 Ensure Encryption of Data at Rest (Manual, L2):** required for compliance with HIPAA, PCI-DSS, and FERPA. The encrypted storage engine encrypts a master key → per-database keys → data; only the master key is external. Two key-management options: third-party KMIP appliance (recommended) or local keyfile (`--enableEncryption 'yes'`, `--encryptionKeyFile '<path to keyfile>'`). Encryption is transparent in the storage layer; data is unencrypted only in memory and in transit. Rotate keys. MongoDB Enterprise only.

## Audit logging

- **5.1 Ensure that system activity is audited (Automated, L1):** track access and changes to configurations and data via the Enterprise system auditing facility. Set `auditLog.destination` to `syslog`, `console`, or `file` (with `--auditFormat JSON` or `BSON` and `--auditPath`); JSON to file degrades performance more than BSON.
- **5.2 Ensure that audit filters are configured properly (Manual, L2):** configure `auditLog.filter` (`--auditFilter`) per organizational requirements so incidents can be backtracked. Enterprise only.
- **5.3 Ensure that logging captures as much information as possible (Automated, L2):** `SystemLog.quiet` suppresses connection events, authentication events, replication sync activity, and evidence of impactful commands (drop, dropIndexes, validate); set:
  ```yaml
  SystemLog:
    quiet: false
  ```
  Enterprise only.
- **5.4 Ensure that new entries are appended to the end of the log file (Automated, L2):** without `systemLog.logAppend: true`, new entries overwrite old ones on mongod/mongos restart, destroying log data needed for investigation and retention.

## Network and bind exposure

- **6.1 Ensure that MongoDB uses a non-default port (Automated, L1):** change the port away from 27017 — standard ports are scanned by automated attacks. In `mongod.conf`:
  ```yaml
  net:
    port: <organization-defined port>
    bindIp: <organization-defined IP>
  ```
  Note the benchmark's own impact statement: this only helps avoid detection ("fly under the radar"); it adds no real safety by itself.

## OS-level hardening

- **6.2 Ensure that operating system resource limits are set for MongoDB (Manual, L2):** per-process/per-user ulimits prevent a single user from consuming too many resources. Recommended: file size `f`, cpu time `t`, virtual memory `v`, memory size `m` unlimited; open files `n` 64000; processes/threads `u` 64000. Restart mongod/mongos after changes. Audit with `cat /proc/<pid>/limits`.
- **6.3 Ensure that server-side scripting is disabled if not needed (Manual, L2):** if mapReduce, group, `$where`, `$accumulator`, and `$function` are not used, disable via `--noscripting` or:
  ```yaml
  security:
    javascriptEnabled: false
  ```
  Default is enabled; also applies to mongos starting in MongoDB 4.4. Disabling blocks all server-side scripts.

## File permissions

- **7.1 Ensure appropriate key file permissions are set (Manual, L1):** locate `keyFile`, `PEMKeyFile`, and `CAFile` in `mongod.conf`, then:
  ```
  chmod 600 /keyfile
  sudo chown mongodb:mongodb /keyfile
  ```
- **7.2 Ensure appropriate database file permissions are set (Manual, L1):** protect the data directory (`storage.dbPath`, e.g. `/var/lib/mongodb`):
  ```
  chmod 770 /var/lib/mongodb
  chown mongodb:mongodb /var/lib/mongodb
  ```
  Audit with `stat -c '%a' /var/lib/mongodb` (Linux) or `icacls "dbpath"` (Windows).

## Related

- [[grc-frameworks/cis-benchmarks/cis-postgresql-16]]
