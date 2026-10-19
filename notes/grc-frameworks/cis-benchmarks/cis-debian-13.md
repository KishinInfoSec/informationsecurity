---
title: cis-debian-13
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Debian 13 Benchmark v1.0.0 checklist: all recommendations with level and Automated/Manual status."
source_pdf: CIS_Debian_Linux_13_Benchmark_v1.0.0.pdf
---

# CIS Debian Linux 13 Benchmark v1.0.0 (12-16-2025)

## Overview

- **Product:** Debian Linux 13
- **Benchmark version:** v1.0.0 (2025-12-16)
- **Profiles:** Level 1 and Level 2, each with a Server and a Workstation variant. Level 1 is the practical baseline with little operational impact; Level 2 is for high-security environments and may reduce functionality.
- **Recommendations:** 343 total (327 Automated, 16 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Initial Setup | 83 |
| 2 Services | 45 |
| 3 Network | 35 |
| 4 Host Based Firewall | 5 |
| 5 Access Control | 72 |
| 6 Logging and Auditing | 80 |
| 7 System Maintenance | 23 |

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Initial Setup

#### 1.1 Filesystem

**1.1.1 Configure Filesystem Kernel Modules**

- [ ] 1.1.1.1 Ensure cramfs kernel module is not available — L1 · Automated
- [ ] 1.1.1.2 Ensure freevxfs kernel module is not available — L1 · Automated
- [ ] 1.1.1.3 Ensure hfs kernel module is not available — L1 · Automated
- [ ] 1.1.1.4 Ensure hfsplus kernel module is not available — L1 · Automated
- [ ] 1.1.1.5 Ensure jffs2 kernel module is not available — L1 · Automated
- [ ] 1.1.1.6 Ensure overlay kernel module is not available — L2 · Automated
- [ ] 1.1.1.7 Ensure squashfs kernel module is not available — L2 · Automated
- [ ] 1.1.1.8 Ensure udf kernel module is not available — L2 · Automated
- [ ] 1.1.1.9 Ensure firewire-core kernel module is not available — L1 Server / L2 Workstation · Automated
- [ ] 1.1.1.10 Ensure usb-storage kernel module is not available — L1 Server / L2 Workstation · Automated
- [ ] 1.1.1.11 Ensure unused filesystems kernel modules are not available — L1 · Manual

**1.1.2 Configure Filesystem Partitions**

**1.1.2.1 Configure /tmp**

- [ ] 1.1.2.1.1 Ensure /tmp is tmpfs or a separate partition — L1 · Automated
- [ ] 1.1.2.1.2 Ensure nodev option set on /tmp partition — L1 · Automated
- [ ] 1.1.2.1.3 Ensure nosuid option set on /tmp partition — L1 · Automated
- [ ] 1.1.2.1.4 Ensure noexec option set on /tmp partition — L1 · Automated

**1.1.2.2 Configure /dev/shm**

- [ ] 1.1.2.2.1 Ensure /dev/shm is tmpfs or a separate partition — L1 · Automated
- [ ] 1.1.2.2.2 Ensure nodev option set on /dev/shm partition — L1 · Automated
- [ ] 1.1.2.2.3 Ensure nosuid option set on /dev/shm partition — L1 · Automated
- [ ] 1.1.2.2.4 Ensure noexec option set on /dev/shm partition — L1 · Automated

**1.1.2.3 Configure /home**

- [ ] 1.1.2.3.1 Ensure separate partition exists for /home — L2 · Automated
- [ ] 1.1.2.3.2 Ensure nodev option set on /home partition — L1 · Automated
- [ ] 1.1.2.3.3 Ensure nosuid option set on /home partition — L1 · Automated

**1.1.2.4 Configure /var**

- [ ] 1.1.2.4.1 Ensure separate partition exists for /var — L2 · Automated
- [ ] 1.1.2.4.2 Ensure nodev option set on /var partition — L1 · Automated
- [ ] 1.1.2.4.3 Ensure nosuid option set on /var partition — L1 · Automated

**1.1.2.5 Configure /var/tmp**

- [ ] 1.1.2.5.1 Ensure separate partition exists for /var/tmp — L2 · Automated
- [ ] 1.1.2.5.2 Ensure nodev option set on /var/tmp partition — L1 · Automated
- [ ] 1.1.2.5.3 Ensure nosuid option set on /var/tmp partition — L1 · Automated
- [ ] 1.1.2.5.4 Ensure noexec option set on /var/tmp partition — L1 · Automated

**1.1.2.6 Configure /var/log**

- [ ] 1.1.2.6.1 Ensure separate partition exists for /var/log — L2 · Automated
- [ ] 1.1.2.6.2 Ensure nodev option set on /var/log partition — L1 · Automated
- [ ] 1.1.2.6.3 Ensure nosuid option set on /var/log partition — L1 · Automated
- [ ] 1.1.2.6.4 Ensure noexec option set on /var/log partition — L1 · Automated

**1.1.2.7 Configure /var/log/audit**

- [ ] 1.1.2.7.1 Ensure separate partition exists for /var/log/audit — L2 · Automated
- [ ] 1.1.2.7.2 Ensure nodev option set on /var/log/audit partition — L1 · Automated
- [ ] 1.1.2.7.3 Ensure nosuid option set on /var/log/audit partition — L1 · Automated
- [ ] 1.1.2.7.4 Ensure noexec option set on /var/log/audit partition — L1 · Automated

#### 1.2 Package Management

**1.2.1 Configure Package Repositories**

- [ ] 1.2.1.1 Ensure the source.list and .source files use the Signed-By option — L1 · Manual
- [ ] 1.2.1.2 Ensure weak dependencies are configured — L2 · Automated
- [ ] 1.2.1.3 Ensure access to gpg key files are configured — L1 Server · Automated
- [ ] 1.2.1.4 Ensure access to /etc/apt/trusted.gpg.d directory is configured — L1 Server · Automated
- [ ] 1.2.1.5 Ensure access to /etc/apt/auth.conf.d directory is configured — L1 Server · Automated
- [ ] 1.2.1.6 Ensure access to files in the /etc/apt/auth.conf.d/ directory is configured — L1 · Automated
- [ ] 1.2.1.7 Ensure access to /usr/share/keyrings directory is configured — L1 Server · Automated
- [ ] 1.2.1.8 Ensure access to /etc/apt/sources.list.d directory is configured — L1 Server · Automated
- [ ] 1.2.1.9 Ensure access to files in /etc/apt/sources.list.d are configured — L1 Server · Automated

**1.2.2 Configure Package Updates**

- [ ] 1.2.2.1 Ensure updates, patches, and additional security software are installed — L1 · Manual

#### 1.3 Mandatory Access Control

**1.3.1 Configure AppArmor**

- [ ] 1.3.1.1 Ensure apparmor packages are installed — L1 · Automated
- [ ] 1.3.1.2 Ensure AppArmor is enabled — L1 · Automated
- [ ] 1.3.1.3 Ensure all AppArmor Profiles are enforcing — L2 · Automated
- [ ] 1.3.1.4 Ensure apparmor_restrict_unprivileged_unconfined is enabled — L1 · Automated

#### 1.4 Configure Bootloader

- [ ] 1.4.1 Ensure bootloader password is set — L1 · Automated
- [ ] 1.4.2 Ensure access to bootloader config is configured — L1 · Automated

#### 1.5 Configure Additional Process Hardening

- [ ] 1.5.1 Ensure fs.protected_hardlinks is configured — L1 · Automated
- [ ] 1.5.2 Ensure fs.protected_symlinks is configured — L2 · Automated
- [ ] 1.5.3 Ensure kernel.yama.ptrace_scope is configured — L1 · Automated
- [ ] 1.5.4 Ensure fs.suid_dumpable is configured — L1 · Automated
- [ ] 1.5.5 Ensure kernel.dmesg_restrict is configured — L1 · Automated
- [ ] 1.5.6 Ensure prelink is not installed — L1 · Automated
- [ ] 1.5.7 Ensure Automatic Error Reporting is configured — L1 · Automated
- [ ] 1.5.8 Ensure kernel.kptr_restrict is configured — L1 · Automated
- [ ] 1.5.9 Ensure kernel.randomize_va_space is configured — L1 · Automated
- [ ] 1.5.10 Ensure kernel.yama.ptrace_scope is configured — L1 · Automated
- [ ] 1.5.11 Ensure core file size is configured — L1 · Automated
- [ ] 1.5.12 Ensure systemd-coredump ProcessSizeMax is configured — L1 · Automated
- [ ] 1.5.13 Ensure systemd-coredump Storage is configured — L1 · Automated

#### 1.6 Configure Command Line Warning Banners

- [ ] 1.6.1 Ensure /etc/motd is configured — L1 · Automated
- [ ] 1.6.2 Ensure /etc/issue is configured — L1 · Automated
- [ ] 1.6.3 Ensure /etc/issue.net is configured — L1 · Automated
- [ ] 1.6.4 Ensure access to /etc/motd is configured — L1 · Automated
- [ ] 1.6.5 Ensure access to /etc/issue is configured — L1 · Automated
- [ ] 1.6.6 Ensure access to /etc/issue.net is configured — L1 · Automated

#### 1.7 Configure GNOME Display Manager

- [ ] 1.7.1 Ensure GDM is removed — L2 Server · Automated
- [ ] 1.7.2 Ensure GDM login banner is configured — L1 · Automated
- [ ] 1.7.3 Ensure GDM disable-user-list option is enabled — L1 · Automated
- [ ] 1.7.4 Ensure GDM screen locks when the user is idle — L1 · Automated
- [ ] 1.7.5 Ensure GDM screen locks cannot be overridden — L1 · Automated
- [ ] 1.7.6 Ensure GDM automatic mounting of removable media is disabled — L1 Server / L2 Workstation · Automated
- [ ] 1.7.7 Ensure GDM disabling automatic mounting of removable media is not overridden — L1 Server / L2 Workstation · Automated
- [ ] 1.7.8 Ensure GDM autorun-never is enabled — L1 · Automated
- [ ] 1.7.9 Ensure GDM autorun-never is not overridden — L1 · Automated
- [ ] 1.7.10 Ensure XDMCP is not enabled — L1 · Automated
- [ ] 1.7.11 Ensure Xwayland is configured — L2 · Automated

### 2 Services

#### 2.1 Configure Server Services

- [ ] 2.1.1 Ensure autofs services are not in use — L1 Server / L2 Workstation · Automated
- [ ] 2.1.2 Ensure avahi daemon services are not in use — L1 Server / L2 Workstation · Automated
- [ ] 2.1.3 Ensure dhcp server services are not in use — L1 · Automated
- [ ] 2.1.4 Ensure dns server services are not in use — L1 · Automated
- [ ] 2.1.5 Ensure dnsmasq services are not in use — L1 · Automated
- [ ] 2.1.6 Ensure ftp server services are not in use — L1 · Automated
- [ ] 2.1.7 Ensure ldap server services are not in use — L1 · Automated
- [ ] 2.1.8 Ensure message access server services are not in use — L1 · Automated
- [ ] 2.1.9 Ensure network file system services are not in use — L1 · Automated
- [ ] 2.1.10 Ensure nis server services are not in use — L1 · Automated
- [ ] 2.1.11 Ensure print server services are not in use — L1 Server / L2 Workstation · Automated
- [ ] 2.1.12 Ensure rpcbind services are not in use — L1 · Automated
- [ ] 2.1.13 Ensure rsync services are not in use — L1 · Automated
- [ ] 2.1.14 Ensure samba file server services are not in use — L1 · Automated
- [ ] 2.1.15 Ensure snmp services are not in use — L1 · Automated
- [ ] 2.1.16 Ensure telnet-server services are not in use — L1 · Automated
- [ ] 2.1.17 Ensure tftp server services are not in use — L1 · Automated
- [ ] 2.1.18 Ensure web proxy server services are not in use — L1 · Automated
- [ ] 2.1.19 Ensure web server services are not in use — L1 · Automated
- [ ] 2.1.20 Ensure xinetd services are not in use — L1 · Automated
- [ ] 2.1.21 Ensure X window server services are not in use — L2 Server · Automated
- [ ] 2.1.22 Ensure mail transfer agents are configured for local-only mode — L1 · Automated
- [ ] 2.1.23 Ensure only approved services are listening on a network interface — L1 · Manual

#### 2.2 Configure Client Services

- [ ] 2.2.1 Ensure nis client is not installed — L1 · Automated
- [ ] 2.2.2 Ensure rsh client is not installed — L1 · Automated
- [ ] 2.2.3 Ensure talk client is not installed — L1 · Automated
- [ ] 2.2.4 Ensure telnet client is not installed — L1 · Automated
- [ ] 2.2.5 Ensure ldap client is not installed — L1 · Automated
- [ ] 2.2.6 Ensure ftp client is not installed — L1 · Automated

#### 2.3 Configure Time Synchronization

**2.3.1 Ensure time synchronization is in use**

- [ ] 2.3.1.1 Ensure a single time synchronization daemon is in use — L1 · Automated

**2.3.2 Configure systemd-timesyncd**

- [ ] 2.3.2.1 Ensure systemd-timesyncd configured with authorized timeserver — L1 · Automated
- [ ] 2.3.2.2 Ensure systemd-timesyncd is enabled and running — L1 · Automated

**2.3.3 Configure chrony**

- [ ] 2.3.3.1 Ensure chrony is configured with authorized timeserver — L1 · Automated
- [ ] 2.3.3.2 Ensure chrony is running as user _chrony — L1 · Automated
- [ ] 2.3.3.3 Ensure chrony is enabled and running — L1 · Automated

#### 2.4 Job Schedulers

**2.4.1 Configure cron**

- [ ] 2.4.1.1 Ensure cron daemon is enabled and active — L1 · Automated
- [ ] 2.4.1.2 Ensure access to /etc/crontab is configured — L1 · Automated
- [ ] 2.4.1.3 Ensure access to /etc/cron.hourly is configured — L1 · Automated
- [ ] 2.4.1.4 Ensure access to /etc/cron.daily is configured — L1 · Automated
- [ ] 2.4.1.5 Ensure access to /etc/cron.weekly is configured — L1 · Automated
- [ ] 2.4.1.6 Ensure access to /etc/cron.monthly is configured — L1 · Automated
- [ ] 2.4.1.7 Ensure access to /etc/cron.yearly is configured — L1 · Automated
- [ ] 2.4.1.8 Ensure access to /etc/cron.d is configured — L1 · Automated
- [ ] 2.4.1.9 Ensure access to crontab is configured — L1 · Automated

**2.4.2 Configure at**

- [ ] 2.4.2.1 Ensure access to at is configured — L1 · Automated

### 3 Network

#### 3.1 Configure Network Devices

- [ ] 3.1.1 Ensure IPv6 status is identified — L1 · Manual
- [ ] 3.1.2 Ensure wireless interfaces are not available — L1 Server · Automated
- [ ] 3.1.3 Ensure bluetooth services are not in use — L1 Server / L2 Workstation · Automated

#### 3.2 Configure Network Kernel Modules

- [ ] 3.2.1 Ensure atm kernel module is not available — L1 · Automated
- [ ] 3.2.2 Ensure can kernel module is not available — L1 · Automated
- [ ] 3.2.3 Ensure dccp kernel module is not available — L1 · Automated
- [ ] 3.2.4 Ensure rds kernel module is not available — L1 · Automated
- [ ] 3.2.5 Ensure sctp kernel module is not available — L1 · Automated
- [ ] 3.2.6 Ensure tipc kernel module is not available — L1 · Automated

#### 3.3 Configure Network Kernel Parameters

**3.3.1 Configure IPv4 parameters**

- [ ] 3.3.1.1 Ensure net.ipv4.ip_forward is configured — L1 Workstation / L2 Server · Automated
- [ ] 3.3.1.2 Ensure net.ipv4.conf.all.forwarding is configured — L1 · Automated
- [ ] 3.3.1.3 Ensure net.ipv4.conf.default.forwarding is configured — L1 · Automated
- [ ] 3.3.1.4 Ensure net.ipv4.conf.all.send_redirects is configured — L1 · Automated
- [ ] 3.3.1.5 Ensure net.ipv4.conf.default.send_redirects is configured — L1 · Automated
- [ ] 3.3.1.6 Ensure net.ipv4.icmp_ignore_bogus_error_responses is configured — L1 · Automated
- [ ] 3.3.1.7 Ensure net.ipv4.icmp_echo_ignore_broadcasts is configured — L1 · Automated
- [ ] 3.3.1.8 Ensure net.ipv4.conf.all.accept_redirects is configured — L1 · Automated
- [ ] 3.3.1.9 Ensure net.ipv4.conf.default.accept_redirects is configured — L1 · Automated
- [ ] 3.3.1.10 Ensure net.ipv4.conf.all.secure_redirects is configured — L1 · Automated
- [ ] 3.3.1.11 Ensure net.ipv4.conf.default.secure_redirects is configured — L1 · Automated
- [ ] 3.3.1.12 Ensure net.ipv4.conf.all.rp_filter is configured — L1 · Automated
- [ ] 3.3.1.13 Ensure net.ipv4.conf.default.rp_filter is configured — L1 · Automated
- [ ] 3.3.1.14 Ensure net.ipv4.conf.all.accept_source_route is configured — L1 · Automated
- [ ] 3.3.1.15 Ensure net.ipv4.conf.default.accept_source_route is configured — L1 · Automated
- [ ] 3.3.1.16 Ensure net.ipv4.conf.all.log_martians is configured — L1 · Automated
- [ ] 3.3.1.17 Ensure net.ipv4.conf.default.log_martians is configured — L1 · Automated
- [ ] 3.3.1.18 Ensure net.ipv4.tcp_syncookies is configured — L1 · Automated

**3.3.2 Configure IPv6 parameters**

- [ ] 3.3.2.1 Ensure net.ipv6.conf.all.forwarding is configured — L1 · Automated
- [ ] 3.3.2.2 Ensure net.ipv6.conf.default.forwarding is configured — L1 · Automated
- [ ] 3.3.2.3 Ensure net.ipv6.conf.all.accept_redirects is configured — L1 · Automated
- [ ] 3.3.2.4 Ensure net.ipv6.conf.default.accept_redirects is configured — L1 · Automated
- [ ] 3.3.2.5 Ensure net.ipv6.conf.all.accept_source_route is configured — L1 · Automated
- [ ] 3.3.2.6 Ensure net.ipv6.conf.default.accept_source_route is configured — L1 · Automated
- [ ] 3.3.2.7 Ensure net.ipv6.conf.all.accept_ra is configured — L1 · Automated
- [ ] 3.3.2.8 Ensure net.ipv6.conf.default.accept_ra is configured — L1 · Automated

### 4 Host Based Firewall

#### 4.1 Configure Uncomplicated Firewall

- [ ] 4.1.1 Ensure ufw is installed — L1 · Automated
- [ ] 4.1.2 Ensure ufw service is configured — L1 · Automated
- [ ] 4.1.3 Ensure ufw incoming default is configured — L1 · Automated
- [ ] 4.1.4 Ensure ufw outgoing default is configured — L2 · Automated
- [ ] 4.1.5 Ensure ufw routed default is configured — L1 · Automated

### 5 Access Control

#### 5.1 Configure SSH Server

- [ ] 5.1.1 Ensure access to /etc/ssh/sshd_config is configured — L1 · Automated
- [ ] 5.1.2 Ensure access to SSH private host key files is configured — L1 · Automated
- [ ] 5.1.3 Ensure access to SSH public host key files is configured — L1 · Automated
- [ ] 5.1.4 Ensure sshd access is configured — L1 · Automated
- [ ] 5.1.5 Ensure sshd Banner is configured — L1 · Automated
- [ ] 5.1.6 Ensure sshd Ciphers are configured — L1 · Automated
- [ ] 5.1.7 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured — L1 · Automated
- [ ] 5.1.8 Ensure sshd DisableForwarding is enabled — L1 Workstation / L2 Server · Automated
- [ ] 5.1.9 Ensure sshd GSSAPIAuthentication is disabled — L1 Workstation / L2 Server · Automated
- [ ] 5.1.10 Ensure sshd HostbasedAuthentication is disabled — L1 · Automated
- [ ] 5.1.11 Ensure sshd IgnoreRhosts is enabled — L1 · Automated
- [ ] 5.1.12 Ensure sshd KexAlgorithms is configured — L1 · Automated
- [ ] 5.1.13 Ensure sshd post-quantum cryptography key exchange algorithms are configured — L1 · Automated
- [ ] 5.1.14 Ensure sshd LoginGraceTime is configured — L1 · Automated
- [ ] 5.1.15 Ensure sshd LogLevel is configured — L1 · Automated
- [ ] 5.1.16 Ensure sshd MACs are configured — L1 · Automated
- [ ] 5.1.17 Ensure sshd MaxAuthTries is configured — L1 · Automated
- [ ] 5.1.18 Ensure sshd MaxSessions is configured — L1 · Automated
- [ ] 5.1.19 Ensure sshd MaxStartups is configured — L1 · Automated
- [ ] 5.1.20 Ensure sshd PermitEmptyPasswords is disabled — L1 · Automated
- [ ] 5.1.21 Ensure sshd PermitRootLogin is disabled — L1 · Automated
- [ ] 5.1.22 Ensure sshd PermitUserEnvironment is disabled — L1 · Automated
- [ ] 5.1.23 Ensure sshd UsePAM is enabled — L1 · Automated

#### 5.2 Configure privilege escalation

- [ ] 5.2.1 Ensure sudo is installed — L1 · Automated
- [ ] 5.2.2 Ensure sudo commands use pty — L1 · Automated
- [ ] 5.2.3 Ensure sudo log file exists — L1 · Automated
- [ ] 5.2.4 Ensure users must provide password for escalation — L2 · Automated
- [ ] 5.2.5 Ensure re-authentication for privilege escalation is not disabled globally — L1 · Automated
- [ ] 5.2.6 Ensure sudo timestamp_timeout is configured — L1 · Automated
- [ ] 5.2.7 Ensure access to the su command is restricted — L1 · Automated

#### 5.3 Pluggable Authentication Modules

**5.3.1 Configure PAM software packages**

- [ ] 5.3.1.1 Ensure latest version of pam is installed — L1 · Automated
- [ ] 5.3.1.2 Ensure latest version of libpam-modules is installed — L1 · Automated
- [ ] 5.3.1.3 Ensure latest version of libpam-pwquality is installed — L1 · Automated

**5.3.2 Configure pam-auth-update profiles**

- [ ] 5.3.2.1 Ensure pam_unix module is enabled — L1 · Automated
- [ ] 5.3.2.2 Ensure pam_faillock module is enabled — L1 · Automated
- [ ] 5.3.2.3 Ensure pam_pwquality module is enabled — L1 · Automated
- [ ] 5.3.2.4 Ensure pam_pwhistory module is enabled — L1 · Automated

**5.3.3 Configure PAM Arguments**

**5.3.3.1 Configure pam_faillock module**

- [ ] 5.3.3.1.1 Ensure password failed attempts lockout is configured — L1 · Automated
- [ ] 5.3.3.1.2 Ensure password unlock time is configured — L1 · Automated
- [ ] 5.3.3.1.3 Ensure password failed attempts lockout includes root account — L2 · Automated

**5.3.3.2 Configure pam_pwquality module**

- [ ] 5.3.3.2.1 Ensure password number of changed characters is configured — L1 · Automated
- [ ] 5.3.3.2.2 Ensure password length is configured — L1 · Automated
- [ ] 5.3.3.2.3 Ensure password complexity is configured — L1 · Manual
- [ ] 5.3.3.2.4 Ensure password same consecutive characters is configured — L1 · Automated
- [ ] 5.3.3.2.5 Ensure password maximum sequential characters is configured — L1 · Automated
- [ ] 5.3.3.2.6 Ensure password dictionary check is enabled — L1 · Automated
- [ ] 5.3.3.2.7 Ensure password quality checking is enforced — L1 · Automated
- [ ] 5.3.3.2.8 Ensure password quality is enforced for the root user — L1 · Automated

**5.3.3.3 Configure pam_pwhistory module**

- [ ] 5.3.3.3.1 Ensure password history remember is configured — L1 · Automated
- [ ] 5.3.3.3.2 Ensure password history is enforced for the root user — L1 · Automated
- [ ] 5.3.3.3.3 Ensure pam_pwhistory includes use_authtok — L1 · Automated

**5.3.3.4 Configure pam_unix module**

- [ ] 5.3.3.4.1 Ensure pam_unix does not include nullok — L1 · Automated
- [ ] 5.3.3.4.2 Ensure pam_unix does not include remember — L1 · Automated
- [ ] 5.3.3.4.3 Ensure pam_unix includes a strong password hashing algorithm — L1 · Automated
- [ ] 5.3.3.4.4 Ensure pam_unix includes use_authtok — L1 · Automated

#### 5.4 User Accounts and Environment

**5.4.1 Configure shadow password suite parameters**

- [ ] 5.4.1.1 Ensure password expiration is configured — L1 · Automated
- [ ] 5.4.1.2 Ensure minimum password days is configured — L2 · Manual
- [ ] 5.4.1.3 Ensure password expiration warning days is configured — L1 · Automated
- [ ] 5.4.1.4 Ensure strong password hashing algorithm is configured — L1 · Automated
- [ ] 5.4.1.5 Ensure inactive password lock is configured — L1 · Automated
- [ ] 5.4.1.6 Ensure all users last password change date is in the past — L1 · Automated

**5.4.2 Configure root and system accounts and environment**

- [ ] 5.4.2.1 Ensure root is the only UID 0 account — L1 · Automated
- [ ] 5.4.2.2 Ensure root is the only GID 0 account — L1 · Automated
- [ ] 5.4.2.3 Ensure group root is the only GID 0 group — L1 · Automated
- [ ] 5.4.2.4 Ensure root account access is controlled — L1 · Automated
- [ ] 5.4.2.5 Ensure root path integrity — L1 · Automated
- [ ] 5.4.2.6 Ensure root user umask is configured — L1 · Automated
- [ ] 5.4.2.7 Ensure system accounts do not have a valid login shell — L1 · Automated
- [ ] 5.4.2.8 Ensure accounts without a valid login shell are locked — L1 · Automated

**5.4.3 Configure user default environment**

- [ ] 5.4.3.1 Ensure nologin is not listed in /etc/shells — L2 · Automated
- [ ] 5.4.3.2 Ensure default user shell timeout is configured — L1 · Automated
- [ ] 5.4.3.3 Ensure default user umask is configured — L1 · Automated

### 6 Logging and Auditing

#### 6.1 System Logging

**6.1.1 Configure journald**

**6.1.1.1 Configure systemd-journald service**

- [ ] 6.1.1.1.1 Ensure journald service is active — L1 · Automated
- [ ] 6.1.1.1.2 Ensure journald log file access is configured — L1 · Manual
- [ ] 6.1.1.1.3 Ensure journald log file rotation is configured — L1 · Manual
- [ ] 6.1.1.1.4 Ensure journald ForwardToSyslog is disabled — L1 · Automated
- [ ] 6.1.1.1.5 Ensure journald Storage is configured — L1 · Automated
- [ ] 6.1.1.1.6 Ensure journald Compress is configured — L1 · Automated

**6.1.1.2 Configure systemd-journal-remote**

- [ ] 6.1.1.2.1 Ensure systemd-journal-remote is installed — L1 · Automated
- [ ] 6.1.1.2.2 Ensure systemd-journal-upload authentication is configured — L1 · Manual
- [ ] 6.1.1.2.3 Ensure systemd-journal-upload is enabled and active — L1 · Automated
- [ ] 6.1.1.2.4 Ensure systemd-journal-remote service is not in use — L1 · Automated

**6.1.2 Configure rsyslog**

- [ ] 6.1.2.1 Ensure rsyslog is installed — L1 · Automated
- [ ] 6.1.2.2 Ensure rsyslog service is enabled and active — L1 · Automated
- [ ] 6.1.2.3 Ensure journald is configured to send logs to rsyslog — L1 · Automated
- [ ] 6.1.2.4 Ensure rsyslog log file creation mode is configured — L1 · Automated
- [ ] 6.1.2.5 Ensure rsyslog logging is configured — L1 · Manual
- [ ] 6.1.2.6 Ensure rsyslog is configured to send logs to a remote log host — L1 · Manual
- [ ] 6.1.2.7 Ensure rsyslog is not configured to receive logs from a remote client — L1 · Automated
- [ ] 6.1.2.8 Ensure logrotate is configured — L1 · Manual
- [ ] 6.1.2.9 Ensure rsyslog-gnutls is installed — L2 · Automated
- [ ] 6.1.2.10 Ensure rsyslog forwarding uses gtls — L2 · Automated
- [ ] 6.1.2.11 Ensure rsyslog CA certificates are configured — L2 · Manual

**6.1.3 Configure Logfiles**

- [ ] 6.1.3.1 Ensure access to all logfiles has been configured — L1 · Automated

#### 6.2 System Auditing

**6.2.1 Configure auditd Service**

- [ ] 6.2.1.1 Ensure auditd packages are installed — L2 · Automated
- [ ] 6.2.1.2 Ensure auditd service is enabled and active — L2 · Automated
- [ ] 6.2.1.3 Ensure auditing for processes that start prior to auditd is enabled — L2 · Automated
- [ ] 6.2.1.4 Ensure audit_backlog_limit is configured — L2 · Automated

**6.2.2 Configure Data Retention**

- [ ] 6.2.2.1 Ensure audit log storage size is configured — L2 · Automated
- [ ] 6.2.2.2 Ensure audit logs are not automatically deleted — L2 · Automated
- [ ] 6.2.2.3 Ensure system is disabled when audit logs are full — L2 · Automated
- [ ] 6.2.2.4 Ensure system warns when audit logs are low on space — L2 · Automated

**6.2.3 Configure auditd Rules**

- [ ] 6.2.3.1 Ensure modification of the /etc/sudoers file is collected — L2 · Automated
- [ ] 6.2.3.2 Ensure actions as another user are always logged — L2 · Automated
- [ ] 6.2.3.3 Ensure events that modify the sudo log file are collected — L2 · Automated
- [ ] 6.2.3.4 Ensure events that modify date and time information are collected — L2 · Automated
- [ ] 6.2.3.5 Ensure events that modify sethostname and setdomainname are collected — L2 · Automated
- [ ] 6.2.3.6 Ensure events that modify /etc/issue and /etc/issue.net are collected — L2 · Automated
- [ ] 6.2.3.7 Ensure events that modify /etc/hosts and /etc/hostname are collected — L2 · Automated
- [ ] 6.2.3.8 Ensure events that modify the system's network environment are collected — L2 · Automated
- [ ] 6.2.3.9 Ensure events that modify /etc/NetworkManager directory are collected — L2 · Automated
- [ ] 6.2.3.10 Ensure use of privileged commands are collected — L2 · Automated
- [ ] 6.2.3.11 Ensure unsuccessful file access attempts are collected — L2 · Automated
- [ ] 6.2.3.12 Ensure events that modify /etc/group information are collected — L2 · Automated
- [ ] 6.2.3.13 Ensure events that modify /etc/passwd information are collected — L2 · Automated
- [ ] 6.2.3.14 Ensure events that modify /etc/shadow and /etc/gshadow are collected — L2 · Automated
- [ ] 6.2.3.15 Ensure events that modify /etc/security/opasswd are collected — L2 · Automated
- [ ] 6.2.3.16 Ensure events that modify /etc/nsswitch.conf file are collected — L2 · Automated
- [ ] 6.2.3.17 Ensure events that modify /etc/pam.conf and /etc/pam.d/ information are collected — L2 · Automated
- [ ] 6.2.3.18 Ensure discretionary access control permission modification events chmod,fchmod,fchmodat,fchmodat2 are collected — L2 · Automated
- [ ] 6.2.3.19 Ensure discretionary access control permission modification events chown,fchown,lchown,fchownat are collected — L2 · Automated
- [ ] 6.2.3.20 Ensure discretionary access control permission modification events setxattr,lsetxattr,fsetxattr,removexattr,lremovexattr,fremovexattr collected — L2 · Automated
- [ ] 6.2.3.21 Ensure successful file system mounts are collected — L2 · Automated
- [ ] 6.2.3.22 Ensure session initiation information is collected — L2 · Automated
- [ ] 6.2.3.23 Ensure login and logout events are collected — L2 · Automated
- [ ] 6.2.3.24 Ensure unlink file deletion events by users are collected — L2 · Automated
- [ ] 6.2.3.25 Ensure rename file deletion events by users are collected — L2 · Automated
- [ ] 6.2.3.26 Ensure events that modify the system's Mandatory Access Controls are collected — L2 · Automated
- [ ] 6.2.3.27 Ensure successful and unsuccessful attempts to use the chcon command are collected — L2 · Automated
- [ ] 6.2.3.28 Ensure successful and unsuccessful attempts to use the setfacl command are collected — L2 · Automated
- [ ] 6.2.3.29 Ensure successful and unsuccessful attempts to use the chacl command are collected — L2 · Automated
- [ ] 6.2.3.30 Ensure successful and unsuccessful attempts to use the usermod command are collected — L2 · Automated
- [ ] 6.2.3.31 Ensure kernel module loading unloading and modification is collected — L2 · Automated
- [ ] 6.2.3.32 Ensure kernel "init_module" and "finit_module" loading unloading and modification is collected — L2 · Automated
- [ ] 6.2.3.33 Ensure kernel "delete_module" loading unloading and modification is collected — L2 · Automated
- [ ] 6.2.3.34 Ensure kernel query_module loading unloading and modification is collected — L2 · Automated
- [ ] 6.2.3.35 Ensure the audit configuration is loaded regardless of errors — L2 · Automated
- [ ] 6.2.3.36 Ensure the audit configuration is immutable — L2 · Automated
- [ ] 6.2.3.37 Ensure the running and on disk configuration is the same — L2 · Manual

**6.2.4 Configure auditd File Access**

- [ ] 6.2.4.1 Ensure audit log files mode is configured — L2 · Automated
- [ ] 6.2.4.2 Ensure audit log files owner is configured — L2 · Automated
- [ ] 6.2.4.3 Ensure audit log files group owner is configured — L2 · Automated
- [ ] 6.2.4.4 Ensure the audit log file directory mode is configured — L2 · Automated
- [ ] 6.2.4.5 Ensure audit configuration files mode is configured — L2 · Automated
- [ ] 6.2.4.6 Ensure audit configuration files owner is configured — L2 · Automated
- [ ] 6.2.4.7 Ensure audit configuration files group owner is configured — L2 · Automated
- [ ] 6.2.4.8 Ensure audit tools mode is configured — L2 · Automated
- [ ] 6.2.4.9 Ensure audit tools owner is configured — L2 · Automated
- [ ] 6.2.4.10 Ensure audit tools group owner is configured — L2 · Automated

#### 6.3 Configure Integrity Checking

- [ ] 6.3.1 Ensure AIDE is installed — L1 · Automated
- [ ] 6.3.2 Ensure filesystem integrity is regularly checked — L1 · Automated
- [ ] 6.3.3 Ensure cryptographic mechanisms are used to protect the integrity of audit tools — L2 · Automated

### 7 System Maintenance

#### 7.1 Configure system file and directory access

- [ ] 7.1.1 Ensure access to /etc/passwd is configured — L1 · Automated
- [ ] 7.1.2 Ensure access to /etc/passwd- is configured — L1 · Automated
- [ ] 7.1.3 Ensure access to /etc/group is configured — L1 · Automated
- [ ] 7.1.4 Ensure access to /etc/group- is configured — L1 · Automated
- [ ] 7.1.5 Ensure access to /etc/shadow is configured — L1 · Automated
- [ ] 7.1.6 Ensure access to /etc/shadow- is configured — L1 · Automated
- [ ] 7.1.7 Ensure access to /etc/gshadow is configured — L1 · Automated
- [ ] 7.1.8 Ensure access to /etc/gshadow- is configured — L1 · Automated
- [ ] 7.1.9 Ensure access to /etc/shells is configured — L1 · Automated
- [ ] 7.1.10 Ensure access to /etc/security/opasswd is configured — L1 · Automated
- [ ] 7.1.11 Ensure world writable files and directories are secured — L1 · Automated
- [ ] 7.1.12 Ensure no files or directories without an owner and a group exist — L1 · Automated
- [ ] 7.1.13 Ensure SUID and SGID files are reviewed — L1 · Manual

#### 7.2 Local User and Group Settings

- [ ] 7.2.1 Ensure accounts in /etc/passwd use shadowed passwords — L1 · Automated
- [ ] 7.2.2 Ensure /etc/shadow password fields are not empty — L1 · Automated
- [ ] 7.2.3 Ensure all groups in /etc/passwd exist in /etc/group — L1 · Automated
- [ ] 7.2.4 Ensure shadow group is empty — L1 · Automated
- [ ] 7.2.5 Ensure no duplicate UIDs exist — L1 · Automated
- [ ] 7.2.6 Ensure no duplicate GIDs exist — L1 · Automated
- [ ] 7.2.7 Ensure no duplicate user names exist — L1 · Automated
- [ ] 7.2.8 Ensure no duplicate group names exist — L1 · Automated
- [ ] 7.2.9 Ensure local interactive user home directories are configured — L1 · Automated
- [ ] 7.2.10 Ensure local interactive user dot files access is configured — L1 · Automated

## Source

CIS Debian Linux 13 Benchmark v1.0.0 (12-16-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[linux-security/privilege-escalation/permissions]]
- [[linux-security/privilege-escalation/logs]]
- [[linux-security/privilege-escalation/cron-jobs]]
- [[linux-security/privilege-escalation/exploiting-setuid-programs]]
- [[enumeration/protocols-and-ports/22-ssh]]
- [[digital-forensics-and-incident-response/data-collection/unix-linux]]
- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
- [[grc-frameworks/cis-benchmarks/cis-almalinux-9]]
