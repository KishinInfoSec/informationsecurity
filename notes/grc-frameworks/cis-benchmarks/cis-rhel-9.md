---
title: cis-rhel-9
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Red Hat Enterprise Linux 9 Benchmark v2.0.0 checklist: file permissions, services, logging, access control, with levels."
source_pdf: CIS_Red_Hat_Enterprise_Linux_9_Benchmark_v2.0.0.pdf
---

# CIS Red Hat Enterprise Linux 9 Benchmark v2.0.0 (06-24-2024)

Prescriptive configuration guidance for Red Hat Enterprise Linux 9 systems on x86_64 platforms; developed and tested against RHEL 9.4. Operations are assumed to run as the root user under the default Bash for the distribution. Recommendations are marked (Automated) or (Manual) and carry profile applicability; the benchmark maps to CIS Controls v7/v8 and MITRE ATT&CK.

## Profiles

| Profile | Intent |
|---|---|
| Level 1 - Server | Practical and prudent; clear security benefit; does not inhibit utility beyond acceptable means. Baseline for servers. |
| Level 2 - Server | Extends Level 1 - Server: for environments where security is paramount, defense in depth; may negatively inhibit utility or performance. |
| Level 1 - Workstation | Same practical/prudent criteria as Level 1 - Server, intended for workstations. |
| Level 2 - Workstation | Extends Level 1 - Workstation; defense-in-depth items that may reduce utility/performance. |

Level 2 items are hardening beyond the baseline — e.g. SELinux enforcing (1.3.1.5) and auditd sudoers watch rules (6.3.3.1) are Level 2, while most partition, package, SSH, and permission controls are Level 1. Server vs Workstation splits mainly affect desktop/GDM and removable-media items.

## Filesystem and partitions (1.1)

- Disable unused filesystem kernel modules: cramfs, freevxfs, hfs, hfsplus, jffs2, squashfs, udf, usb-storage (1.1.1.x). Audit each via `modprobe --showconfig` for `install <mod> /bin/(true|false)` and `blacklist <mod>` entries under `/etc/modprobe.d/`, and confirm the module is not loaded in `lsmod`. Remediate by creating a `.conf` in `/etc/modprobe.d/` with `install cramfs /bin/false` plus a blacklist line.
- Separate partitions with mount hardening (1.1.2.x) for `/tmp`, `/dev/shm`, `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit`:
  - `/tmp`: separate partition (or tmpfs) so `noexec`, `nodev`, `nosuid` can be applied — `noexec` makes /tmp useless for installing executable code and blocks hard-link attacks on setuid programs. Verify with `findmnt -kn /tmp`.
  - `/var/log` and `/var/log/audit`: separate partitions so log growth cannot fill `/`; each gets `nodev`, `nosuid`, `noexec`.
  - `/home`, `/var`: at least `nodev` and `nosuid`.

## Package management and patching (1.2)

- `gpgcheck=1` globally in `/etc/dnf/dnf.conf` (1.2.1.2): `grep -Pi -- '^\h*gpgcheck\h*=\h*(1|true|yes)\b' /etc/dnf/dnf.conf`; no `gpgcheck=0`/`false`/`no` entries in `/etc/yum.repos.d/` (repo settings take precedence over global). Remediate with `sed -i 's/^gpgcheck\s*=\s*.*/gpgcheck=1/' /etc/dnf/dnf.conf`.
- GPG keys configured (1.2.1.1, Manual), `repo_gpgcheck` activated (1.2.1.3, Manual), repositories reviewed (1.2.1.4).
- Updates, patches, and additional security software installed (1.2.2.1, Manual) — mapped to CIS Controls v8 7.3 Automated OS Patch Management.

## SELinux and MAC (1.3)

