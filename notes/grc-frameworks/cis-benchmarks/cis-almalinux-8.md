---
title: cis-almalinux-8
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS AlmaLinux OS 8 Benchmark v4.0.0 checklist: file permissions, services, logging, access control, with levels."
source_pdf: CIS_AlmaLinux_OS_8_Benchmark_v4.0.0.pdf
---

# CIS AlmaLinux OS 8 Benchmark v4.0.0 (08-28-2025)

## Overview

- **Benchmark:** CIS AlmaLinux OS 8 Benchmark, v4.0.0, cover date 08-28-2025.
- **Structure:** 7 recommendation sections, 305 recommendations total — 282 Automated and 23 Manual.
- **Assessment status:** *Automated* means the technical control can be assessed and validated to a pass/fail state automatically, with the information needed to automate it supplied in the recommendation. *Manual* means assessment cannot be fully automated and depends on the environment. Both statuses are equally important.
- **Section outline:** 1 Initial Setup (81), 2 Services (42), 3 Network (35), 4 Host Based Firewall (7), 5 Access Control (72), 6 Logging and Auditing (54), 7 System Maintenance (14).

### Profile applicability

Four profiles are defined; each recommendation lists the profiles it belongs to.

| Profile | Intent |
|---|---|
| Level 1 - Server | Practical and prudent, provides a clear security benefit, does not inhibit utility beyond acceptable means. Intended for servers. |
| Level 2 - Server | Extends "Level 1 - Server". Items are for environments where security is paramount, act as defense in depth, and may negatively inhibit utility or performance. |
| Level 1 - Workstation | Same three Level 1 intentions, intended for workstations. |
| Level 2 - Workstation | Extends "Level 1 - Workstation" with the same Level 2 characteristics. |

Level 2 is never a standalone profile — it always contains the matching Level 1. Several recommendations are profile-specific rather than universal:

- Server-only: 2.1.11 print server services are not in use (Level 1 - Server).
- Split across variants: 3.3.1.1 `net.ipv4.ip_forward` is Level 1 - Workstation / Level 2 - Server (not applicable on routers); 5.1.10 `DisableForwarding` and 5.1.11 `GSSAPIAuthentication` are Level 1 - Workstation / Level 2 - Server.
- L2-only hardening: 1.1.1.6 `overlay` kernel module, 1.2.1.5 weak dependencies, 1.3.1.5 SELinux enforcing, 5.2.4 password for escalation, 5.4.1.2 minimum password days, the whole 6.3.1–6.3.4 auditd block.

## Filesystem and permissions

**Kernel modules (1.1.1, Level 1 unless noted).** Uncommon filesystem types are removed to cut local attack surface: cramfs, freevxfs, hfs, hfsplus, jffs2, firewire-core (all L1), overlay, squashfs, udf (all L2), usb-storage (Level 1 - Server / Level 2 - Workstation), plus a Manual sweep of the remaining unused filesystems. Current inventory: `ls /usr/lib/modules/**/kernel/fs | sort -u`.

**Partitions and mount options (1.1.2).** `/tmp` must be tmpfs or a separate partition with `nodev`, `nosuid`, `noexec`; `/dev/shm` must be tmpfs with the same three options; `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit` need `nodev` and `nosuid` (`/var/tmp`, `/var/log`, `/var/log/audit` also `noexec`). Separate-partition items for `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit` are Level 2.

```
# findmnt -kn /tmp
# systemctl is-enabled tmp.mount
# systemctl unmask tmp.mount
tmpfs /tmp tmpfs     defaults,rw,nosuid,nodev,noexec,relatime,size=2G  0 0
```

**Account file permissions (7.1, L1).** `/etc/passwd`, `/etc/passwd-`, `/etc/group`, `/etc/group-`, `/etc/shells` → mode 644 or more restrictive, `root:root`; `/etc/shadow`, `/etc/shadow-`, `/etc/gshadow`, `/etc/gshadow-` → mode 0000, `root:root`; `/etc/security/opasswd` → mode 600 or more restrictive.

```
# chmod u-x,go-wx /etc/passwd
# chown root:root /etc/passwd
# chown root:root /etc/shadow
# chmod 0000 /etc/shadow
```

7.1.11 removes world-writable files and sets the sticky bit on world-writable directories (exempting `/run`, `/tmp`, `/var/tmp`); 7.1.12 finds files with no owner or group; 7.1.13 SUID/SGID review is Manual.

