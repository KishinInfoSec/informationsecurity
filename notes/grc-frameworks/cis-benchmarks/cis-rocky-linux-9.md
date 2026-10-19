---
title: cis-rocky-linux-9
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Rocky Linux 9 Benchmark v2.0.0 checklist: file permissions, services, logging, access control, with levels."
source_pdf: "CIS_Rocky_Linux_9_Benchmark_v2.0.0 .pdf"
---

# CIS Rocky Linux 9 Benchmark v2.0.0 (06-25-2024)

## Overview

- **Product:** Rocky Linux 9 (x86_64); developed and tested against Rocky Linux 9.4, commands assumed run as root under default Bash.
- **Benchmark:** CIS Rocky Linux 9 Benchmark v2.0.0, published 06-25-2024; latest version at http://workbench.cisecurity.org.
- **Recommendations:** 297 total (275 Automated, 22 Manual) across 7 sections.
- **Assessment legend:** every item is **Automated** (fully assessable to pass/fail) or **Manual** (environment-dependent). Condensed selections below keep the benchmark's numbering, wording, and commands.

## Profiles

Four configuration profiles are defined; Level 2 extends Level 1 and is not standalone:

| Profile | Intent |
|---|---|
| Level 1 - Server | Practical and prudent; clear security benefit; does not inhibit utility beyond acceptable means. Intended for servers. |
| Level 2 - Server | Extends L1 - Server: for environments where security is paramount, defense in depth; may inhibit utility or performance. |
| Level 1 - Workstation | Same practical/prudent intent as L1 - Server, intended for workstations. |
| Level 2 - Workstation | Extends L1 - Workstation with the same security-paramount characteristics as L2 - Server. |

Items are tagged per profile variant (Server vs Workstation) where applicability differs — for example usb-storage removal is L1 Server / L2 Workstation, while auditd rules (6.3) are L2 only.

### Section map

| Section | Recommendations |
|---|---|
| 1 Initial Setup | 77 |
| 2 Services | 39 |
| 3 Network | 18 |
| 4 Host Based Firewall | 8 |
| 5 Access Control | 71 |
| 6 Logging and Auditing | 62 |
| 7 System Maintenance | 22 |

## Filesystem and permissions

- **Unused filesystem kernel modules (1.1.1.1–1.1.1.9, L1; squashfs/udf are L2):** cramfs, freevxfs, hfs, hfsplus, jffs2, squashfs, udf, usb-storage must not be available. Remediation pattern (cramfs shown; same per module): create a `.conf` in `/etc/modprobe.d/` containing `install cramfs /bin/false` and `blacklist cramfs`, then `modprobe -r cramfs 2>/dev/null; rmmod cramfs 2>/dev/null`. Audit verifies the module is not loaded, not loadable, and deny listed via `modprobe --showconfig`.
- **Separate partitions with mount options (1.1.2.1–1.1.2.7):** `/tmp` must be a separate partition (L1) with `nodev`, `nosuid`, `noexec`; `/dev/shm` same (L1); `nodev`/`nosuid` (and `noexec` for `/var/tmp`, `/var/log`, `/var/log/audit`) also required on `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit` (separate partitions themselves are L2 for those five). Audit `/tmp` with `findmnt -kn /tmp` (example output `/tmp tmpfs tmpfs rw,nosuid,nodev,noexec`) and `systemctl is-enabled tmp.mount` (not masked/disabled); remediate with `systemctl unmask tmp.mount` plus an `/etc/fstab` entry, for example `tmpfs /tmp tmpfs defaults,rw,nosuid,nodev,noexec,relatime,size=2G 0 0` or `<device> /tmp <fstype> defaults,nodev,nosuid,noexec 0 0`.
- **Cron file permissions (2.4.1.2–2.4.1.7, L1):** `/etc/crontab`, `/etc/cron.hourly`, `/etc/cron.daily`, `/etc/cron.weekly`, `/etc/cron.monthly`, `/etc/cron.d` owned `root:root` with no group/other access — for crontab: `chown root:root /etc/crontab` and `chmod og-rwx /etc/crontab` (target `Access: (600/-rw-------)`). Restrict `crontab`/`at` to authorized users via `/etc/cron.allow` (takes precedence over `/etc/cron.deny`) and `/etc/at.allow` (2.4.1.8, 2.4.2.1, L1).
- **System file permissions (7.1, L1):** `/etc/passwd` mode 644 or more restrictive, `root:root` — `chmod u-x,go-wx /etc/passwd; chown root:root /etc/passwd`. `/etc/shadow` (and `-` backups, `/etc/gshadow`, `/etc/shells`, `/etc/security/opasswd`) mode 0000, `root:root` — `chown root:root /etc/shadow; chmod 0000 /etc/shadow`. Verify with `stat -Lc 'Access: (%#a/%A)  Uid: ( %u/ %U) Gid: ( %g/ %G)' <file>`. World-writable files must not exist, and world-writable directories must carry the sticky bit (7.1.11); no unowned/ungrouped files (7.1.12); review SUID/SGID files (7.1.13, Manual).

