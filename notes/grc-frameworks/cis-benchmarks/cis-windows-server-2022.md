---
title: cis-windows-server-2022
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/windows, source/cis]
description: "CIS Microsoft Windows Server 2022 Benchmark v5.0.0 checklist: account policy, audit policy, firewall, services, with levels."
source_pdf: CIS_Microsoft_Windows_Server_2022_Benchmark_v5.0.0.pdf
---

# CIS Microsoft Windows Server 2022 Benchmark v5.0.0 (02-20-2026)

## Overview

- **Product:** Microsoft Windows Server 2022 (Group Policy / registry settings); secure configuration guide based on Server 2022, tested against Microsoft Windows Server 2022 Datacenter edition.
- **Benchmark version:** v5.0.0 (published 02-20-2026).
- **Audience:** written for Active Directory domain-joined systems using Active Directory's Group Policy Manager only — not for standalone or workgroup systems, systems cloud-joined to Entra ID, or cloud-created systems. Covers AD and Entra Hybrid joined endpoint states that receive policy from AD Group Policy Manager only.
- **ADMX dependency:** all Windows OS Benchmarks, including Server, need the newest Windows 11 ADMX/ADML templates (the benchmark cites *Download Administrative Templates (.admx) for Windows 11 2025 Update (25H2)*) so all required GPOs exist for compliance.
- **Recommendation counts (from the table of contents):** 432 total — 1 Account Policies (11), 2 Local Policies (118), 5 System Services (2), 9 Windows Defender Firewall (23), 17 Advanced Audit Policy Configuration (34), 18 Administrative Templates (Computer) (233), 19 Administrative Templates (User) (11). Sections 3, 4, 6, 7, 8, 10–16 are intentionally blank (structure placeholders).
- **Assessment status:** every recommendation is Automated (technical control fully automatable to pass/fail) except two Manual items: 1.2.3 'Allow Administrator account lockout' and 2.3.11.6 'Network security: Force logoff when logon hours expire'.

## Profiles and applicability

Six profiles; ~30 recommendations are DC-only and ~26 MS-only (tagged in the title as (DC only) / (MS only)):

- **Level 1 - Domain Controller** / **Level 1 - Member Server** — practical and prudent; clear security benefit; does not inhibit utility beyond acceptable means. Member Server profile also covers servers with roles: AD Certificate Services, DHCP Server, DNS Server, File Server, Hyper-V, Network Policy and Access Services, Print Server, Remote Access Services, Remote Desktop Services, Web Server.
- **Level 2 - Domain Controller** / **Level 2 - Member Server** — extends the matching Level 1 profile (not standalone); items where security is paramount, act as defense in depth, or may negatively inhibit utility or performance (e.g. 2.3.7.1 CTRL+ALT+DEL required, 2.3.7.6 cached logons ≤ 4 on MS, 5.2 Print Spooler disabled on MS, LLTDIO/RSPNDR disabled).
- **Next Generation Windows Security - Domain Controller** / **- Member Server** — optional add-on to L1 or L2; advanced features with configuration dependencies requiring testing (VBS/Credential Guard 18.9.5.x, LSASS protected process 18.9.27.2).
- DC/MS variants of the same control differ by group membership, e.g. 'Access this computer from the network' = Administrators, Authenticated Users, ENTERPRISE DOMAIN CONTROLLERS (2.2.2, DC only) vs Administrators, Authenticated Users (2.2.3, MS only); Credential Guard enabled with UEFI lock on MS (18.9.5.5) but disabled on DCs (18.9.5.6 — enabling it on domain controllers is not supported).

## Section outline

| Section | Contents |
|---|---|
| 1 Account Policies | Password policy (7), account lockout policy (4) |
| 2 Local Policies | Audit Policy heading, User Rights Assignment (48), Security Options (70, incl. UAC, NTLM/Kerberos, network access) |
| 3 Event Log | Intentionally blank — no event log size recommendations in this benchmark |
| 4 Restricted Groups | Intentionally blank |
| 5 System Services | Print Spooler (Spooler) disabled (DC only / MS only variants) |
| 6 Registry / 7 File System | Intentionally blank |
| 9 Windows Defender Firewall with Advanced Security | Domain Profile (7), Private Profile (7), Public Profile (9) |
| 17 Advanced Audit Policy Configuration | 34 subcategory settings across Account Logon, Account Management, Detailed Tracking, DS Access, Logon/Logoff, Object Access, Policy Change, Privilege Use, System |
| 18 Administrative Templates (Computer) | MS Security Guide, MSS (Legacy), Network, Printers, System (Device Guard, LAPS, LSA, Windows Time Service), Windows Components (Defender, AutoPlay, SmartScreen, Windows Update), Custom Settings |
| 19 Administrative Templates (User) | Notifications, System, Windows Spotlight, shared files within profile |