**Cron and at (2.4).** `/etc/crontab` mode 600 `root:root` (`chmod og-rwx /etc/crontab`), `/etc/cron.{hourly,daily,weekly,monthly,yearly,d}` mode 700 `root:root`, and `crontab`/`at` restricted to authorized users.

## Patching and package management (1.2)

- 1.2.1.1 GPG keys configured per repo (Manual); keys live in `/etc/pki/rpm-gpg/` and are listed with `grep -r gpgkey /etc/yum.repos.d/* /etc/dnf/dnf.conf`.
- 1.2.1.2 `gpgcheck=1` in the `[main]` section of `/etc/dnf/dnf.conf` (Automated); 1.2.1.3 `repo_gpgcheck=1` globally (Manual); 1.2.1.5 weak dependencies restricted (L2).
- 1.2.2.1 updates, patches and additional security software are installed (Manual) — the patch management process itself is left to the organization; CIS Controls 7.3/7.4 call for automated OS and application patching monthly or more often.

## Services (2)

Server services that are not required should have their package removed; if a dependency needs the package, stop and mask instead:

```
# systemctl stop <service_name>.socket <service_name>.service
# systemctl mask <service_name>.socket <service_name>.service
```

Covered by 2.1.1–2.1.24: autofs, avahi, cockpit, dhcp/dns/dnsmasq, ftp, imap/pop, NFS, nis, print, rpcbind, rsync, samba, snmp, telnet, tftp, web proxy, web server, xinetd, GDM, X window server, MTA local-only mode, and a Manual check that only approved services listen on an interface. 2.2 removes ftp/ldap/nis/telnet/tftp clients. 2.3 requires `chrony` (`rpm -q chrony`, `dnf install chrony`) with a `server` or `pool` directive in `/etc/chrony.conf`, not run as root.

## Network and firewall (3, 4)

IPv6 status is identified (3.1.1), wireless interfaces are unavailable (3.1.2, Level 1 - Server) and bluetooth services are not in use (3.1.3, Level 1 - Server / Level 2 - Workstation). Network kernel modules atm, can, dccp, rds, sctp and tipc are made unavailable (3.2, Level 1 - Server / Level 1 - Workstation). IPv4/IPv6 sysctls are set both at runtime and in a file under `/etc/sysctl.d/`, then loaded with `sysctl --system`:

| Parameter | Value |
|---|---|
| `net.ipv4.ip_forward` | 0 (L1 Workstation / L2 Server; routers exempt) |
| `net.ipv4.conf.all.send_redirects` / `default.send_redirects` | 0 |
| `net.ipv4.icmp_echo_ignore_broadcasts` | 1 |
| `net.ipv4.conf.all.accept_redirects` / `default.accept_redirects` | 0 |
| `net.ipv4.conf.all.secure_redirects` / `default.secure_redirects` | 0 |
| `net.ipv4.conf.all.rp_filter` / `default.rp_filter` | 1 |
| `net.ipv4.conf.all.accept_source_route` / `default.accept_source_route` | 0 |
| `net.ipv4.conf.all.log_martians` / `default.log_martians` | 1 |
| `net.ipv4.tcp_syncookies` | 1 |

Example remediation files named in the benchmark: `/etc/sysctl.d/60-ipv4_sysctl.conf`, `/etc/sysctl.d/60-kernel_sysctl.conf`, `/etc/sysctl.d/60-fs_sysctl.conf`.

**firewalld (4.1, all L1).** Install it (`rpm -q firewalld`, `dnf install firewalld`), set `FirewallBackend=nftables` in `/etc/firewalld/firewalld.conf`, then `systemctl unmask firewalld.service` and `systemctl --now enable firewalld.service`. The active zone target for non-loopback, non-virtual interfaces must not be `ACCEPT` (use `DROP`/`default`); the loopback interface sits in a zone whose target is `ACCEPT` (4.1.5: `firewall-cmd --permanent --zone=trusted --add-interface=lo`, then `--reload`); traffic with a loopback source address to non-loopback destinations is dropped (4.1.6); and services/ports are opened per site policy (4.1.7, Manual). The benchmark ships a sample `securezone` zone XML saved to `/etc/firewalld/zones/securezone.xml`, then `firewall-cmd --reload` and `firewall-cmd --permanent --zone=securezone --change-interface={NAME OF NETWORK INTERFACE}`. Only one firewall configuration method may be used.