- SELinux installed, not disabled in bootloader, policy configured (targeted), mode not disabled (1.3.1.1–1.3.1.4).
- SELinux mode enforcing (1.3.1.5, Level 2): `getenforce` → `Enforcing`; `grep -i SELINUX=enforcing /etc/selinux/config`; remediate `setenforce 1` and set `SELINUX=enforcing`. Permissive only logs denials; disabled skips labeling persistent objects entirely.
- No unconfined services (1.3.1.6, Manual); remove `mcstrans` and `SETroubleshoot` (1.3.1.7–1.3.1.8).

## Bootloader and process hardening (1.4–1.6)

- Bootloader password set (1.4.1); access to bootloader config restricted (1.4.2).
- ASLR enabled (1.5.1); `ptrace_scope` restricted (1.5.2); core dump backtraces and storage disabled (1.5.3–1.5.4).
- System-wide crypto policy not `LEGACY` (1.6.1): `grep -Pi '^\h*LEGACY\b' /etc/crypto-policies/config` returns nothing; remediate `update-crypto-policies --set DEFAULT`. LEGACY allows TLS 1.0/1.1, DSA, 3DES, RC4 and weak RSA/DH minimums. Further items disable SHA-1, MACs < 128 bits, CBC for SSH, and chacha20-poly1305/EtM for SSH (1.6.3–1.6.7).

## Warning banners (1.7) and GDM (1.8)

- MOTD configured properly (1.7.1); local and remote login warning banners via `/etc/issue` and `/etc/issue.net` (1.7.2–1.7.3); access to `/etc/motd`, `/etc/issue`, `/etc/issue.net` configured (1.7.4–1.7.6).
- GNOME Display Manager: remove if unused (1.8.1); login banner, `disable-user-list`, idle screen locks that cannot be overridden, disabled automatic mounting of removable media, `autorun-never`, XDMCP disabled (1.8.2–1.8.10) — workstation-relevant.

## Services (2)

- Server services not in use (2.1.x): autofs, avahi, dhcp/dns servers, dnsmasq, samba, ftp, imap/pop, NFS, NIS, print server, rpcbind, rsync, SNMP, telnet, tftp, web proxy, web server, xinetd, X window server. MTAs in local-only mode (2.1.21); only approved services listening (2.1.22, Manual).
- Client services removed (2.2.x): ftp, ldap, nis, telnet, tftp clients.
- Time synchronization (2.3.x): chrony in use, configured with `server`/`pool` lines in `/etc/chrony.conf` or `/etc/chrony.d/` (`grep -Prs -- '^\h*(server|pool)\h+[^#\n\r]+' /etc/chrony.conf /etc/chrony.d/`), and not run as root (`/etc/sysconfig/chronyd`).
- Cron enabled and active (2.4.1.1); permissions on `/etc/crontab`, `/etc/cron.{hourly,daily,weekly,monthly}`, `/etc/cron.d` (2.4.1.2–2.4.1.7); crontab and at restricted to authorized users (2.4.1.8, 2.4.2.1).

## Network (3)

- Identify IPv6 status (3.1.1, Manual); wireless interfaces disabled (3.1.2); bluetooth not in use (3.1.3).
- Network kernel modules disabled: dccp, tipc, rds, sctp (3.2.x), same modprobe.d blacklist pattern as filesystems.
- Kernel parameters (3.3.x), audited via `sysctl` plus durable config via `systemd-sysctl --cat-config`:
  - `net.ipv4.ip_forward=0` and `net.ipv6.conf.all.forwarding=0` (3.3.1) — system will never act as a router; review before applying on CSP-hosted systems that require forwarding.
  - Packet redirect sending disabled (3.3.2); bogus ICMP ignored (3.3.3); broadcast ICMP ignored (3.3.4); ICMP redirects not accepted (3.3.5–3.3.6); reverse path filtering enabled (3.3.7); source-routed packets not accepted (3.3.8); suspicious packets logged (3.3.9); TCP SYN cookies enabled (3.3.10); IPv6 router advertisements not accepted (3.3.11).

## Host-based firewall (4)