## Package management and patching

- **1.2.1.2 gpgcheck globally activated (L1, Automated):** `gpgcheck=1` in the main section of `/etc/dnf/dnf.conf` and in every `/etc/yum.repos.d/*` file (repo entries take precedence; no `gpgcheck=0`/`false`/`no` anywhere). Audit: `grep -Pi -- '^\h*gpgcheck\h*=\h*(1|true|yes)\b' /etc/dnf/dnf.conf`.
- **1.2.1.1/1.2.1.3/1.2.1.4 (L1/L2, Manual):** GPG keys configured, `repo_gpgcheck` activated, repositories per site policy.
- **1.2.2.1 Updates, patches, and additional security software are installed (L1, Manual):** apply updates and security fixes per site policy; the benchmark's Overview stresses monitoring the base OS and applications for vulnerabilities and updating quickly.

## SELinux, bootloader, and process hardening

- **1.3.1.2 SELinux not disabled in bootloader (L1):** `grubby --info=ALL | grep -Po '(selinux|enforcing)=0\b'` must return nothing; remove with `grubby --update-kernel ALL --remove-args "selinux=0 enforcing=0"`.
- **1.3.1.3 Policy configured (L1):** `SELINUXTYPE=targeted` (or `mls`) in `/etc/selinux/config`; confirm with `sestatus | grep Loaded`.
- **1.3.1.5 Mode enforcing (L2):** `setenforce 1` and `SELINUX=enforcing` in `/etc/selinux/config`; audit with `getenforce`. Also: SELinux installed (1.3.1.1), not disabled (1.3.1.4, L1), no unconfined services (1.3.1.6, L2 Manual), mcstrans and SETroubleshoot not installed (1.3.1.7 L1, 1.3.1.8 L1 Server).
- **1.4.1 Bootloader password (L1):** set with `grub2-setpassword` (writes hashed `GRUB2_PASSWORD=grub.pbkdf2.sha512` to `user.cfg`); 1.4.2 restricts access to bootloader config.
- **1.5 Additional process hardening (L1):** `kernel.randomize_va_space=2` (ASLR, 1.5.1), `kernel.yama.ptrace_scope=1` (1.5.2), core dump backtraces and storage disabled (1.5.3, 1.5.4).
- **1.6 System-wide crypto policy (L1):** never `LEGACY` — audit `grep -Pi '^\h*LEGACY\b' /etc/crypto-policies/config`; remediate `update-crypto-policies --set DEFAULT` then `update-crypto-policies`. 1.6.3–1.6.7 further disable SHA-1, short MACs, CBC, chacha20-poly1305, and EtM for SSH.
- **1.7 Warning banners (L1):** properly configured MOTD, local (`/etc/issue`) and remote (`/etc/issue.net`) login banners; restricted access to `/etc/motd`, `/etc/issue`, `/etc/issue.net`. GNOME/GDM hardening is 1.8 (idle screen lock, no removable-media autorun, XDMCP off).