## SELinux, bootloader and process hardening (1.3–1.7)

- **SELinux (1.3.1):** installed (`rpm -q libselinux`), not disabled in the bootloader, policy set to `targeted`, mode not disabled (L1) and mode `enforcing` (L2: `SELINUX=enforcing` in `/etc/selinux/config`, verified with `getenforce`, applied with `setenforce 1`, or `touch /.autorelabel` plus `reboot` when previously disabled), no unconfined services (L2, Manual), mcstrans and SETroubleshoot removed.
- **Bootloader (1.4):** password set with `# grub2-setpassword`, producing `GRUB2_PASSWORD=grub.pbkdf2.sha512` in `user.cfg`; access to bootloader config restricted.
- **Process hardening (1.5):** `fs.protected_hardlinks = 1`, `fs.protected_symlinks = 1`, `fs.suid_dumpable = 0`, `kernel.dmesg_restrict = 1`, `kernel.kptr_restrict = 1` or `2`, `kernel.yama.ptrace_scope = 1`, `kernel.randomize_va_space = 2`, plus core file size and `systemd-coredump` ProcessSizeMax/Storage.
- **Crypto policy (1.6):** must not be `LEGACY` — `# update-crypto-policies --set DEFAULT` then `# update-crypto-policies`; sha1 hash/signature support and CBC/`chacha20-poly1305`/EtM for ssh disabled; FIPS via `fips-mode-setup --enable` if site policy requires it.
- **Banners (1.7):** `/etc/motd`, `/etc/issue`, `/etc/issue.net` carry site-policy text with no OS-release escapes — e.g. `echo "Authorized users only. All activity may be monitored and reported." > /etc/issue` — and are locked down with `chmod u-x,go-wx /etc/issue` (and the same for `motd`/`issue.net`).

## SSH and access control (5.1)

`/etc/ssh/sshd_config` and `/etc/ssh/sshd_config.d/*.conf` are mode 0600 or more restrictive, `root:root`; SSH private host keys are `root` with group `ssh_keys` (mode 0640) or group `root` (mode 0600); public host keys are mode 644 or more restrictive. Effective configuration is audited with `sshd -T $OPTIONS $CRYPTO_POLICY` (source `/etc/crypto-policies/back-ends/opensshserver.config` and `/etc/sysconfig/sshd`), including any `Match` block via `-C user=<name>`.

| Setting | Required value |
|---|---|
| `PermitRootLogin` | `no` (above any Include/Match entries; default `prohibit-password`) |
| `PermitEmptyPasswords` | `no` |
| `Banner` | `/etc/issue.net` |
| `MaxAuthTries` | 4 or less |
| `MaxSessions`, `MaxStartups`, `LoginGraceTime` | per site policy |
| `ClientAliveInterval` / `ClientAliveCountMax` | both greater than zero (benchmark example: 15 / 3) |
| `UsePAM` | `yes` |
| `HostbasedAuthentication`, `GSSAPIAuthentication` | disabled |
| `IgnoreRhosts` | enabled |
| `DisableForwarding` | enabled (L1 Workstation / L2 Server) |
| access control | `AllowUsers <userlist>`, `AllowGroups <grouplist>`, `DenyUsers`, `DenyGroups` (AND-ed together) |

`sshd crypto_policy` must not be set (5.1.1) — the system-wide crypto policy from section 1.6 applies instead; `Ciphers`, `KexAlgorithms` and `MACs` come from the crypto policy back end.

## sudo, PAM and accounts (5.2–5.4)

- **sudo:** installed; `Defaults use_pty` set and `!use_pty` removed; a dedicated log file via `Defaults logfile="/var/log/sudo.log"` in `/etc/sudoers` or a `/etc/sudoers.d/` file edited with `visudo -f <PATH TO FILE>`; no `NOPASSWD` tags (`grep -r "^[^#].*NOPASSWD" /etc/sudoers*`, L2); global re-authentication not disabled; `timestamp_timeout` configured; access to `su` restricted.
- **PAM/authselect:** active profile includes `pam_faillock`, `pam_pwquality`, `pam_pwhistory`, `pam_unix`. In `/etc/security/faillock.conf`: `deny = 5` (5 or less, default 3) and `unlock_time = 900` (0/never or 900 seconds and up, default 600); L2 adds `even_deny_root` with `root_unlock_time` 60 or more. `pam_unix` must not include `nullok`; pwquality length/complexity/dictionary and pwhistory `remember` follow site policy.
- **Password aging (5.4.1):** `PASS_MAX_DAYS 365` or less in `/etc/login.defs` with `chage --maxdays 365 <user>` applied to every account with a password (default 99999); `PASS_MIN_DAYS` (L2), `PASS_WARN_DAYS`, `ENCRYPT_METHOD SHA512` or `YESCRYPT`, `INACTIVE` lock, and all last-change dates in the past.
- **Accounts (5.4.2/5.4.3):** root is the only UID 0/GID 0 account; root path and umask controlled; system accounts below `UID_MIN` get `usermod -s $(command -v nologin) <user>` and are locked; default user umask `027` (e.g. `umask 027` appended to `/etc/profile.d/60-default_umask.sh`); shell timeout configured.