- nftables installed (4.1.1); exactly one firewall utility in use (4.1.2): either firewalld enabled+active with nftables disabled/masked, or the reverse — never both. Only configure the recommendations for the utility in use.
- Firewalld: drop unnecessary services and ports (4.2.1, Manual); loopback traffic configured (4.2.2).
- NFTables: base chains exist (4.3.1); established connections configured (4.3.2, Manual); default deny policy (4.3.3) — `nft list ruleset | grep 'hook input' | grep -v 'policy drop'` returns nothing; remediate `nft chain inet filter input { policy drop \; }` (same for forward). Allow SSH before setting drop if managing remotely. Loopback traffic configured (4.3.4).

## SSH server (5.1)

- `/etc/ssh/sshd_config` and `/etc/ssh/sshd_config.d/*.conf`: mode 0600 or stricter, root:root (5.1.1). Private host keys 0600, public host keys 0644 or stricter (5.1.2–5.1.3).
- Ciphers/KexAlgorithms/MACs configured (5.1.4–5.1.6): audit `sshd -T` for weak ciphers (3des-cbc, aes*-cbc, arcfour, chacha20-poly1305@openssh.com pending CVE-2023-48795 review). Prefer configuring via system-wide crypto policy (`Include /etc/crypto-policies/back-ends/opensshserver.config`) over sshd_config; FIPS 140-compliant strong ciphers: aes256-gcm@openssh.com, aes128-gcm@openssh.com, aes256-ctr, aes192-ctr, aes128-ctr.
- Access and session controls: `sshd access` (5.1.7), Banner (5.1.8), ClientAliveInterval/ClientAliveCountMax (5.1.9), DisableForwarding enabled (5.1.10), GSSAPIAuthentication disabled (5.1.11), HostbasedAuthentication disabled (5.1.12), IgnoreRhosts enabled (5.1.13), LoginGraceTime (5.1.14), LogLevel INFO (5.1.15), MaxAuthTries ≤ 4 (5.1.16), MaxStartups (5.1.17), MaxSessions (5.1.18), PermitEmptyPasswords disabled (5.1.19).
- `PermitRootLogin no` (5.1.20): `sshd -T | grep permitrootlogin` → `permitrootlogin no`; also check Match blocks via `sshd -T -C user=sshuser`. Disallowing root SSH forces admins to authenticate as themselves then escalate, giving a clear audit trail. Default is prohibit-password.
- PermitUserEnvironment disabled (5.1.21); UsePAM enabled (5.1.22).

## Sudo and privilege escalation (5.2)

- sudo installed (5.2.1); sudo commands use pty (5.2.2).
- Dedicated sudo log file (5.2.3): `Defaults logfile="/var/log/sudo.log"` in `/etc/sudoers` or `/etc/sudoers.d/` — edit only with `visudo -f <FILE>`; manage rotation via logrotate.
- Password required for escalation (5.2.4); re-authentication not disabled globally (5.2.5); authentication timeout configured (5.2.6); `su` access restricted (5.2.7).

## PAM and password policy (5.3–5.4)

- Latest pam, authselect, libpwquality (5.3.1.x); authselect profile includes pam modules (5.3.2.1); modules enabled: pam_faillock, pam_pwquality, pam_pwhistory, pam_unix (5.3.2.2–5.3.2.5).
- pam_faillock (5.3.3.1.x): `deny = 5` (or less) in `/etc/security/faillock.conf` (default is 3); unlock with `faillock --user <USERNAME> --reset`.
- pam_pwquality (5.3.3.2.x): `minlen = 14` or more in `/etc/security/pwquality.conf.d/*.conf` (module args override `pwquality.conf`, which overrides `.d/` files); also changed characters, complexity, same-consecutive-characters, sequential characters, dictionary check, enforce for root.
- pam_pwhistory: history remember configured and enforced for root, includes `use_authtok` (5.3.3.3.x). pam_unix: no `nullok`, no `remember`, strong hashing algorithm, `use_authtok` (5.3.3.4.x).
- Shadow suite (5.4.1.x): `PASS_MAX_DAYS 365` or less in `/etc/login.defs`, verified per-user in `/etc/shadow`; minimum days, warning days, strong hashing algorithm, inactive password lock, last password change in the past.
- Root/system accounts (5.4.2.x): root only UID 0 and GID 0 account; root access controlled; root path integrity; root umask; system accounts no valid login shell and locked.
- Default user environment (5.4.3.x): nologin not listed in `/etc/shells`; shell timeout; default umask.