## Password and lockout policy (1.1, 1.2)

| Control | Recommended state |
|---|---|
| 1.1.1 Enforce password history | 24 or more password(s) |
| 1.1.2 Maximum password age | 365 or fewer days, but not 0 |
| 1.1.3 Minimum password age | 1 or more day(s) |
| 1.1.4 Minimum password length | 14 or more character(s) |
| 1.1.5 Password must meet complexity requirements | Enabled |
| 1.1.6 Relax minimum password length limits | Enabled |
| 1.1.7 Store passwords using reversible encryption | Disabled |
| 1.2.1 Account lockout duration | 15 or more minute(s) |
| 1.2.2 Account lockout threshold | 5 or fewer invalid logon attempt(s), but not 0 |
| 1.2.3 Allow Administrator account lockout | Enabled (MS only, Manual) |
| 1.2.4 Reset account lockout counter after | 15 or more minute(s) |

Application note from the benchmark: Password Policy (1.1) and Account Lockout Policy (1.2) settings must be applied via the **Default Domain Policy** GPO to be globally in effect on domain user accounts; configured in any other GPO they only affect local user accounts on receiving computers. Per-user/group exceptions use Password Settings Objects (PSOs), configured most easily in Active Directory Administrative Center. Microsoft's maximum for saved password history is 24. UI path pattern: `Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\...`.

## User rights assignment (2.2) — representative controls

| Recommendation | Setting |
|---|---|
| 2.2.1 Access Credential Manager as a trusted caller | No One |
| 2.2.2 / 2.2.3 Access this computer from the network | Administrators, Authenticated Users, ENTERPRISE DOMAIN CONTROLLERS (DC only) / Administrators, Authenticated Users (MS only) |
| 2.2.4 Act as part of the operating system | No One |
| 2.2.7 / 2.2.8 Allow log on locally | Administrators, ENTERPRISE DOMAIN CONTROLLERS (DC only) / Administrators (MS only) |
| 2.2.9 / 2.2.10 Allow log on through Remote Desktop Services | Administrators (DC only) / Administrators, Remote Desktop Users (MS only) |
| 2.2.14 Create a token object | No One |
| 2.2.17 / 2.2.18 Create symbolic links | Administrators (DC only) / Administrators, NT VIRTUAL MACHINE\Virtual Machines (MS only) |
| 2.2.19 Debug programs | Administrators |
| 2.2.20 / 2.2.21 Deny access to this computer from the network | include Guests (DC only) / include Guests, Local account and member of Administrators group (MS only) |
| 2.2.26 Deny log on through Remote Desktop Services | Guests, Local account (MS only) |
| 2.2.27 / 2.2.28 Enable computer and user accounts to be trusted for delegation | Administrators (DC only) / No One (MS only) |
| 2.2.35 Lock pages in memory | No One |
| 2.2.36 Log on as a batch job | Administrators (L2 DC only) |
| 2.2.47 Synchronize directory service data | No One (DC only) |
| 2.2.48 Take ownership of files or other objects | Administrators |

## Security options highlights (2.3)

- **Accounts:** Guest account status Disabled (MS only); blank passwords limited to console logon only Enabled; rename administrator and guest accounts.
- **Audit:** Force audit policy subcategory settings (Vista or later) to override category settings Enabled (prerequisite for 17.x); shut down system immediately if unable to log security audits Disabled.
- **Domain controller (DC only):** LDAP server channel binding token requirements Always; LDAP server signing requirements Require signing; refuse machine account password changes Disabled.
- **Domain member:** digitally encrypt or sign secure channel data (always) Enabled; maximum machine account password age ≤ 30 days, not 0; require strong (Windows 2000 or later) session key Enabled.
- **Interactive logon:** do not require CTRL+ALT+DEL Disabled (L2); don't display last signed-in Enabled; machine inactivity limit ≤ 900 seconds, not 0; cached logons ≤ 4 (MS only, L2); prompt user to change password before expiration 5–14 days; configure legal notice message text/title.
- **Network access:** anonymous SID/Name translation Disabled; remotely accessible registry paths configured; shares that can be accessed anonymously None; restrict clients allowed to make remote calls to SAM = Administrators: Remote Access: Allow (MS only); sharing and security model for local accounts = Classic - local users authenticate as themselves.
- **Network security:** Kerberos encryption types = AES128_HMAC_SHA1, AES256_HMAC_SHA1, Future encryption types; do not store LAN Manager hash value on next password change Enabled; LAN Manager authentication level = Send NTLMv2 response only. Refuse LM & NTLM; NTLM SSP client/server minimum session security = Require NTLMv2 session security, Require 128-bit encryption; Restrict NTLM: audit incoming NTLM traffic = Enable auditing for all accounts, audit NTLM authentication in this domain = Enable all (DC only), outgoing NTLM traffic = Audit all or higher.
- **User Account Control:** Admin Approval Mode for the Built-in Administrator Enabled; elevation prompt for administrators = Prompt for consent on the secure desktop or higher; standard users = Automatically deny elevation requests; run all administrators in Admin Approval Mode Enabled; switch to secure desktop for elevation prompts Enabled.

