---
title: cis-ubuntu-24-04
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/linux, source/cis]
description: "CIS Ubuntu 24.04 LTS Benchmark v1.0.0 checklist: all recommendations with level and Automated/Manual status."
source_pdf: CIS_Ubuntu_Linux_24.04_LTS_Benchmark_v1.0.0.pdf
---

# CIS Ubuntu Linux 24.04 LTS Benchmark v1.0.0 (08-26-2024)

## Overview

- **Product:** Ubuntu Linux 24.04 LTS
- **Benchmark version:** v1.0.0 (2024-08-26)
- **Profiles:** Level 1 and Level 2, each with a Server and a Workstation variant. Level 1 is the practical baseline with little operational impact; Level 2 is for high-security environments and may reduce functionality.
- **Recommendations:** 312 total (291 Automated, 21 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Initial Setup | 66 |
| 2 Services | 43 |
| 3 Network | 18 |
| 4 Host Based Firewall | 29 |
| 5 Access Control | 71 |
| 6 Logging and Auditing | 62 |
| 7 System Maintenance | 23 |

## Lab relevance

- **SSH (5.1.x):** the k3s nodes and Docker host are reached over SSH; prioritise 5.1.20 PermitRootLogin, 5.1.19 PermitEmptyPasswords, 5.1.16 MaxAuthTries, 5.1.4 sshd access and the cipher/KEX/MAC items (5.1.6, 5.1.12, 5.1.15). 5.1.8 DisableForwarding is L2 Server, so decide deliberately if you rely on SSH tunnels.
- **Kernel networking (3.3.x):** 3.3.1 ip forwarding must be disabled by the benchmark, but k3s (flannel/CNI) and Docker need forwarding on. Document this as an accepted exception on the k3s nodes and the Docker host rather than failing the scan blindly.
- **Kernel modules (1.1.1.x):** 1.1.1.6 overlayfs is L2 and would break containerd/Docker, so skip it on container hosts. 3.2.x (dccp, tipc, rds, sctp) are safe to apply.
- **Host firewall (4.x):** choose one utility (4.1.1) and keep default deny. Docker and kube-proxy write their own iptables/nftables rules, so test ufw rules against published container ports (4.2.6 firewall rules for all open ports, 4.2.7 default deny).
- **Services and listeners (2.1.x):** 2.1.22 only approved services listening, plus 2.1.17/2.1.18 (no stray web proxy or web server services) matter on the Docker host where Caddy is the intended front end. 2.1.21 keeps any MTA local-only.
- **Hardening and patching:** 1.2.2.1 updates and security patches, 1.5.1 ASLR, 1.5.2 ptrace_scope, 1.5.3 core dumps, 1.3.1.x AppArmor (matches Docker's default AppArmor profile).
- **Logging and audit (6.x):** journald (6.1.1.x/6.1.2.x) is L1; auditd rules (6.2.x) are L2 but useful on the Docker host for sudoers and sudo-log changes (6.2.3.1, 6.2.3.3).
- **Accounts and sudo (5.2.x, 5.4.2.x):** sudo with pty and log file (5.2.2, 5.2.3), only root UID 0 (5.4.2.1), pam_faillock lockout (5.3.3.1.x).

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
- [ ] 1.1.1.6 Ensure overlayfs kernel module is not available — L2 · Automated
- [ ] 1.1.1.7 Ensure squashfs kernel module is not available — L2 · Automated
- [ ] 1.1.1.8 Ensure udf kernel module is not available — L2 · Automated
- [ ] 1.1.1.9 Ensure usb-storage kernel module is not available — L1 Server / L2 Workstation · Automated
- [ ] 1.1.1.10 Ensure unused filesystems kernel modules are not available — L1 · Manual

**1.1.2 Configure Filesystem Partitions**

**1.1.2.1 Configure /tmp**

- [ ] 1.1.2.1.1 Ensure /tmp is a separate partition — L1 · Automated
- [ ] 1.1.2.1.2 Ensure nodev option set on /tmp partition — L1 · Automated
- [ ] 1.1.2.1.3 Ensure nosuid option set on /tmp partition — L1 · Automated
- [ ] 1.1.2.1.4 Ensure noexec option set on /tmp partition — L1 · Automated

**1.1.2.2 Configure /dev/shm**

- [ ] 1.1.2.2.1 Ensure /dev/shm is a separate partition — L1 · Automated
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

- [ ] 1.2.1.1 Ensure GPG keys are configured — L1 · Manual
- [ ] 1.2.1.2 Ensure package manager repositories are configured — L1 · Manual

**1.2.2 Configure Package Updates**

- [ ] 1.2.2.1 Ensure updates, patches, and additional security software are installed — L1 · Manual

#### 1.3 Mandatory Access Control

**1.3.1 Configure AppArmor**

- [ ] 1.3.1.1 Ensure AppArmor is installed — L1 · Automated
- [ ] 1.3.1.2 Ensure AppArmor is enabled in the bootloader configuration — L1 · Automated
- [ ] 1.3.1.3 Ensure all AppArmor Profiles are in enforce or complain mode — L1 · Automated
- [ ] 1.3.1.4 Ensure all AppArmor Profiles are enforcing — L2 · Automated

#### 1.4 Configure Bootloader

- [ ] 1.4.1 Ensure bootloader password is set — L1 · Automated
- [ ] 1.4.2 Ensure access to bootloader config is configured — L1 · Automated

#### 1.5 Configure Additional Process Hardening

- [ ] 1.5.1 Ensure address space layout randomization is enabled — L1 · Automated
- [ ] 1.5.2 Ensure ptrace_scope is restricted — L1 · Automated
- [ ] 1.5.3 Ensure core dumps are restricted — L1 · Automated
- [ ] 1.5.4 Ensure prelink is not installed — L1 · Automated
- [ ] 1.5.5 Ensure Automatic Error Reporting is not enabled — L1 · Automated

#### 1.6 Configure Command Line Warning Banners

- [ ] 1.6.1 Ensure message of the day is configured properly — L1 · Automated
- [ ] 1.6.2 Ensure local login warning banner is configured properly — L1 · Automated
- [ ] 1.6.3 Ensure remote login warning banner is configured properly — L1 · Automated
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
- [ ] 2.1.16 Ensure tftp server services are not in use — L1 · Automated
- [ ] 2.1.17 Ensure web proxy server services are not in use — L1 · Automated
- [ ] 2.1.18 Ensure web server services are not in use — L1 · Automated
- [ ] 2.1.19 Ensure xinetd services are not in use — L1 · Automated
- [ ] 2.1.20 Ensure X window server services are not in use — L2 Server · Automated
- [ ] 2.1.21 Ensure mail transfer agent is configured for local-only mode — L1 · Automated
- [ ] 2.1.22 Ensure only approved services are listening on a network interface — L1 · Manual

#### 2.2 Configure Client Services

- [ ] 2.2.1 Ensure NIS Client is not installed — L1 · Automated
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
- [ ] 2.4.1.2 Ensure permissions on /etc/crontab are configured — L1 · Automated
- [ ] 2.4.1.3 Ensure permissions on /etc/cron.hourly are configured — L1 · Automated
- [ ] 2.4.1.4 Ensure permissions on /etc/cron.daily are configured — L1 · Automated
- [ ] 2.4.1.5 Ensure permissions on /etc/cron.weekly are configured — L1 · Automated
- [ ] 2.4.1.6 Ensure permissions on /etc/cron.monthly are configured — L1 · Automated
- [ ] 2.4.1.7 Ensure permissions on /etc/cron.d are configured — L1 · Automated
- [ ] 2.4.1.8 Ensure crontab is restricted to authorized users — L1 · Automated

**2.4.2 Configure at**

- [ ] 2.4.2.1 Ensure at is restricted to authorized users — L1 · Automated

### 3 Network

#### 3.1 Configure Network Devices

- [ ] 3.1.1 Ensure IPv6 status is identified — L1 · Manual
- [ ] 3.1.2 Ensure wireless interfaces are disabled — L1 Server · Automated
- [ ] 3.1.3 Ensure bluetooth services are not in use — L1 Server / L2 Workstation · Automated

#### 3.2 Configure Network Kernel Modules

- [ ] 3.2.1 Ensure dccp kernel module is not available — L2 · Automated
- [ ] 3.2.2 Ensure tipc kernel module is not available — L2 · Automated
- [ ] 3.2.3 Ensure rds kernel module is not available — L2 · Automated
- [ ] 3.2.4 Ensure sctp kernel module is not available — L2 · Automated

#### 3.3 Configure Network Kernel Parameters

- [ ] 3.3.1 Ensure ip forwarding is disabled — L1 · Automated
- [ ] 3.3.2 Ensure packet redirect sending is disabled — L1 · Automated
- [ ] 3.3.3 Ensure bogus icmp responses are ignored — L1 · Automated
- [ ] 3.3.4 Ensure broadcast icmp requests are ignored — L1 · Automated
- [ ] 3.3.5 Ensure icmp redirects are not accepted — L1 · Automated
- [ ] 3.3.6 Ensure secure icmp redirects are not accepted — L1 · Automated
- [ ] 3.3.7 Ensure reverse path filtering is enabled — L1 · Automated
- [ ] 3.3.8 Ensure source routed packets are not accepted — L1 · Automated
- [ ] 3.3.9 Ensure suspicious packets are logged — L1 · Automated
- [ ] 3.3.10 Ensure tcp syn cookies is enabled — L1 · Automated
- [ ] 3.3.11 Ensure ipv6 router advertisements are not accepted — L1 · Automated

### 4 Host Based Firewall

#### 4.1 Configure a single firewall utility

- [ ] 4.1.1 Ensure a single firewall configuration utility is in use — L1 · Automated

#### 4.2 Configure UncomplicatedFirewall

- [ ] 4.2.1 Ensure ufw is installed — L1 · Automated
- [ ] 4.2.2 Ensure iptables-persistent is not installed with ufw — L1 · Automated
- [ ] 4.2.3 Ensure ufw service is enabled — L1 · Automated
- [ ] 4.2.4 Ensure ufw loopback traffic is configured — L1 · Automated
- [ ] 4.2.5 Ensure ufw outbound connections are configured — L1 · Manual
- [ ] 4.2.6 Ensure ufw firewall rules exist for all open ports — L1 · Automated
- [ ] 4.2.7 Ensure ufw default deny firewall policy — L1 · Automated

#### 4.3 Configure nftables

- [ ] 4.3.1 Ensure nftables is installed — L1 · Automated
- [ ] 4.3.2 Ensure ufw is uninstalled or disabled with nftables — L1 · Automated
- [ ] 4.3.3 Ensure iptables are flushed with nftables — L1 · Manual
- [ ] 4.3.4 Ensure a nftables table exists — L1 · Automated
- [ ] 4.3.5 Ensure nftables base chains exist — L1 · Automated
- [ ] 4.3.6 Ensure nftables loopback traffic is configured — L1 · Automated
- [ ] 4.3.7 Ensure nftables outbound and established connections are configured — L1 · Manual
- [ ] 4.3.8 Ensure nftables default deny firewall policy — L1 · Automated
- [ ] 4.3.9 Ensure nftables service is enabled — L1 · Automated
- [ ] 4.3.10 Ensure nftables rules are permanent — L1 · Automated

#### 4.4 Configure iptables

**4.4.1 Configure iptables software**

- [ ] 4.4.1.1 Ensure iptables packages are installed — L1 · Automated
- [ ] 4.4.1.2 Ensure nftables is not in use with iptables — L1 · Automated
- [ ] 4.4.1.3 Ensure ufw is not in use with iptables — L1 · Automated

**4.4.2 Configure IPv4 iptables**

- [ ] 4.4.2.1 Ensure iptables default deny firewall policy — L1 · Automated
- [ ] 4.4.2.2 Ensure iptables loopback traffic is configured — L1 · Automated
- [ ] 4.4.2.3 Ensure iptables outbound and established connections are configured — L1 · Manual
- [ ] 4.4.2.4 Ensure iptables firewall rules exist for all open ports — L1 · Automated

**4.4.3 Configure IPv6 ip6tables**

- [ ] 4.4.3.1 Ensure ip6tables default deny firewall policy — L1 · Automated
- [ ] 4.4.3.2 Ensure ip6tables loopback traffic is configured — L1 · Automated
- [ ] 4.4.3.3 Ensure ip6tables outbound and established connections are configured — L1 · Manual
- [ ] 4.4.3.4 Ensure ip6tables firewall rules exist for all open ports — L1 · Automated

### 5 Access Control

#### 5.1 Configure SSH Server

- [ ] 5.1.1 Ensure permissions on /etc/ssh/sshd_config are configured — L1 · Automated
- [ ] 5.1.2 Ensure permissions on SSH private host key files are configured — L1 · Automated
- [ ] 5.1.3 Ensure permissions on SSH public host key files are configured — L1 · Automated
- [ ] 5.1.4 Ensure sshd access is configured — L1 · Automated
- [ ] 5.1.5 Ensure sshd Banner is configured — L1 · Automated
- [ ] 5.1.6 Ensure sshd Ciphers are configured — L1 · Automated
- [ ] 5.1.7 Ensure sshd ClientAliveInterval and ClientAliveCountMax are configured — L1 · Automated
- [ ] 5.1.8 Ensure sshd DisableForwarding is enabled — L1 Workstation / L2 Server · Automated
- [ ] 5.1.9 Ensure sshd GSSAPIAuthentication is disabled — L1 Workstation / L2 Server · Automated
- [ ] 5.1.10 Ensure sshd HostbasedAuthentication is disabled — L1 · Automated
- [ ] 5.1.11 Ensure sshd IgnoreRhosts is enabled — L1 · Automated
- [ ] 5.1.12 Ensure sshd KexAlgorithms is configured — L1 · Automated
- [ ] 5.1.13 Ensure sshd LoginGraceTime is configured — L1 · Automated
- [ ] 5.1.14 Ensure sshd LogLevel is configured — L1 · Automated
- [ ] 5.1.15 Ensure sshd MACs are configured — L1 · Automated
- [ ] 5.1.16 Ensure sshd MaxAuthTries is configured — L1 · Automated
- [ ] 5.1.17 Ensure sshd MaxSessions is configured — L1 · Automated
- [ ] 5.1.18 Ensure sshd MaxStartups is configured — L1 · Automated
- [ ] 5.1.19 Ensure sshd PermitEmptyPasswords is disabled — L1 · Automated
- [ ] 5.1.20 Ensure sshd PermitRootLogin is disabled — L1 · Automated
- [ ] 5.1.21 Ensure sshd PermitUserEnvironment is disabled — L1 · Automated
- [ ] 5.1.22 Ensure sshd UsePAM is enabled — L1 · Automated

#### 5.2 Configure privilege escalation

- [ ] 5.2.1 Ensure sudo is installed — L1 · Automated
- [ ] 5.2.2 Ensure sudo commands use pty — L1 · Automated
- [ ] 5.2.3 Ensure sudo log file exists — L1 · Automated
- [ ] 5.2.4 Ensure users must provide password for privilege escalation — L2 · Automated
- [ ] 5.2.5 Ensure re-authentication for privilege escalation is not disabled globally — L1 · Automated
- [ ] 5.2.6 Ensure sudo authentication timeout is configured correctly — L1 · Automated
- [ ] 5.2.7 Ensure access to the su command is restricted — L1 · Automated

#### 5.3 Pluggable Authentication Modules

**5.3.1 Configure PAM software packages**

- [ ] 5.3.1.1 Ensure latest version of pam is installed — L1 · Automated
- [ ] 5.3.1.2 Ensure libpam-modules is installed — L1 · Automated
- [ ] 5.3.1.3 Ensure libpam-pwquality is installed — L1 · Automated

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
- [ ] 5.3.3.2.2 Ensure minimum password length is configured — L1 · Automated
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

**6.1.1 Configure systemd-journald service**

- [ ] 6.1.1.1 Ensure journald service is enabled and active — L1 · Automated
- [ ] 6.1.1.2 Ensure journald log file access is configured — L1 · Manual
- [ ] 6.1.1.3 Ensure journald log file rotation is configured — L1 · Manual
- [ ] 6.1.1.4 Ensure only one logging system is in use — L1 · Automated

**6.1.2 Configure journald**

**6.1.2.1 Configure systemd-journal-remote**

- [ ] 6.1.2.1.1 Ensure systemd-journal-remote is installed — L1 · Automated
- [ ] 6.1.2.1.2 Ensure systemd-journal-upload authentication is configured — L1 · Manual
- [ ] 6.1.2.1.3 Ensure systemd-journal-upload is enabled and active — L1 · Automated
- [ ] 6.1.2.1.4 Ensure systemd-journal-remote service is not in use — L1 · Automated
- [ ] 6.1.2.2 Ensure journald ForwardToSyslog is disabled — L1 · Automated
- [ ] 6.1.2.3 Ensure journald Compress is configured — L1 · Automated
- [ ] 6.1.2.4 Ensure journald Storage is configured — L1 · Automated

**6.1.3 Configure rsyslog**

- [ ] 6.1.3.1 Ensure rsyslog is installed — L1 · Automated
- [ ] 6.1.3.2 Ensure rsyslog service is enabled and active — L1 · Automated
- [ ] 6.1.3.3 Ensure journald is configured to send logs to rsyslog — L1 · Automated
- [ ] 6.1.3.4 Ensure rsyslog log file creation mode is configured — L1 · Automated
- [ ] 6.1.3.5 Ensure rsyslog logging is configured — L1 · Manual
- [ ] 6.1.3.6 Ensure rsyslog is configured to send logs to a remote log host — L1 · Manual
- [ ] 6.1.3.7 Ensure rsyslog is not configured to receive logs from a remote client — L1 · Automated
- [ ] 6.1.3.8 Ensure logrotate is configured — L1 · Manual

**6.1.4 Configure Logfiles**

- [ ] 6.1.4.1 Ensure access to all logfiles has been configured — L1 · Automated

#### 6.2 System Auditing

**6.2.1 Configure auditd Service**

- [ ] 6.2.1.1 Ensure auditd packages are installed — L2 · Automated
- [ ] 6.2.1.2 Ensure auditd service is enabled and active — L2 · Automated
- [ ] 6.2.1.3 Ensure auditing for processes that start prior to auditd is enabled — L2 · Automated
- [ ] 6.2.1.4 Ensure audit_backlog_limit is sufficient — L2 · Automated

**6.2.2 Configure Data Retention**

- [ ] 6.2.2.1 Ensure audit log storage size is configured — L2 · Automated
- [ ] 6.2.2.2 Ensure audit logs are not automatically deleted — L2 · Automated
- [ ] 6.2.2.3 Ensure system is disabled when audit logs are full — L2 · Automated
- [ ] 6.2.2.4 Ensure system warns when audit logs are low on space — L2 · Automated

**6.2.3 Configure auditd Rules**

- [ ] 6.2.3.1 Ensure changes to system administration scope (sudoers) is collected — L2 · Automated
- [ ] 6.2.3.2 Ensure actions as another user are always logged — L2 · Automated
- [ ] 6.2.3.3 Ensure events that modify the sudo log file are collected — L2 · Automated
- [ ] 6.2.3.4 Ensure events that modify date and time information are collected — L2 · Automated
- [ ] 6.2.3.5 Ensure events that modify the system's network environment are collected — L2 · Automated
- [ ] 6.2.3.6 Ensure use of privileged commands are collected — L2 · Automated
- [ ] 6.2.3.7 Ensure unsuccessful file access attempts are collected — L2 · Automated
- [ ] 6.2.3.8 Ensure events that modify user/group information are collected — L2 · Automated
- [ ] 6.2.3.9 Ensure discretionary access control permission modification events are collected — L2 · Automated
- [ ] 6.2.3.10 Ensure successful file system mounts are collected — L2 · Automated
- [ ] 6.2.3.11 Ensure session initiation information is collected — L2 · Automated
- [ ] 6.2.3.12 Ensure login and logout events are collected — L2 · Automated
- [ ] 6.2.3.13 Ensure file deletion events by users are collected — L2 · Automated
- [ ] 6.2.3.14 Ensure events that modify the system's Mandatory Access Controls are collected — L2 · Automated
- [ ] 6.2.3.15 Ensure successful and unsuccessful attempts to use the chcon command are collected — L2 · Automated
- [ ] 6.2.3.16 Ensure successful and unsuccessful attempts to use the setfacl command are collected — L2 · Automated
- [ ] 6.2.3.17 Ensure successful and unsuccessful attempts to use the chacl command are collected — L2 · Automated
- [ ] 6.2.3.18 Ensure successful and unsuccessful attempts to use the usermod command are collected — L2 · Automated
- [ ] 6.2.3.19 Ensure kernel module loading unloading and modification is collected — L2 · Automated
- [ ] 6.2.3.20 Ensure the audit configuration is immutable — L2 · Automated
- [ ] 6.2.3.21 Ensure the running and on disk configuration is the same — L2 · Manual

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

#### 7.1 System File Permissions

- [ ] 7.1.1 Ensure permissions on /etc/passwd are configured — L1 · Automated
- [ ] 7.1.2 Ensure permissions on /etc/passwd- are configured — L1 · Automated
- [ ] 7.1.3 Ensure permissions on /etc/group are configured — L1 · Automated
- [ ] 7.1.4 Ensure permissions on /etc/group- are configured — L1 · Automated
- [ ] 7.1.5 Ensure permissions on /etc/shadow are configured — L1 · Automated
- [ ] 7.1.6 Ensure permissions on /etc/shadow- are configured — L1 · Automated
- [ ] 7.1.7 Ensure permissions on /etc/gshadow are configured — L1 · Automated
- [ ] 7.1.8 Ensure permissions on /etc/gshadow- are configured — L1 · Automated
- [ ] 7.1.9 Ensure permissions on /etc/shells are configured — L1 · Automated
- [ ] 7.1.10 Ensure permissions on /etc/security/opasswd are configured — L1 · Automated
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

CIS Ubuntu Linux 24.04 LTS Benchmark v1.0.0 (08-26-2024), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[linux-security/privilege-escalation/permissions]]
- [[linux-security/privilege-escalation/logs]]
- [[linux-security/privilege-escalation/cron-jobs]]
- [[linux-security/privilege-escalation/exploiting-setuid-programs]]
- [[enumeration/protocols-and-ports/22-ssh]]
- [[digital-forensics-and-incident-response/data-collection/unix-linux]]
- [[grc-frameworks/cis-benchmarks/cis-debian-13]]
- [[grc-frameworks/cis-benchmarks/cis-docker]]
- [[grc-frameworks/cis-benchmarks/cis-kubernetes]]
