---
title: cis-ubuntu-22-04
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Ubuntu Linux 22.04 LTS Benchmark v3.0.0 checklist: filesystem, services, patching, SSH, auditing, with levels."
source_pdf: CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v3.0.0.pdf
---

# CIS Ubuntu Linux 22.04 LTS Benchmark v3.0.0 (10-30-2025)

## Overview

- **Product:** Ubuntu Linux 22.04 LTS on x86_64 platforms; developed and tested against Ubuntu 22.04.5 LTS. Commands assume the root user and the default Bash shell; sudo or another shell may produce unexpected results.
- **Benchmark version:** v3.0.0 (10-30-2025). Latest version notice in the PDF: https://workbench.cisecurity.org
- **Assessment status:** every recommendation is Automated (can be fully validated pass/fail) or Manual (all or some steps cannot be automated). All Manual items must still be addressed for audits — some tooling skips them, which is wrong.
- **Exceptions:** recommendations are guidance, not requirements; exceptions must be reviewed cross-functionally, documented for audit, and paired with a mitigation/elimination plan or an explicit risk acceptance.

### Profile applicability

Four profiles; each Level 2 profile *extends* its Level 1 counterpart and is not standalone:

| Profile | Intent |
|---|---|
| Level 1 - Server / Workstation | Practical and prudent; clear security benefit; does not inhibit utility beyond acceptable means |
| Level 2 - Server / Workstation | For environments where security is paramount; defense in depth; may negatively inhibit utility or performance |

Server vs workstation differences appear as profile splits on individual items: for example 1.1.1.9 usb-storage is L1 Server / L2 Workstation (USB sticks are a bigger workstation risk), while 1.7.1 GDM removed and 2.1.20 X window server services are L2 Server only, and 3.3.1.1 net.ipv4.ip_forward is L1 Workstation / L2 Server.

### Section outline

| Section | Contents |
|---|---|
| 1 Initial Setup | filesystem modules/partitions, package management, AppArmor, bootloader, process hardening, banners, GDM |
| 2 Services | server/client services, time synchronization, cron/at |
| 3 Network | devices, network kernel modules, sysctl parameters |
| 4 Host Based Firewall | ufw only (no nftables/iptables sections in this version) |
| 5 Access Control | SSH, sudo, PAM, password and account policy |
| 6 Logging and Auditing | journald, rsyslog, auditd, AIDE |
| 7 System Maintenance | system file permissions, local user/group settings |

## Filesystem and permissions

