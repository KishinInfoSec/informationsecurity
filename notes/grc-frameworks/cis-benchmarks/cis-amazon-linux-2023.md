---
title: cis-amazon-linux-2023
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Amazon Linux 2023 Benchmark v1.0.0 checklist: filesystem, services, patching, SSH, auditing, with levels."
source_pdf: CIS_Amazon_Linux_2023_Benchmark_v1.0.0.pdf
---

# CIS Amazon Linux 2023 Benchmark v1.0.0 (06-26-2023)

Prescriptive guidance for establishing a secure configuration posture for Amazon Linux 2023 running on x86_64 platforms. Operations are assumed to be performed as the root user under the default Bash for the distribution; sudo or another shell may produce unexpected results. Recommendations are marked (Automated) or (Manual) and mapped to CIS Controls v7/v8 (the benchmark as a whole covers v7 5.1 / v8 4.1 Establish Secure Configurations) and individual NIST SP 800-53 Rev. 5 controls, with MITRE ATT&CK technique mappings.

## Profiles

| Profile | Intent |
|---|---|
| Level 1 - Server | Practical and prudent; clear security benefit; does not inhibit the utility of the technology beyond acceptable means. Intended for servers. |
| Level 2 - Server | Extends Level 1 - Server: for environments where security is paramount, defense in depth; may negatively inhibit utility or performance. Intended for servers. |

This benchmark defines only Server profiles — no Workstation profiles. Level 2 items are hardening beyond baseline — e.g. squashfs mounting disabled (1.1.1.1), SELinux mode enforcing (1.6.1.5), nftables default deny (3.4.2.7), auditd enabled and audit_backlog_limit (5.2.1.3–5.2.1.4) — while most partition, package, SSH, banner, and permission controls are Level 1.

## Filesystem configuration (1.1)

- Disable unused filesystem kernel modules (1.1.1.x, Level 2 for squashfs, Level 1 for the rest): squashfs, udf, cramfs, freevxfs, jffs2, hfs, hfsplus. Audit with the benchmark's bash script per module: `modprobe -n -v <mod>` must show `install <mod> /bin/(true|false)`, `modprobe --showconfig` must show `blacklist <mod>`, and `lsmod` must not list it; search locations include `/etc/modprobe.d/*.conf`. Remediate by creating e.g. `install jffs2 /bin/false` plus `blacklist jffs2` in `/etc/modprobe.d/` and unloading the module. A module pre-compiled into the kernel is an acceptable passing state.
- Separate partitions with mount hardening (1.1.2.x–1.1.8.x) for `/tmp`, `/var`, `/var/tmp`, `/var/log`, `/var/log/audit`, `/home`, `/dev/shm`, each with `nodev`, `nosuid`, and (per intended use) `noexec`:
  - `/tmp`: separate partition or tmpfs so `noexec` makes it useless for installing executable code and blocks hard-link attacks on setuid programs. Audit `findmnt -nk /tmp` and `systemctl is-enabled tmp.mount` (must not be masked/disabled); remediate `systemctl unmask tmp.mount` and an `/etc/fstab` entry, e.g. `tmpfs /tmp tmpfs defaults,rw,nosuid,nodev,noexec,relatime,size=2G 0 0`.
  - `/var/log` and `/var/log/audit`: separate partitions so log growth cannot fill `/`; each gets `nodev`, `nosuid`, `noexec`.
  - `/home`, `/var`, `/var/tmp`: at least `nodev` and `nosuid`; `/var/tmp` also `noexec`.
- usb-storage disabled (1.1.9).

## Software and patch management (1.2)