## Logging and auditing (6)

- AIDE installed (6.1.1): `rpm -q aide`; `dnf install aide`; initialize with `aide --init` then `mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz`. Filesystem integrity regularly checked (6.1.2); audit tools integrity protected by cryptographic mechanisms (6.1.3).
- journald enabled and active (6.2.1.1); log file access and rotation (6.2.1.2–6.2.1.3, Manual); only one logging system in use (6.2.1.4); ForwardToSyslog disabled when not needed (6.2.2.2); Compress and Storage configured (6.2.2.3–6.2.2.4); journal-remote/upload controls (6.2.2.1.x).
- rsyslog (6.2.3.x): installed, enabled/active, journald sends to it, creation mode, logging config and remote log host (Manual), not receiving from remote clients, logrotate.
- Logfile access configured (6.2.4.1).
- auditd (6.3.1–6.3.2): packages installed; processes started prior to auditd logged (`kernel.audit_backlog_limit` sufficient); service enabled/active; log storage size configured; logs not automatically deleted; system disabled when audit logs full (space_running_left); system warns when logs low on space.
- audit rules (6.3.3.x) in `/etc/audit/rules.d/*.rules`, merged with `augenrules --load` (reboot may be required if `-e 2`): sudoers scope (`-w /etc/sudoers -p wa -k scope` and `-w /etc/sudoers.d -p wa -k scope`, Level 2), actions as another user, sudo log file modifications, date/time changes, network environment changes, privileged commands, unsuccessful file access attempts, user/group information changes, DAC permission modifications, filesystem mounts, session initiation, login/logout, file deletion, MAC changes, chcon/setfacl/chacl/usermod usage, kernel module load/unload; audit configuration immutable (6.3.3.20); running and on-disk configuration the same (6.3.3.21, Manual).
- auditd file access (6.3.4.x): log directory mode 0700; log files 0600 owned root:root; configuration files 0600 root:root; audit tools 0700 root:root.

## System maintenance (7)

- Critical file permissions (7.1.x), verified with e.g. `stat -Lc 'Access: (%#a/%A) Uid: ( %u/ %U) Gid: ( %g/ %G)' /etc/passwd`:

| File | Mode | Owner |
|---|---|---|
| /etc/passwd, /etc/passwd- | 0644 or stricter | root:root |
| /etc/group, /etc/group- | 0644 or stricter | root:root |
| /etc/shadow, /etc/shadow- | 0640 or stricter | root:root (shadow) |
| /etc/gshadow, /etc/gshadow- | 0640 or stricter | root:root (shadow) |
| /etc/shells | 0644 or stricter | root:root |
| /etc/security/opasswd | 0600 or stricter | root:root |

- World-writable files secured and world-writable directories have sticky bit (7.1.11); no files without owner/group (7.1.12); SUID/SGID files reviewed (7.1.13, Manual).
- Local user/group settings (7.2.x): shadowed passwords in `/etc/passwd`, non-empty `/etc/shadow` fields, groups exist, no duplicate UIDs/GIDs/names, interactive home directories configured, dot files access configured.

## Related

- [[grc-frameworks/cis-benchmarks/cis-almalinux-9]] — same Benchmark family applied to AlmaLinux 9 (RHEL rebuild); controls and section numbering align closely with this note.