## Services, time synchronization, and network

- **Disable unused server services (2.1, mostly L1):** autofs, avahi, dhcp/dns/dnsmasq servers, samba, ftp, message access, NFS, NIS, print server, rpcbind, rsync, snmp, telnet/tftp servers, web proxy, web server, xinetd (X Window L2 Server). MTAs must run in local-only mode (2.1.21); only approved services may listen on an interface (2.1.22, Manual). Remove ftp/ldap/nis/telnet/tftp clients (2.2).
- **Time synchronization (2.3, L1):** chrony installed (`rpm -q chrony` / `dnf install chrony`), configured, and not run as root (2.3.1–2.3.3). Supports Kerberos and consistent log timestamps for forensics.
- **Network kernel modules (3.2, L2):** dccp, tipc, rds, sctp not available (same modprobe-deny pattern as filesystem modules).
- **Kernel parameters (3.3, L1):** `net.ipv4.ip_forward = 0` and `net.ipv6.conf.all.forwarding = 0` (3.3.1) — persist via `/etc/sysctl.d/`, e.g. `printf '%s\n' "net.ipv4.ip_forward = 0" >> /etc/sysctl.d/60-netipv4_sysctl.conf`; also no packet redirects (3.3.2), ignore bogus/broadcast ICMP (3.3.3–3.3.4), refuse ICMP and secure redirects (3.3.5–3.3.6), reverse path filtering on (3.3.7), no source routing (3.3.8), log suspicious packets (3.3.9), `net.ipv4.tcp_syncookies = 1` (3.3.10), no IPv6 router advertisements (3.3.11). Note: many CSP-hosted systems require IP forwarding — review before disabling.

## Host-based firewall

- **4.1 (L1):** nftables installed; exactly one of firewalld or nftables in use (not both, neither).
- **4.2 FirewallD (L1):** drop unnecessary services/ports (4.2.1, Manual); loopback configured (4.2.2) — `firewall-cmd --permanent --zone=trusted --add-interface=lo; firewall-cmd --reload`, plus rules dropping traffic *from* 127.0.0.1 on non-loopback interfaces (anti-spoofing).
- **4.3 NFTables (L1):** base chains exist (4.3.1); established connections allowed (4.3.2, Manual); default deny — `nft chain inet filter input { policy drop \; }` and same for `forward` (add an SSH-allow rule before setting drop to avoid lockout); loopback rules `nft add rule inet filter input iif lo accept`, `nft add rule inet filter input ip saddr 127.0.0.0/8 counter drop`, and the IPv6 `::1` equivalents (4.3.4).

## SSH and access control

Applies only if sshd is installed; after changes run `systemctl reload-or-restart sshd`. First occurrence of an option wins; `Include` (default `/etc/ssh/sshd_config.d/*.conf`, which includes `/etc/crypto-policies/back-ends/opensshserver.config` via `50-redhat.conf`) and `Match` blocks affect audits — place settings above them.