- GPG keys configured (1.2.1, Manual); `gpgcheck=1` globally in the `[main]` section of `/etc/dnf/dnf.conf` (1.2.2): `grep ^gpgcheck /etc/dnf/dnf.conf`; remediate `sed -i 's/^gpgcheck\s*=\s*.*/gpgcheck=1/' /etc/dnf/dnf.conf`. Configuration in `/etc/yum.repos.d/` takes precedence — no `gpgcheck` set to 0 or invalid values there: `grep -Prs -- '^\h*gpgcheck\h*=\h*(0|[2-9]|[1-9][0-9]+|[a-zA-Z_]+)\b' /etc/yum.repos.d/`.
- Package manager repositories configured (1.2.3, Manual): `dnf repolist` — on AL2023 this returns the `amazonlinux` (Amazon Linux 2023 repository) and `kernel-livepatch` repos; inspect `/etc/yum.repos.d/*.repo` per site policy. `repo_gpgcheck` globally activated (1.2.4, Manual).
- Updates, patches, and additional security software installed (1.8, Manual): `dnf check-update` (a newer Amazon Linux release may be flagged), remediate with `dnf upgrade --releasever=2023.0.XXXXXXX`, then `dnf needs-restarting -r` to check whether a reboot is required. Site policy may mandate testing before production.

## Filesystem integrity checking (1.3)

