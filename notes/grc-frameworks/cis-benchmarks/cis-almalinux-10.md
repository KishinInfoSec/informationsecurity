---
title: cis-almalinux-10
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS AlmaLinux OS 10 Benchmark v1.0.0 checklist: file permissions, services, logging, access control, with levels."
source_pdf: CIS_AlmaLinux_OS_10_Benchmark_v1.0.0.pdf
---

# CIS AlmaLinux OS 10 Benchmark v1.0.0 (09-30-2025)

## Overview

- **Product:** AlmaLinux OS 10, Benchmark v1.0.0 dated 09-30-2025.
- **Profiles:** Level 1 - Server, Level 2 - Server, Level 1 - Workstation, Level 2 - Workstation.
  - Level 1 items are practical and prudent, provide a clear security benefit, and do not inhibit utility beyond acceptable means.
  - Level 2 extends Level 1 (not standalone): items are for environments where security is paramount, act as defense in depth, and may negatively inhibit utility or performance.
- **Recommendations:** 328 total (307 Automated, 21 Manual). Assessment status: *Automated* = technical control can be fully assessed to a pass/fail state; *Manual* = requires manual steps and expected state varies by environment. Both must be addressed for audits.
- **Assessment tooling:** CIS-CAT Pro Assessor and CIS Benchmarks Certified 3rd party tooling.
- **CIS Controls:** the Benchmark as a whole addresses (v7) "5.1 - Establish Secure Configurations" and (v8) "4.1 - Establish and Maintain a Secure Configuration Process"; individual recommendations are not mapped to these safeguards.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Initial Setup | 79 |
| 2 Services | 39 |
| 3 Network | 35 |
| 4 Host Based Firewall | 7 |
| 5 Access Control | 68 |
| 6 Logging and Auditing | 78 |
| 7 System Maintenance | 22 |

## Condensed checklist

Representative high-signal controls; commands and values are from the benchmark. See the full PDF for every recommendation's audit and remediation steps.

### 1 Initial Setup

Advised for all systems, but best done at install time.

- **Filesystem kernel modules (1.1.1.x, L1):** cramfs, freevxfs, hfs, hfsplus, jffs2, overlay, squashfs, udf, firewire-core not available; usb-storage L1 Server / L2 Workstation; unused modules Manual. Audit with `modprobe --showconfig | grep -P -- '\b(install|blacklist)\h+cramfs\b'`; remediate via `/etc/modprobe.d/60-cramfs.conf`: `install cramfs /bin/false` and `blacklist cramfs`.
- **Partitions (1.1.2.x, L1):** `/tmp`, `/dev/shm` tmpfs or separate partitions with `nodev`, `nosuid`, `noexec`; separate partitions for `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit` (partition existence L2) with `nodev`/`nosuid` (+ `noexec` on `/var/tmp`, `/var/log`, `/var/log/audit`).
- **Package management (1.2.x, L1):** GPG keys configured (Manual); `gpgcheck=1` in `/etc/dnf/dnf.conf` `[main]`; `repo_gpgcheck=1` (Manual); repositories configured (Manual); `install_weak_deps=0` (L2); updates, patches, and additional security software installed (Manual).
- **SELinux (1.3.1.x):** installed; not disabled in bootloader; policy configured; mode not disabled (L1); mode enforcing (L2): `SELINUX=enforcing` in `/etc/selinux/config`, `setenforce 1` at runtime; no unconfined services (L2, Manual); mcstrans and SETroubleshoot not installed.
- **Bootloader (1.4.x, L1):** bootloader password set (`grub2-mkpasswd-pbkdf2`, `GRUB2_PASSWORD=grub.pbkdf2.sha512` in `user.cfg`); access to bootloader config configured.
- **Process hardening (1.5.x, L1):** core file size configured; `fs.protected_hardlinks = 1`; `fs.protected_symlinks`; `fs.suid_dumpable`; `kernel.dmesg_restrict`; `kernel.kptr_restrict` = 1 or 2; `kernel.yama.ptrace_scope`; `kernel.randomize_va_space = 2`; systemd-coredump `ProcessSizeMax` and `Storage`.
  - Persist with e.g. `printf '%s\n' "" "fs.protected_hardlinks = 1" >> /etc/sysctl.d/60-fs_sysctl.conf`.
- **Crypto policy (1.6.x, L1):** not set to legacy (`update-crypto-policies --set DEFAULT`); sha1 hash/signature support disabled; MACs configured; CBC disabled for ssh.
- **Banners (1.7.x, L1):** `/etc/motd`, `/etc/issue`, `/etc/issue.net` configured (e.g. `echo "Authorized users only. All activity may be monitored and reported." > /etc/issue`) and access to each configured.
- **GDM (1.8.x):** login banner; `disable-user-list`; screen lock; automount configured; `autorun-never`; Xwayland configured.