- **5.1.1 Config file permissions (L1):** `/etc/ssh/sshd_config` and `*.conf` under `sshd_config.d` — mode 0600 or more restrictive, `root:root`. Private host keys 0600 (5.1.2), public host keys 0644 (5.1.3), all `root:root`.
- **5.1.4/5.1.5/5.1.6 Ciphers, KexAlgorithms, MACs (L1):** prefer the system-wide crypto-policy back-end over manual `Ciphers`/`MACs` lines. Weak ciphers not permitted: `3des-cbc`, `aes128/192/256-cbc`; if `chacha20-poly1305@openssh.com` appears, review CVE-2023-48795 patch status. Weak MACs include hmac-md5, hmac-md5-96, hmac-sha1-96, umac-64@openssh.com and their etm variants. FIPS-compliant strong ciphers: `aes256-gcm@openssh.com`, `aes128-gcm@openssh.com`, `aes256-ctr`, `aes192-ctr`, `aes128-ctr`. Audit with `sshd -T` grep scripts.
- **5.1.7 Access configured (L1):** at least one of `AllowUsers <userlist>`, `AllowGroups <grouplist>`, `DenyUsers`, `DenyGroups` per site policy (allow lists easier to manage than deny lists).
- **5.1.9 Idle timeout (L1):** `ClientAliveInterval 15` and `ClientAliveCountMax 3` (example 45-second timeout; `ClientAliveCountMax` must be > 0 to drop idle connections).
- **5.1.16 MaxAuthTries 4 or less (L1; default 6).** Also: `LoginGraceTime` (5.1.14), `LogLevel INFO` (5.1.15), `MaxStartups` (5.1.17), `MaxSessions` (5.1.18).
- **5.1.19–5.1.22 (L1):** `PermitEmptyPasswords no`, `PermitRootLogin no` (admins authenticate as themselves then escalate — clear audit trail), `PermitUserEnvironment no`, `UsePAM yes`. Disable forwarding (5.1.10), GSSAPIAuthentication (5.1.11), HostbasedAuthentication (5.1.12); `IgnoreRhosts yes` (5.1.13). Banner per 1.7 (5.1.8).

## sudo, PAM, and user accounts

- **sudo (5.2, L1 unless noted):** installed (5.2.1); `Defaults use_pty` (5.2.2) so sudo cannot fork persistent background processes; dedicated log file `Defaults logfile="/var/log/sudo.log"` (5.2.3) — always edit via `visudo`/`visudo -f`; password required for escalation (5.2.4, L2); no global `!timestamp_timeout` disabling re-auth (5.2.5); timeout per policy (5.2.6). Restrict `su` to an empty wheel group: `groupadd sugroup` and `auth required pam_wheel.so use_uid group=sugroup` in `/etc/pam.d/su` (5.2.7) — reinforces sudo for better logging.
- **PAM (5.3, L1):** current pam, authselect, libpwquality; authselect profile includes pam_faillock, pam_pwquality, pam_pwhistory, pam_unix (5.3.2). Lockout `deny = 5` (or ≤ 5) in `/etc/security/faillock.conf` (5.3.3.1.1; default 3; unlock with `faillock --user <USERNAME> --reset`), unlock time (5.3.3.1.2), lockout includes root (5.3.3.1.3, L2). Password quality: length, minlen/dictionary, consecutive and sequential characters, enforce for root (5.3.3.2.x); history via pam_pwhistory `remember` (5.3.3.3.x); pam_unix without `nullok` or `remember`, strong hash, `use_authtok` (5.3.3.4.x).
- **Shadow suite (5.4.1, L1 unless noted):** `PASS_MAX_DAYS 365` (or less) in `/etc/login.defs` plus `chage --maxdays 365 <user>` for every account with a password (5.4.1.1); minimum days (5.4.1.2, L2 Manual); `PASS_WARN_AGE 7` / `chage --warndays` (5.4.1.3); `ENCRYPT_METHOD SHA512` or `YESCRYPT` (5.4.1.4); inactive lock `useradd -D -f 45` / `chage --inactive 45`, no more than 45 days (5.4.1.5); all last-change dates in the past (5.4.1.6).
- **Root and system accounts (5.4.2, L1):** root is the only UID 0 / GID 0 account and only member of group root (5.4.2.1–5.4.2.3); root access controlled via `/etc/securetty` (5.4.2.4); root PATH integrity — no `.`/empty (`::`)/trailing `:` entries, only root-owned directories no more permissive than 0755 (5.4.2.5); root umask 027 or stricter (5.4.2.6); system accounts get a nologin shell (5.4.2.7) and are locked (5.4.2.8).
- **User defaults (5.4.3):** nologin not in `/etc/shells` (L2); `TMOUT` shell timeout 900 or less (L1); default umask 027 or stricter (L1).
- **Local user/group hygiene (7.2, L1):** shadowed passwords in `/etc/passwd`, non-empty shadow fields, groups consistent, no duplicate UIDs/GIDs/usernames/group names, interactive home directories `0700` `root:root`-owned or user-owned, dot-file access configured.