- AIDE installed (1.3.1): `rpm -q aide`; `dnf install aide`; initialize with `aide --init` then `mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz`.
- Filesystem integrity regularly checked (1.3.2): cron entry matching `aide --check` (e.g. `0 5 * * * /usr/sbin/aide --check` in root's crontab) or `aidecheck.service`/`aidecheck.timer` enabled and the timer running.
- Audit tools integrity protected by cryptographic mechanisms (1.3.3).

## Secure boot and process hardening (1.4–1.5)

- Bootloader config permissions (1.4.1): UEFI files under `/boot/efi/EFI/*` mode 0700 or stricter (via `/etc/fstab` `fmask=0077,uid=0,gid=0` on the vfat ESP mount); BIOS files under `/boot/grub2/*` mode 0600 or stricter, root:root (e.g. `chown root:root /boot/grub2/grub.cfg && chmod u-x,go-rwx /boot/grub2/grub.cfg`).
- ASLR enabled (1.5.1): `kernel.randomize_va_space=2`, audited via `sysctl` plus durable config via `systemd-sysctl --cat-config`.
- ptrace_scope restricted (1.5.2): `kernel.yama.ptrace_scope=1` — limits PTRACE_ATTACH by a compromised process to others under the same user; root retains ptrace.
- Core dump storage disabled (1.5.3) and core dump backtraces disabled (1.5.4).

## Mandatory access control — SELinux (1.6)

- SELinux installed (1.6.1.1) and not disabled in bootloader configuration (1.6.1.2).
- Policy configured (1.6.1.3): `grep -E '^\s*SELINUXTYPE=(targeted|mls)\b' /etc/selinux/config`; `sestatus | grep Loaded`.
- Mode not disabled (1.6.1.4): `getenforce` returns Enforcing or Permissive; `grep -Ei '^\s*SELINUX=(enforcing|permissive)' /etc/selinux/config`. Disabled skips labeling persistent objects, making future enablement difficult.
- Mode enforcing (1.6.1.5, Level 2): `getenforce` → `Enforcing`; remediate `setenforce 1` and `SELINUX=enforcing`. Permissive only logs denials.
- No unconfined services (1.6.1.6, Manual); remove `SETroubleshoot` (1.6.1.7) and `mcstrans` (1.6.1.8).

## Warning banners (1.7)

- MOTD configured properly (1.7.1): `cat /etc/motd` per site policy; no `\m`, `\r`, `\s`, `\v` or OS-name references (they leak platform info to attackers): `grep -E -i "(\\\v|\\\r|\\\m|\\\s|$(grep '^ID=' /etc/os-release | cut -d= -f2 | sed -e 's/"//g'))" /etc/motd`. Or remove `/etc/motd` if unused.
- Local and remote login warning banners via `/etc/issue` and `/etc/issue.net` (1.7.2–1.7.3), same escape-sequence scrubbing; permissions on `/etc/motd`, `/etc/issue`, `/etc/issue.net` configured (1.7.4–1.7.6).

## System-wide crypto policy (1.9)

- Not LEGACY (1.9): `grep -E -i '^\s*LEGACY\s*(\s+#.*)?$' /etc/crypto-policies/config` returns nothing; remediate `update-crypto-policies --set DEFAULT` then `update-crypto-policies`. LEGACY allows TLS 1.0/1.1, DSA, 3DES, RC4, and RSA/DH parameters above 1023 bits — vulnerable per RFC 7457. Default value is DEFAULT. To switch to FIPS: `fips-mode-setup --enable`.

## Services (2)

- Time synchronization (2.1.x): time sync in use (2.1.1); chrony configured (2.1.2) with `server`/`pool` lines in a `.conf` file under `/etc/chrony.d/`: `grep -Pr -- '^\h*(server|pool)\h+[^#\n\r]+' /etc/chrony.d/`.
- Special-purpose services not installed or masked (2.2.x): xorg-x11-server-common, avahi, print server, dhcp server, dns server, ftp server, tftp server, web server, IMAP/POP3, Samba, HTTP proxy, net-snmp (or snmpd not enabled), telnet-server, dnsmasq; MTA in local-only mode (2.2.15); nfs-utils / nfs-server masked (2.2.16), rpcbind masked (2.2.17), rsync-daemon / rsyncd masked (2.2.18). Removal via `dnf remove <pkg>`, e.g. `dnf remove xorg-x11-server-common`.
- Service clients removed (2.3.x): telnet client, LDAP client, FTP client.
- Nonessential services listening on the system removed or masked (2.4, Manual).

## Network configuration (3)

- IPv6 status identified (3.1.1, Manual); network kernel modules disabled (3.1.2–3.1.5): dccp, sctp, rds, tipc — same modprobe.d blacklist pattern as filesystems.
- Host-only parameters (3.2.x): `net.ipv4.ip_forward=0` and `net.ipv6.conf.all.forwarding=0` (3.2.1) — the system will never forward packets or serve as a router; packet redirect sending disabled (3.2.2).
- Host-and-router parameters (3.3.x): source-routed packets not accepted; ICMP redirects and secure ICMP redirects not accepted; suspicious packets logged; broadcast ICMP ignored; bogus ICMP responses ignored; reverse path filtering enabled; `net.ipv4.tcp_syncookies=1` (3.3.8) — SYN cookies let the system keep accepting valid connections under SYN flood; IPv6 router advertisements not accepted.
- Host-based firewall (3.4.x): nftables package installed (3.4.1.1); exactly one firewall utility in use (3.4.1.2) — firewalld enabled+active with nftables disabled/masked, or the reverse, never both; only configure recommendations for the utility in use.
- Firewalld: default zone set per site policy (3.4.2.1, Level 2): `firewall-cmd --get-default-zone`; loopback traffic configured (3.4.2.4); drops unnecessary services and ports (3.4.2.5, Manual).
- NFTables: at least one table exists (3.4.2.2); base chains exist (3.4.2.3); established connections configured (3.4.2.6, Manual); default deny policy (3.4.2.7, Level 2): `systemctl --quiet is-enabled nftables.service && nft list ruleset | grep 'hook input' | grep -v 'policy drop'` returns nothing (same for forward); remediate `nft chain inet filter input { policy drop \; }` (and forward). Ensure a rule allowing SSH exists before setting drop when managing over the network.

## Access, authentication and authorization (4)

- Cron (4.1.x): cronie installed and crond enabled (4.1.1, `rpm -q cronie`); permissions on `/etc/crontab`, `/etc/cron.{hourly,daily,weekly,monthly}`, `/etc/cron.d` (4.1.2–4.1.7); cron restricted to authorized users (4.1.8) — no `/etc/cron.deny`, `/etc/cron.allow` exists, mode 600-class, root:root; at restricted similarly (4.1.9).
- SSH server (4.2.x), audited with `sshd -T -C user=root -C host="$(hostname)" -C addr=...` plus grep of `/etc/ssh/sshd_config` and `/etc/ssh/sshd_config.d/*.conf`:
  - `/etc/ssh/sshd_config` mode 600 root:root (4.2.1); SSH private host keys 0600, public host keys 0644 or stricter (4.2.2–4.2.3); SSH access limited (4.2.4); LogLevel INFO or VERBOSE (4.2.5, default INFO); PAM enabled (4.2.6).
  - `PermitRootLogin no` (4.2.7, default without-password): forces admins to authenticate as themselves then escalate via sudo/su, giving non-repudiation and a clear audit trail.
  - HostbasedAuthentication disabled (4.2.8); PermitEmptyPasswords disabled (4.2.9); PermitUserEnvironment disabled (4.2.10); IgnoreRhosts enabled (4.2.11); X11 forwarding disabled (4.2.12); AllowTcpForwarding disabled (4.2.13).
  - System-wide crypto policy not over-ridden (4.2.14): no `CRYPTO_POLICY=` in `/etc/sysconfig/sshd` or sshd_config.d — overrides could allow weaker Ciphers/MACs/KexAlgorithms.
  - Banner `/etc/issue.net` (4.2.15); MaxAuthTries 4 or less (4.2.16, default 6); MaxStartups 10:30:60 or more restrictive (4.2.17); MaxSessions ≤ 10 (4.2.18); LoginGraceTime ≤ 60s (4.2.19); idle timeout (4.2.20): ClientAliveInterval and ClientAliveCountMax both greater than zero (benchmark example: 15 × 3 ≈ 45s) — protocol-level idle connections, not active-user detection.
- Sudo (4.3.x): sudo installed (4.3.1); sudo commands use pty (4.3.2); dedicated log file (4.3.3): `Defaults logfile="/var/log/sudo.log"` in `/etc/sudoers` or `/etc/sudoers.d/`, edited only with `visudo`/`visudo -f <PATH>` and managed with logrotate; re-authentication not disabled globally (no `!authenticate`); authentication timeout configured (4.3.5); access to `su` restricted (4.3.6).
- authselect (4.4.x): custom authselect profile used (4.4.1, Manual); profile includes with-faillock (4.4.2).
- PAM (4.5.x): password creation requirements (4.5.1) — `pam_pwquality.so try_first_pass ... enforce_for_root retry=3` in `/etc/pam.d/system-auth` and `password-auth`; `minlen = 14` in `/etc/security/pwquality.conf`, complexity via `minclass = 4` OR `dcredit/ucredit/ocredit/lcredit = -1`; failed-attempt lockout (4.5.2) — `/etc/security/faillock.conf` `deny = 5` (1–5; default 3) and `unlock_time = 900` or more (default 600); unlock with `faillock --user <USERNAME> --reset`; password reuse limited (4.5.3, `remember` via pam_pwhistory, `/etc/security/opasswd`); hashing algorithm SHA-512 (4.5.4).
- User accounts and environment (4.6.x): `PASS_MAX_DAYS 365` or less in `/etc/login.defs`, verified per-user in `/etc/shadow` field 5 (`chage --maxdays 365 <user>`); `PASS_MIN_DAYS 1` or more (4.6.1.2); password expiration warning 7 or more (4.6.1.3); inactive password lock 30 days or less (4.6.1.4); all users' last password change in the past (4.6.1.5).
- System accounts secured (4.6.2): accounts below UID_MIN or 65534 (except root/halt/sync/shutdown/nfsnobody) use `nologin` and are locked (`usermod -s $(command -v nologin) <user>`, `usermod -L <user>`).
- Shell timeout (4.6.3): `TMOUT=900` or less, `readonly TMOUT`, `export TMOUT` in `/etc/profile`, `/etc/profile.d/*.sh`, or `/etc/bashrc`; no longer timeout anywhere.
- Root default group GID 0 (4.6.4); default user umask 027 or more restrictive (4.6.5) — new directories 750 and files 640, via pam_umask/`umask` in `/etc/login.defs` or system-wide shell config; root password set (4.6.6, Manual).

## Logging and auditing (5)

- rsyslog (5.1.1.x): installed, enabled, journald configured to send logs to rsyslog; default file permissions `$FileCreateMode 0640` or more restrictive in `/etc/rsyslog.conf` or `/etc/rsyslog.d/*.conf` (5.1.1.4), set before any file is created, then `systemctl restart rsyslog`; logging configured per site policy (5.1.1.5, Manual); remote log host configured (5.1.1.6, Manual); not configured to receive logs from a remote client (5.1.1.7).
- journald (5.1.2.x): systemd-journal-remote installed/configured/enabled (5.1.2.1.x, Manual); journald service enabled (5.1.2.2); compress large log files (5.1.2.3); write to persistent disk (5.1.2.4); not sending to rsyslog if rsyslog is the chosen system (5.1.2.5, Manual); rotation per site policy (5.1.2.6, Manual); default file permissions (5.1.2.7, Manual); not receiving from remote clients (5.1.2.1.4).
- All logfiles have appropriate permissions and ownership (5.1.3).
- auditd (5.2.1.x): auditd installed (5.2.1.1); processes started prior to auditd logged (5.2.1.2); `audit_backlog_limit` sufficient (5.2.1.3, Level 2) — `grubby --info=ALL | grep -Po "\baudit_backlog_limit=\d+\b"`, recommended 8192 or larger, remediate `grubby --update-kernel ALL --args 'audit_backlog_limit=8192'`; auditd service enabled (5.2.1.4, Level 2): `systemctl --now enable auditd`.
- Data retention (5.2.2.x): audit log storage size configured (5.2.2.1); logs not automatically deleted (5.2.2.2); system disabled when audit logs are full (5.2.2.3, Level 2) — `/etc/audit/auditd.conf` `space_left_action = email`, `action_mail_acct = root`, `admin_space_left_action` = halt or single.
- auditd rules (5.2.3.x) in `/etc/audit/rules.d/*.rules`, merged with `augenrules --load` (reboot may be required if `-e 2`): sudoers scope (Level 2): `-w /etc/sudoers -p wa -k scope` and `-w /etc/sudoers.d -p wa -k scope` (5.2.3.1); actions as another user (5.2.3.2); sudo log file modifications (5.2.3.3); date/time changes (5.2.3.4); network environment changes (5.2.3.5); privileged commands (5.2.3.6); unsuccessful file access attempts (5.2.3.7); user/group information changes (5.2.3.8); DAC permission modifications (5.2.3.9); filesystem mounts (5.2.3.10); session initiation (5.2.3.11); login/logout (5.2.3.12); file deletion by users (5.2.3.13); MAC changes (5.2.3.14); chcon/setfacl/chacl/usermod usage (5.2.3.15–5.2.3.18); kernel module load/unload/modification (5.2.3.19); audit configuration immutable (5.2.3.20); running and on-disk configuration the same (5.2.3.21, Manual).
- auditd file access (5.2.4.x): audit log files 0640 or less permissive, owned by authorized users/groups; audit log directory 0750 or more restrictive; audit configuration files 0640 or more restrictive, root:root; audit tools 755 or more restrictive, root:root.
- logrotate configured (5.3, Manual).

## System maintenance (6)

- System file permissions (6.1.x), verified with `stat -Lc "%n %a %u/%U %g/%G" <file>`:

| File | Mode | Owner |
|---|---|---|
| /etc/passwd, /etc/passwd- | 0644 or stricter | root:root |
| /etc/group, /etc/group- | 0644 or stricter | root:root |
| /etc/shadow, /etc/shadow- | 0640 or stricter | root:root |
| /etc/gshadow, /etc/gshadow- | 0640 or stricter | root:root |

  Remediation pattern: `chmod u-x,go-wx /etc/passwd && chown root:root /etc/passwd`. System file permissions audited (6.1.10, Manual); world-writable files/directories secured and directories have sticky bit (6.1.11); no unowned/ungrouped files (6.1.12); SUID/SGID files reviewed (6.1.13, Manual).
- Local user and group settings (6.2.x): shadowed passwords in `/etc/passwd` (6.2.1); non-empty `/etc/shadow` password fields (6.2.2); groups exist (6.2.3); no duplicate UIDs/GIDs/user names/group names (6.2.4–6.2.7); root PATH integrity (6.2.8); root is the only UID 0 account (6.2.9); interactive user home directories configured (6.2.10); dot files access configured (6.2.11).

## Related

- [[grc-frameworks/cis-benchmarks/cis-rhel-9]] — same Benchmark family applied to RHEL 9; AL2023 inherits the RHEL/Fedora tooling (dnf, SELinux, crypto-policies, authselect, auditd) but uses its own section numbering and dnf-specific commands.