## Logging and auditd (6.2, 6.3)

Pick one client-side logging method and follow only that branch:

- **journald path:** 6.2.1.1.4 sets `ForwardToSyslog=no` and skips the rsyslog recommendations; `Storage=persistent` and `Compress=yes` in the `[Journal]` section of `/etc/systemd/journald.conf` or a drop-in `/etc/systemd/journald.conf.d/60-journald.conf`; log file access and rotation set per policy; systemd-journal-remote/upload handled separately.
- **rsyslog path:** 6.2.2.x — `dnf install rsyslog`, then `systemctl unmask rsyslog.service`, `systemctl enable rsyslog.service`, `systemctl start rsyslog.service`; `ForwardToSyslog=yes` in journald; log file creation mode and remote forwarding per site policy (6.2.2.6 expects `*.* @@loghost.example.com`, where `@@` is TCP and a single `@` is UDP); 6.2.2.7 forbids receiving logs from remote clients (`imtcp` module/input must not be loaded); logrotate configured (Manual).
- **Logfile access (6.2.3.1):** everything under `/var/log` is mode 0640 or more restrictive and owned by `root`/`syslog` with group `root`/`adm` (special cases: `wtmp`/`btmp`/`lastlog` 0640 root:utmp, `*.journal` root:systemd-journal).

**auditd (6.3, all L2):**

- Boot parameters: `audit=1` and `audit_backlog_limit=8192` added with `# grubby --update-kernel ALL --args 'audit=1'` (and the same for `audit_backlog_limit`), or by editing `GRUB_CMDLINE_LINUX` in `/etc/default/grub`.
- Service: `systemctl unmask auditd`, `systemctl enable auditd`, `systemctl start auditd`.
- Retention in `/etc/audit/auditd.conf`: `max_log_file = <MB>` (default 8), `max_log_file_action = keep_logs` (no automatic deletion), `space_left_action = email`, `admin_space_left_action = single` (single/halt).
- Rules live in `/etc/audit/rules.d/*.rules` and are merged with `# augenrules --load`, e.g. `-w /etc/sudoers -p wa -k scope` and `-w /etc/sudoers.d -p wa -k scope` (50-scope.rules). Other rule families cover date/time, network environment, privileged commands, failed file access, user/group changes, DAC permission changes, mounts, logins, deletions, MAC changes, `chcon`/`setfacl`/`chacl`/`usermod`, and kernel module load/unload.
- Immutability: `-e 2` appended to `/etc/audit/rules.d/99-finalize.rules` — a reboot is then required to change the active configuration.
- File access: audit log directory mode 0750 or more restrictive, audit log files 0640 or more restrictive, audit configuration files 0640, audit tools 0755, all owned by `root`.

## AIDE (6.1)

- 6.1.1 install and initialize: `# dnf install aide`, `# aide --init`, `# mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz`.
- 6.1.2 schedule regular checks — cron `0 5 * * * /usr/sbin/aide --check`, or `aidecheck.service` + `aidecheck.timer` (`OnCalendar=*-*-* 05:00:00`) with `chown root:root /etc/systemd/system/aidecheck.*` and `chmod 0644 /etc/systemd/system/aidecheck.*`.
- 6.1.3 the AIDE configuration must cover the audit tools `auditctl`, `auditd`, `ausearch`, `aureport`, `autrace`, `augenrules` with the options `p, i, n, u, g, s, b, acl, xattrs and sha512`.

## Source

CIS AlmaLinux OS 8 Benchmark v4.0.0 (08-28-2025), Center for Internet Security.

## Related

- [[grc-frameworks/cis-benchmarks/cis-almalinux-9]]