### 2 Services

- **Server services (2.1.x):** autofs, avahi, cockpit (L2), dhcp/dns/dnsmasq/ftp/message access/nfs/print/rpcbind/rsync/samba/snmp/telnet/tftp/web proxy/web server not in use; GDM removed (L2 Server) and X window server not in use; mail transfer agents in local-only mode.
  - Only approved services listening on a network interface (Manual).
- **Client services (2.2.x):** ftp, ldap (L2), telnet, tftp clients not installed.
- **Time sync (2.3.x, L1):** time synchronization in use; `chrony` configured with `server`/`pool` lines per site policy; `chrony` not run as the root user.
- **Job schedulers (2.4.x, L1):** cron daemon enabled and active; access to `/etc/crontab`, `/etc/cron.{hourly,daily,weekly,monthly,yearly}`, `/etc/cron.d`, `crontab` and `at` restricted — e.g. `chown root:root /etc/crontab; chmod og-rwx /etc/crontab` (`Access: (600/-rw-------) Uid/Gid 0/root`).

### 3 Network

- **Devices (3.1.x):** IPv6 status identified (Manual); wireless interfaces not available; bluetooth not in use (L1 Server / L2 Workstation).
- **Kernel modules (3.2.x, L1):** atm, can, dccp, tipc, rds, sctp not available (`modprobe --showconfig | grep -P -- '\b(install|blacklist)\h+dccp\b'`).
- **IPv4 sysctls (3.3.1.x):** `net.ipv4.ip_forward = 0` (L1 Workstation / L2 Server — routers excepted); `net.ipv4.conf.{all,default}.forwarding = 0`; `send_redirects = 0`; `icmp_ignore_bogus_error_responses`; `icmp_echo_ignore_broadcasts`; `accept_redirects = 0` and `secure_redirects = 0`; `rp_filter = 1`; `accept_source_route = 0`; `log_martians`; `tcp_syncookies = 1`.
  - Values are set in files under `/etc/sysctl.d/` (e.g. `60-ipv4_sysctl.conf`).
- **IPv6 sysctls (3.3.2.x):** `forwarding = 0`, `accept_redirects = 0`, `accept_source_route = 0`, `accept_ra` configured.

### 4 Host Based Firewall

firewalld (NFTables backend) is the only firewall guidance in this benchmark; only one firewall method should be configured on a system.

- **4.1.1** firewalld installed (L1); **4.1.2** backend configured; **4.1.3** `firewalld.service` configured; **4.1.4** active zone target configured — example `securezone` zone with `target="DROP"` allowing `ssh`, saved to `/etc/firewalld/zones/securezone.xml`, then `firewall-cmd --reload` and `firewall-cmd --permanent --zone=securezone --change-interface={NAME OF NETWORK INTERFACE}`.
- **4.1.5–4.1.6** loopback traffic and loopback source address traffic (Manual); **4.1.7** only approved services and ports (Manual).

### 5 Access Control

- **SSH (5.1.x, L1):** access to `/etc/ssh/sshd_config` and to private/public host key files (private keys `0640` or more restrictive, group `ssh_keys`); `sshd` access configured (AllowUsers/AllowGroups); Banner; audit effective config with `sshd -T`.
  - Crypto: Ciphers free of weak algorithms (approved: `aes256-gcm@openssh.com`, `aes128-gcm@openssh.com`, `aes256-ctr`, `aes128-ctr`); `KexAlgorithms` restricted (e.g. `curve25519-sha256`, `diffie-hellman-group14-sha256` and newer groups); `MACs` restricted (e.g. `hmac-sha2-256-etm@openssh.com`, `hmac-sha2-512-etm@openssh.com`).
  - Session/connection: `ClientAliveInterval 15` / `ClientAliveCountMax 3`; `DisableForwarding` enabled; `LoginGraceTime 60`; `LogLevel INFO`; `MaxAuthTries 4`; `MaxStartups 10:30:60`; `MaxSessions 10`.
  - Authentication: `GSSAPIAuthentication no`; `HostbasedAuthentication no`; `IgnoreRhosts yes`; `PermitEmptyPasswords no`; `PermitRootLogin no`; `PermitUserEnvironment no`; `UsePAM yes`.