## Advanced audit policy (17)

Configure via `Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\...`; the benchmark also gives auditpol.exe audit checks, e.g. for 17.5.4 Audit Logon: `auditpol /get /subcategory:"{0cce9215-69ae-11d9-bed3-505054503030}"`.

| Subcategory | Recommended state |
|---|---|
| 17.1.1 Audit Credential Validation | Success and Failure |
| 17.1.2 / 17.1.3 Audit Kerberos Authentication Service / Service Ticket Operations | Success and Failure (DC only) |
| 17.2.2 Audit Computer Account Management | include Success (DC only) |
| 17.2.6 Audit User Account Management | Success and Failure |
| 17.3.2 Audit Process Creation | include Success (pair with 18.9.3.1 Include command line in process creation events Enabled) |
| 17.4.1 / 17.4.2 Audit Directory Service Access / Changes | include Failure / Success (DC only) |
| 17.5.1 Audit Account Lockout | include Failure |
| 17.5.3 / 17.5.4 Audit Logoff / Logon | include Success / Success and Failure |
| 17.6.1 / 17.6.2 Audit Detailed File Share / File Share | include Failure / Success and Failure |
| 17.6.4 Audit Removable Storage | Success and Failure |
| 17.7.4 Audit MPSSVC Rule-Level Policy Change | Success and Failure |
| 17.8.1 Audit Sensitive Privilege Use | Success |
| 17.9.5 Audit System Integrity | Success and Failure |

## Windows Defender Firewall profiles (9)

Applied per profile (Domain 9.1, Private 9.2, Public 9.3); renamed from "Windows Firewall" starting with Server 2019:

- Firewall state **On (recommended)**; inbound connections **Block (default)**; display a notification **No**.
- Logging: Name configured to `%SystemRoot%\System32\logfiles\firewall\pfirewall.log`; Size limit (KB) **16,384 KB or greater**; log dropped packets **Yes**; log successful connections **Yes**.
- Public profile additionally: Apply local firewall rules **No**; Apply local connection security rules **No**.
- Registry backing example: `HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile:EnableFirewall` (REG_DWORD 1).

## Services and printing (5, 18.7)

- 5.1 / 5.2 Ensure 'Print Spooler (Spooler)' is set to 'Disabled' — Level 1 - Domain Controller (DC only) and Level 2 - Member Server (MS only); mitigates PrintNightmare (CVE-2021-34527). Backed by `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Spooler:Start` (REG_DWORD 4); GPO path `Computer Configuration\Policies\Windows Settings\Security Settings\System Services\Print Spooler`; default Automatic. DCs cannot prune published printers from AD or act as print servers.
- 18.7.1 'Allow Print Spooler to accept client connections' Disabled; 18.7.2 Configure Redirection Guard Enabled; RPC over TCP for outgoing/incoming RPC with packet-level privacy; 18.7.9 'Limits print driver installation to Administrators' Enabled; Point and Print Restrictions show warning and elevation prompt.

## Microsoft Defender Antivirus and Exploit Guard (18.10.42)