- **Kernel filesystem modules (1.1.1.x):** remove unused filesystem types (cramfs, freevxfs, hfs, hfsplus, jffs2, squashfs, udf — L1; overlay and udf-style L2 items differ). Remediation pattern for cramfs (1.1.1.1, L1): unload with `modprobe -r cramfs` / `rmmod cramfs`, then drop a file in `/etc/modprobe.d/` (example `60-cramfs.conf`) containing both `install cramfs /bin/false` and `blacklist cramfs`. Audit with `lsmod | grep 'cramfs'` (nothing) and `modprobe --showconfig | grep -P -- '\b(install|blacklist)\h+cramfs\b'`. 1.1.1.6 overlay (L2) cites CVE-2023-32629, CVE-2023-2640, CVE-2023-0386. 1.1.1.10 unused filesystems and 1.1.1.11 firewire-core are also covered.
- **Partitions (1.1.2.x):** `/tmp` and `/dev/shm` must be tmpfs or a separate partition (L1) with `nodev`, `nosuid`, `noexec`; separate partitions (L1) or separate filesystems with nodev/nosuid (L2 or L1) for `/home`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit`. Separate `/tmp` blocks executable code and hard-link attacks on setuid programs.
- **MAC (1.3.1.x):** AppArmor packages installed, AppArmor enabled in the bootloader (remove `apparmor=0` from `GRUB_CMDLINE_LINUX=` in `/etc/default/grub`, then `update-grub` and reboot), all profiles not disabled (L1), all profiles enforcing (L2).
- **Process hardening (1.5.x):** `kernel.randomize_va_space = 2` (ASLR); `ptrace_scope`; `suid_dumpable`; core file size; prelink not installed; Automatic Error Reporting configured.
- **Banners (1.6.x):** configure `/etc/motd`, `/etc/issue`, `/etc/issue.net` and restrict access to each.

## Services and special files

- **Server services (2.1.x):** autofs, avahi, dhcp/dns/dnsmasq, ftp, ldap, IMAP, NFS, NIS, print, rpcbind, rsync, samba, snmp, tftp, web proxy, web server, xinetd not in use (2.1.18 web server, L1: remove packages, or stop and mask service/socket if needed for a dependency); MTA local-only (2.1.21); only approved services listening (2.1.22, Manual). X window server services are L2 Server.
- **Client services (2.2.x):** nis, rsh, talk, telnet, ldap, ftp clients not installed.
- **Time sync (2.3.x):** exactly one synchronization daemon; either systemd-timesyncd or chrony configured with an authorized timeserver, enabled and running (chrony as user `_chrony`).
- **Job schedulers (2.4.x):** cron enabled and active; access configured on `/etc/crontab`, `/etc/cron.hourly`, `/etc/cron.daily`, `/etc/cron.weekly`, `/etc/cron.monthly`, `/etc/cron.yearly`, `/etc/cron.d`, crontab, and at.

## Patching

- **1.2.1.1 / 1.2.1.2 (Manual):** GPG keys configured; package manager repositories configured.
- **1.2.2.1 (Manual):** updates, patches, and additional security software installed. The benchmark stresses testing Build Kits or remediation scripts in a lab, deploying to a small production subset first, then iterating.

## Network and firewall

- **Modules (3.2.x):** dccp, tipc, rds, sctp kernel modules not available (L2).
- **Sysctl (3.3.x):** IPv4 and IPv6 parameters set via files under `/etc/sysctl.d/` (precedence: `/etc/sysctl.d/*.conf` then `/run/sysctl.d/*.conf` then `/etc/sysctl.conf` via systemd-sysctl). Examples: `net.ipv4.ip_forward = 0` (3.3.1.1; not applicable on routers; many CSP hosts need forwarding — review before disabling), send_redirects, icmp_ignore_bogus_error_responses, icmp_echo_ignore_broadcasts, accept_redirects, secure_redirects, rp_filter, accept_source_route, log_martians, `net.ipv4.tcp_syncookies`, plus the IPv6 counterparts (3.3.2.x).
- **Firewall (4.1.x):** ufw is the only utility in this version. 4.1.1 ufw installed; 4.1.2 service configured (`systemctl is-enabled/is-active ufw.service`, `ufw status` shows `Status: active` — before `ufw enable`, add an SSH rule such as `ufw allow proto tcp from any to any port 22`, restricted to required hosts per site policy; `ufw --force enable` avoids the SSH prompt); 4.1.3 incoming default deny/reject (`ufw status verbose`); 4.1.4 outgoing default; 4.1.5 routed default.

## SSH and access control

From `/etc/ssh/sshd_config` (5.1.x); audit with `sshd -T` (add `-C user=<name>` when Match blocks exist — first occurrence of an option takes precedence except Match):

- 5.1.1–5.1.3: access to `sshd_config`, private host keys, public host keys configured.
- 5.1.7 ClientAliveInterval and ClientAliveCountMax > 0 (example 15 / 3 ≈ 45 s timeout; ClientAliveCountMax must be > 0 to drop unresponsive connections).
- 5.1.6/5.1.12/5.1.15: Ciphers, KexAlgorithms, MACs configured; 5.1.13 LoginGraceTime; 5.1.16 MaxAuthTries ≤ 4; 5.1.17 MaxSessions; 5.1.18 MaxStartups.
- 5.1.19 PermitEmptyPasswords disabled; 5.1.20 PermitRootLogin no (`sshd -T | grep permitrootlogin` — default is prohibit-password; forces admins to authenticate as themselves then escalate, aiding non-repudiation); 5.1.21 PermitUserEnvironment disabled; 5.1.22 UsePAM enabled.
- 5.1.8 DisableForwarding enabled, 5.1.9 GSSAPIAuthentication disabled.

## sudo, accounts, and password policy

- **sudo (5.2.x):** sudo installed; `Defaults use_pty` in `/etc/sudoers` or `/etc/sudoers.d/` (edit only with visudo — misconfiguration can break sudo; remove any `!use_pty`); sudo log file exists; 5.2.4 users must provide password for escalation; 5.2.5 re-auth not disabled globally; 5.2.6 timestamp_timeout; 5.2.7 su access restricted.
- **PAM (5.3.x):** latest pam, libpam-modules, libpam-pwquality; pam_unix, pam_faillock, pam_pwquality, pam_pwhistory enabled via pam-auth-update. pam_faillock: `deny = 5` or less in `/etc/security/faillock.conf` (default deny = 3); `unlock_time = 900` or more (or 0 = never; max 604800; tally dir usually cleared on boot); lockout may include root (L2). pam_pwquality: complexity, dictionary check, enforced quality (incl. root). pam_pwhistory: `remember` history, enforced for root, with use_authtok. pam_unix: no `nullok`, no `remember`, strong hashing algorithm, use_authtok.
- **Password/account lifecycle (5.4.1.x):** `PASS_MAX_DAYS 365` or less in `/etc/login.defs` (default 99999; verify all shadowed users with the awk audit from the benchmark; apply via `chage --maxdays 365 <user>`); 5.4.1.2 minimum password days (Manual); PASS_WARN_DAYS; strong hashing algorithm; inactive password lock; all last-change dates in the past.
- **Root/system accounts (5.4.2.x):** root is the only UID 0 account, only GID 0 account, root group only GID 0 group; root account access controlled; root path integrity; root umask; system accounts have no valid login shell and are locked.
- **User environment (5.4.3.x):** nologin not in `/etc/shells`; default shell timeout; default user umask.

## Logging and auditing

- **journald (6.1.1.x):** service active; log file access and rotation configured (Manual); ForwardToSyslog disabled; Storage configured; Compress configured; systemd-journal-remote/upload handling (6.1.1.2.x).
- **rsyslog (6.1.2.x):** installed, enabled and active; journald sending to it; log file creation mode configured; logging configured (Manual); remote log host (Manual); not receiving from remote clients; logrotate configured (Manual). 6.1.3.1 access to all logfiles configured.
- **auditd (6.2.x, Level 2 both profiles):** packages installed; service enabled and active; early auditing; `audit_backlog_limit`; `max_log_file = <MB>` in `/etc/audit/auditd.conf` (default 8); `max_log_file_action = keep_logs` (logs never auto-deleted); disk_full_action / disk_error_action halt-or-single-user behavior. Rules live in `/etc/audit/rules.d/*.rules` and are merged/loaded with `augenrules --load` (check `auditctl -s` for enabled=2 → reboot needed; immutable config with `-e 2` silently blocks reloads). Key rules: 6.2.3.1 sudoers scope — `-w /etc/sudoers -p wa -k scope` and `-w /etc/sudoers.d -p wa -k scope`; plus actions as another user, sudo log file, time changes, network environment, privileged commands, unsuccessful file access, user/group info, DAC modifications, mounts, sessions, logins, deletions, MAC changes, chcon/setfacl/chacl/usermod, kernel module changes, immutable audit config (6.2.3.20). 6.2.4.x: audit log/config file modes and ownership (root, mode 0600-class), audit tools ownership.
- **Integrity (6.3.x):** AIDE installed (`apt install aide aide-common`, then `aideinit` and `mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db`); filesystem integrity regularly checked; 6.3.3 cryptographic protection of audit tools.

## System maintenance

- **File permissions (7.1.x):** `/etc/passwd` mode 644 root:root (`chmod u-x,go-wx /etc/passwd; chown root:root /etc/passwd`); same pattern for `/etc/passwd-`, `/etc/group`, `/etc/group-`; `/etc/shadow` and `/etc/shadow-` mode 640 root:shadow or root:root (`chmod u-x,g-wx,o-rwx /etc/shadow`); `/etc/gshadow`, `/etc/gshadow-`, `/etc/shells`, `/etc/security/opasswd`; world-writable files/directories secured; no unowned/ungrouped files; SUID/SGID files reviewed (Manual).
- **Local user/group settings (7.2.x):** shadowed passwords in `/etc/passwd`; no empty `/etc/shadow` password fields; groups in passwd exist in group; shadow group empty; no duplicate UIDs/GIDs/usernames/group names; interactive user home directories and dot files configured.

## CIS Controls mapping

The benchmark maps every recommendation to CIS Controls by version, Safeguard, and Implementation Group in appendices for CIS Controls v7 (IG 1/2/3 plus unmapped) and v8 (IG 1/2/3 plus unmapped). The benchmark as a whole addresses v7 "5.1 - Establish Secure Configurations" and v8 "4.1 - Establish and Maintain a Secure Configuration Process", so individual recommendations are not mapped to those safeguards. Each recommendation body also carries its own CIS Controls block (e.g. 5.1.20 PermitRootLogin → v8 5.4 Restrict Administrator Privileges to Dedicated Administrator Accounts; 6.2.2.2 keep_logs → v8 8.3 Ensure Adequate Audit Log Storage). An Appendix: Summary Table provides a correct/yes/no checklist of the full recommendation set.

## Source

CIS Ubuntu Linux 22.04 LTS Benchmark v3.0.0 (10-30-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