- **Privilege escalation (5.2.x):** sudo installed; sudo commands use pty; sudo log file exists (`Defaults logfile="/var/log/sudo.log"`); users must provide password for escalation (L2); re-authentication not disabled globally; `timestamp_timeout` 15 minutes or less (`Defaults env_reset, timestamp_timeout=15`); access to `su` restricted.
- **PAM (5.3.x, L1):** authselect profile includes `pam_faillock`, `pam_pwquality`, `pam_pwhistory`, `pam_unix`.
  - faillock: `deny = 5`, `unlock_time = 900`, root included via `even_deny_root` (L2).
  - pwquality: `minlen = 14` (e.g. `/etc/security/pwquality.conf.d/50-pwlength.conf`), changed characters, consecutive/sequential characters, dictionary check, enforced for root.
  - pwhistory: `remember = 5` with `use_authtok`; pam_unix without `nullok`/`remember`, strong hashing (`sha512` or `yescrypt`) and `use_authtok`.
- **Accounts and environment (5.4.x):** `PASS_MAX_DAYS 365` or less, `PASS_MIN_DAYS 1` or more, `PASS_WARN_AGE 7` or more in `/etc/login.defs`; strong password hashing algorithm; inactive password lock; all users' last password change in the past.
  - root and system accounts: root the only UID 0 / GID 0 account; root account access controlled; root path integrity; root umask `0027`; system accounts without a valid login shell and locked; `nologin` not in `/etc/shells` (L2).
  - default user environment: shell timeout (`TMOUT`, no more than 900 seconds, readonly and exported); default user umask `0027` (e.g. `umask 027` in `/etc/profile.d/60-default_umask.sh`).

### 6 Logging and Auditing

- **Integrity checking (6.1.x, L1):** AIDE installed (`dnf install aide`); filesystem integrity regularly checked — root crontab entry `0 5 * * * /usr/sbin/aide --check` or `aidecheck.service`/`aidecheck.timer`; cryptographic mechanisms (sha256/sha512 hashes) protect audit tools.
- **journald (6.2.1–6.2.2):** service active (`systemctl --now enable systemd-journald.service`); log file access and rotation configured (Manual); only one logging system in use; systemd-journal-remote handling; `ForwardToSyslog` disabled when rsyslog is the transport; `Compress` and `Storage` configured.
- **rsyslog (6.2.3):** installed, enabled and active; journald configured to send logs to rsyslog; log file creation mode; logging facilities per site policy (Manual); optional remote log host (Manual); not configured to receive from remote clients; logrotate configured (Manual).
- **Logfiles (6.2.4, L1):** access to all logfiles configured — mode `0640` or more restrictive under `/var/log`.
- **auditd (6.3.x, L2):** packages installed; early-boot auditing (`audit=1`); `audit_backlog_limit=8192` (e.g. `grubby --update-kernel ALL --args 'audit_backlog_limit=8192'`); service enabled and active; `max_log_file`, logs not auto-deleted, `space_left_action` = email/exec/single/halt, system halted or warned when logs full.
  - Rules (drop into `/etc/audit/rules.d/`): modification of `/etc/sudoers` (`-a always,exit -F path=/etc/sudoers -F perm=wa` plus `-F dir=/etc/sudoers.d`); actions as another user (`-a always,exit -F arch=b64 -C euid!=uid -F auid!=unset -S execve`); sudo log file changes; date/time, hostname, `/etc/issue`, `/etc/hosts`, network config changes.
  - Also: privileged commands, unsuccessful file access, `/etc/{group,passwd,shadow,gshadow}` and PAM changes; DAC permission changes (chmod/chown/xattr families); mounts, sessions, logins, unlink/rename; MAC changes and `chcon`/`setfacl`/`chacl`/`usermod` usage; kernel module load/unload (`init_module`, `finit_module`, `delete_module`, `query_module`); configuration loaded regardless of errors and immutable (`-e 2`).
  - File access: audit log directory mode `0750` or more restrictive, log files `0640` or more restrictive, owners `root`, config files and tools similarly restricted.

### 7 System Maintenance

- **File permissions (7.1.x, L1):** `/etc/passwd` mode `644` root/root; `/etc/passwd-`, `/etc/group`, `/etc/group-`, `/etc/shells`, `/etc/security/opasswd` similarly restricted; `/etc/shadow`, `/etc/shadow-`, `/etc/gshadow`, `/etc/gshadow-` mode `000` or more restrictive (`chmod 0000 /etc/shadow`).
  - World-writable files and directories secured — no output expected from `find / -xdev \( -type f -o -type d \) -perm -0002`; no files without owner/group; SUID and SGID files reviewed (Manual) via `find "$l_mount" -xdev -type f \( -perm -2000 -o -perm -4000 \)`.
- **User and group settings (7.2.x, L1):** shadowed passwords in `/etc/passwd`; no empty `/etc/shadow` password fields; groups in `/etc/passwd` exist in `/etc/group`; no duplicate UIDs/GIDs/user names/group names; interactive user home directories configured; dot file access configured.

## Source

CIS AlmaLinux OS 10 Benchmark v1.0.0 (09-30-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[grc-frameworks/cis-benchmarks/cis-almalinux-9]]