- EDR in block mode Enabled; Join Microsoft MAPS = Enabled: Advanced (local setting override for MAPS Disabled); convert warn verdict to block Enabled; enable file hash computation feature Enabled.
- Real-time protection: scan all downloaded files and attachments Enabled; turn off real-time protection Disabled; behavior monitoring Enabled; script scanning Enabled. Scans: packed executables Enabled, removable drives Enabled, e-mail scanning Enabled, trigger quick scan after 7 days without scans, scan excluded files/directories during quick scans Enabled.
- PUA detection = Enabled: Block; exclusions visible to local users Enabled.
- **Attack Surface Reduction (18.10.42.6.1.1/.2):** Configure ASR rules Enabled with each rule set to 1 (block), including `9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2` (block credential stealing from lsass.exe), `56a863a9-875e-4185-98a7-b882c64b5ce5` (abuse of exploited vulnerable signed drivers), `d4f940ab-401b-4efc-aadc-ad5f3c50688a` (Office applications creating child processes), `3b576869-a4ec-4529-8536-b80a7769e899` (Office executable content), `5beb7efe-fd9a-4556-801d-275e5ffc04cc` (obfuscated scripts), `be9ba2d9-53ea-4cdc-84e5-9b1eeee46550` (executable content from email/webmail), `b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4` (untrusted/unsigned processes from USB), `e6db77e5-3df2-4cf1-b95a-636979351e5b` (WMI event subscription persistence) — full set is the 13 rules listed in 18.10.42.6.1.2. Backed by `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules:<rule-GUID>` (REG_SZ 1).
- Network Protection: 'Prevent users and apps from accessing dangerous websites' = Enabled: Block.

## Device Guard / Next Generation (18.9.5, 18.9.27)

- Turn On Virtualization Based Security Enabled; Select Platform Security Level = Secure Boot or higher; Virtualization Based Protection of Code Integrity = Enabled with UEFI lock; Require UEFI Memory Attributes Table True; Secure Launch Configuration Enabled. Requires 64-bit Windows with Secure Boot/UEFI (not Legacy BIOS); Credential Guard and Device Guard not currently supported on Azure IaaS VMs; enabling Credential Guard on domain controllers is not supported (causes crashes).
- Credential Guard Configuration = Enabled with UEFI lock (Next Gen - Member Server) vs Disabled (Next Gen - Domain Controller).
- Local Security Authority: Allow custom SSPs and APs to be loaded into LSASS Disabled (DC only); Configures LSASS to run as a protected process = Enabled: Enabled with UEFI Lock.

## Windows LAPS (18.9.26)

Configure password backup directory = Enabled: Active Directory or Enabled: Azure Active Directory; password complexity = large+small letters+numbers+special characters or Passphrase; password length ≥ 15; password age ≤ 30 days; enable password encryption Enabled; do not allow password expiration longer than required by policy Enabled; post-authentication grace period ≤ 8 hours (not 0); post-authentication actions = reset the password and logoff the managed account or higher.

## Other high-signal computer policy

- **SMB (18.4, 18.6):** Configure SMB v1 client driver = Enabled: Disable driver (recommended); Configure SMB v1 server Disabled; Mandate the minimum version of SMB = Enabled: 3.1.1; enable insecure guest logons Disabled; Microsoft network server: Digitally sign communications (always) Enabled, idle time before suspending session ≤ 15 minutes, disconnect clients when logon hours expire Enabled.
- **UNC paths:** Hardened UNC Paths Enabled with Require Mutual Authentication, Require Integrity, and Require Privacy for all NETLOGON and SYSVOL shares (18.6.14.1).
- **Name resolution:** mDNS protocol Disabled; NetBIOS = Enabled: Disable NetBIOS name resolution on public networks; turn off multicast name resolution Enabled; NetBT NodeType = Enabled: P-node (recommended).
- **MSS (Legacy) 18.5:** AutoAdminLogon Disabled; IP source routing highest protection (IPv4 and IPv6); ICMP redirects Disabled; TcpMaxDataRetransmissions (IPv4/IPv6) = 3; WarningLevel = 90% or less (security event log warning threshold); SafeDllSearchMode Enabled.
- **Boot/hardware:** ELAM Boot-Start Driver Initialization Policy = Enabled: Good, unknown and bad but critical; Kernel DMA Protection enumeration policy = Enabled: Block All.
- **Windows Update (18.10.94):** Configure Automatic Updates Enabled (if feasible use 4 - Auto download and schedule the install; not a scored requirement); scheduled install day = 0 - Every day; manage preview builds Disabled; select when quality updates are received = Enabled: 0 days.
- **SmartScreen:** Configure Windows Defender SmartScreen = Enabled: Warn and prevent bypass (18.10.77.2.1).
- **AutoPlay:** disallow Autoplay for non-volume devices Enabled; default AutoRun behavior = Do not execute any autorun commands; turn off Autoplay = Enabled: All drives.
- **Remote assistance:** offer and solicited Remote Assistance both Disabled; Encryption Oracle Remediation = Enabled: Force Updated Clients.
- **User side (19):** prevent users from sharing files within their profile Enabled; turn off toast notifications on the lock screen Enabled; turn off all Windows Spotlight features Enabled.

## Related

- [[grc-frameworks/cis-benchmarks/cis-windows-11-enterprise]]