## Logging and auditing

- **journald (6.2.1–6.2.2, L1):** journald enabled/active; only one logging system in use. If journald is the sole logger: `ForwardToSyslog=no` in `/etc/systemd/journald.conf` `[Journal]` section; `Storage=persistent` and `Compress=yes` per policy; log file access and rotation configured (Manual).
- **rsyslog (6.2.3, L1):** installed, enabled, journald forwarding to it, creation mode 0640 or stricter; logging rules, remote log host (6.2.3.6, Manual), no receiving from remote clients (6.2.3.7), logrotate (Manual). All logfiles access configured (6.2.4.1).
- **auditd service (6.3.1, L2):** audit packages installed; `audit=1` boot parameter; `audit_backlog_limit` sufficient — recommended 8192+, e.g. `grubby --update-kernel ALL --args 'audit_backlog_limit=8192'`; auditd enabled/active.
- **Data retention (6.3.2, L2):** `max_log_file = <MB>` in `/etc/audit/auditd.conf` per site policy (default 8); `max_log_file_action = keep_logs` so audit logs are never auto-deleted (default ROTATE); system disabled when logs full (`-f 2`/`disk_full_action`) and warned when low on space.
- **Audit rules (6.3.3, L2, `/etc/audit/rules.d/*.rules` then `augenrules --load`; reboot may be required when `-e 2` is set):** sudoers scope `-w /etc/sudoers -p wa -k scope` and `-w /etc/sudoers.d -p wa -k scope`; actions as another user `-a always,exit -F arch=b64 -C euid!=uid -F auid!=unset -S execve -k user_emulation` (plus b32 variant, 6.3.3.2); date/time, network environment, privileged commands, user/group info (`-w /etc/group -p wa -k identity`, `-w /etc/passwd -p wa -k identity`, `-w /etc/shadow -p wa -k identity`, plus gshadow/opasswd/nsswitch.conf/pam.conf/pam.d), DAC permission changes, mounts, session/logon info, file deletions, MAC changes, `chcon`/`setfacl`/`chacl`/`usermod` usage. Unsuccessful file access (6.3.3.7): `-a always,exit -F arch=b64 -S creat,open,openat,truncate,ftruncate -F exit=-EACCES -F auid>=1000 -F auid!=unset -k access` (plus `-F exit=-EPERM` and b32 variants). Kernel modules (6.3.3.19): `-a always,exit -F arch=b64 -S init_module,finit_module,delete_module,create_module,query_module -F auid>=1000 -F auid!=unset -k kernel_modules` and `-F path=/usr/bin/kmod -F perm=x -F auid>=1000 -F auid!=unset -k kernel_modules`. Immutability (6.3.3.20): last line of `/etc/audit/rules.d/99-finalize.rules` is `-e 2`. Running and on-disk configuration must match (6.3.3.21, Manual).
- **Audit file access (6.3.4, L2):** `/var/log/audit` directory mode 0700 or stricter; audit log files 0600 or stricter owned `root:root` (per `auditd.conf` user/group); audit configuration files 0600 `root:root`; audit tools (`auditctl`, `ausearch`, `aureport`, `augenrules`) 0755 or stricter `root:root`.

## AIDE (integrity checking)

- **6.1.1 Installed (L1):** `rpm -q aide` / `dnf install aide`, configure per site policy, initialize: `aide --init` then `mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz`.
- **6.1.2 Regularly checked (L1):** cron job running `/usr/sbin/aide --check` (or `$AIDEARGS`) in `/etc/cron.*`/`/etc/crontab`/`/var/spool/cron/`, or `aidecheck.service` and `aidecheck.timer` enabled and the timer running.
- **6.1.3 Audit tools protected (L1):** cryptographic mechanisms (hashes/signatures) protect integrity of audit tools and logs against tampering.

## Source

CIS Rocky Linux 9 Benchmark v2.0.0 (06-25-2024), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[grc-frameworks/cis-benchmarks/cis-rhel-9]]
