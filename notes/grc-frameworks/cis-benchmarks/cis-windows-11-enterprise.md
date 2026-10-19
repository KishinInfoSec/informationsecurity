---
title: cis-windows-11-enterprise
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/windows, source/cis]
description: "CIS Windows 11 Enterprise Benchmark v5.0.0 checklist: account policy, user rights, audit, admin templates, with levels."
source_pdf: CIS_Microsoft_Windows_11_Enterprise_Benchmark_v5.0.0.pdf
---

# CIS Microsoft Windows 11 Enterprise Benchmark v5.0.0 (01-27-2026)

## Overview

- **Product:** Microsoft Windows 11 Enterprise (Group Policy / registry settings)
- **Benchmark version:** v5.0.0 (2026-01-27)
- **Profiles:** Level 1 (L1) baseline, Level 2 (L2) high-security, and a BitLocker (BL) add-on profile that can be combined with L1 or L2 (L1+BL, L2+BL).
- **Recommendations:** 560 total (558 Automated, 2 Manual)
- **Checklist legend:** level (L1/L2, BL) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Account Policies | 11 |
| 2 Local Policies | 100 |
| 3 Event Log | 0 |
| 4 Restricted Groups | 0 |
| 5 System Services | 44 |
| 6 Registry | 0 |
| 7 File System | 0 |
| 8 Wired Network (IEEE 802.3) Policies | 0 |
| 9 Windows Defender Firewall with Advanced Security (formerly Windows Firewall with Advanced Security) | 23 |
| 10 Network List Manager Policies | 0 |
| 11 Wireless Network (IEEE 802.11) Policies | 0 |
| 12 Public Key Policies | 0 |
| 13 Software Restriction Policies | 0 |
| 14 Network Access Protection NAP Client Configuration | 0 |
| 15 Application Control Policies | 0 |
| 16 IP Security Policies | 0 |
| 17 Advanced Audit Policy Configuration | 27 |
| 18 Administrative Templates (Computer) | 344 |
| 19 Administrative Templates (User) | 11 |

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Account Policies

#### 1.1 Password Policy

- [ ] 1.1.1 Ensure 'Enforce password history' is set to '24 or more password(s)' — L1 · Automated
- [ ] 1.1.2 Ensure 'Maximum password age' is set to '365 or fewer days, but not 0' — L1 · Automated
- [ ] 1.1.3 Ensure 'Minimum password age' is set to '1 or more day(s)' — L1 · Automated
- [ ] 1.1.4 Ensure 'Minimum password length' is set to '14 or more character(s)' — L1 · Automated
- [ ] 1.1.5 Ensure 'Password must meet complexity requirements' is set to 'Enabled' — L1 · Automated
- [ ] 1.1.6 Ensure 'Relax minimum password length limits' is set to 'Enabled' — L1 · Automated
- [ ] 1.1.7 Ensure 'Store passwords using reversible encryption' is set to 'Disabled' — L1 · Automated

#### 1.2 Account Lockout Policy

- [ ] 1.2.1 Ensure 'Account lockout duration' is set to '15 or more minute(s)' — L1 · Automated
- [ ] 1.2.2 Ensure 'Account lockout threshold' is set to '5 or fewer invalid logon attempt(s), but not 0' — L1 · Automated
- [ ] 1.2.3 Ensure 'Allow Administrator account lockout' is set to 'Enabled' — L1 · Manual
- [ ] 1.2.4 Ensure 'Reset account lockout counter after' is set to '15 or more minute(s)' — L1 · Automated

### 2 Local Policies

#### 2.2 User Rights Assignment

- [ ] 2.2.1 Ensure 'Access Credential Manager as a trusted caller' is set to 'No One' — L1 · Automated
- [ ] 2.2.2 Ensure 'Access this computer from the network' is set to 'Administrators, Remote Desktop Users' — L1 · Automated
- [ ] 2.2.3 Ensure 'Act as part of the operating system' is set to 'No One' — L1 · Automated
- [ ] 2.2.4 Ensure 'Adjust memory quotas for a process' is set to 'Administrators, LOCAL SERVICE, NETWORK SERVICE' — L1 · Automated
- [ ] 2.2.5 Ensure 'Allow log on locally' is set to 'Administrators, Users' — L1 · Automated
- [ ] 2.2.6 Ensure 'Allow log on through Remote Desktop Services' is set to 'Administrators, Remote Desktop Users' — L1 · Automated
- [ ] 2.2.7 Ensure 'Back up files and directories' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.8 Ensure 'Change the system time' is set to 'Administrators, LOCAL SERVICE' — L1 · Automated
- [ ] 2.2.9 Ensure 'Create a pagefile' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.10 Ensure 'Create a token object' is set to 'No One' — L1 · Automated
- [ ] 2.2.11 Ensure 'Create global objects' is set to 'Administrators, LOCAL SERVICE, NETWORK SERVICE, SERVICE' — L1 · Automated
- [ ] 2.2.12 Ensure 'Create permanent shared objects' is set to 'No One' — L1 · Automated
- [ ] 2.2.13 Ensure 'Create symbolic links' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.14 Ensure 'Debug programs' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.15 Ensure 'Deny access to this computer from the network' to include 'Guests, Local account' — L1 · Automated
- [ ] 2.2.16 Ensure 'Deny log on as a batch job' to include 'Guests' — L1 · Automated
- [ ] 2.2.17 Ensure 'Deny log on as a service' to include 'Guests' — L1 · Automated
- [ ] 2.2.18 Ensure 'Deny log on locally' to include 'Guests' — L1 · Automated
- [ ] 2.2.19 Ensure 'Deny log on through Remote Desktop Services' to include 'Guests, Local account' — L1 · Automated
- [ ] 2.2.20 Ensure 'Enable computer and user accounts to be trusted for delegation' is set to 'No One' — L1 · Automated
- [ ] 2.2.21 Ensure 'Force shutdown from a remote system' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.22 Ensure 'Generate security audits' is set to 'LOCAL SERVICE, NETWORK SERVICE, RESTRICTED SERVICES\PrintSpoolerService' — L1 · Automated
- [ ] 2.2.23 Ensure 'Impersonate a client after authentication' is set to 'Administrators, LOCAL SERVICE, NETWORK SERVICE, SERVICE, RESTRICTED SERVICES\PrintSpoolerService' — L1 · Automated
- [ ] 2.2.24 Ensure 'Increase scheduling priority' is set to 'Administrators, Window Manager\Window Manager Group' — L1 · Automated
- [ ] 2.2.25 Ensure 'Load and unload device drivers' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.26 Ensure 'Lock pages in memory' is set to 'No One' — L1 · Automated
- [ ] 2.2.27 Ensure 'Log on as a batch job' is set to 'Administrators' — L2 · Automated
- [ ] 2.2.28 Ensure 'Log on as a service' is set to 'No One' — L2 · Automated
- [ ] 2.2.29 Ensure 'Manage auditing and security log' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.30 Ensure 'Modify an object label' is set to 'No One' — L1 · Automated
- [ ] 2.2.31 Ensure 'Modify firmware environment values' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.32 Ensure 'Perform volume maintenance tasks' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.33 Ensure 'Profile single process' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.34 Ensure 'Profile system performance' is set to 'Administrators, NT SERVICE\WdiServiceHost' — L1 · Automated
- [ ] 2.2.35 Ensure 'Replace a process level token' is set to 'LOCAL SERVICE, NETWORK SERVICE' — L1 · Automated
- [ ] 2.2.36 Ensure 'Restore files and directories' is set to 'Administrators' — L1 · Automated
- [ ] 2.2.37 Ensure 'Shut down the system' is set to 'Administrators, Users' — L1 · Automated
- [ ] 2.2.38 Ensure 'Take ownership of files or other objects' is set to 'Administrators' — L1 · Automated

#### 2.3 Security Options

**2.3.1 Accounts**

- [ ] 2.3.1.1 Ensure 'Accounts: Guest account status' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.1.2 Ensure 'Accounts: Limit local account use of blank passwords to console logon only' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.1.3 Configure 'Accounts: Rename administrator account' — L1 · Automated
- [ ] 2.3.1.4 Configure 'Accounts: Rename guest account' — L1 · Automated

**2.3.2 Audit**

- [ ] 2.3.2.1 Ensure 'Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.2.2 Ensure 'Audit: Shut down system immediately if unable to log security audits' is set to 'Disabled' — L1 · Automated

**2.3.4 Devices**

- [ ] 2.3.4.1 Ensure 'Devices: Prevent users from installing printer drivers' is set to 'Enabled' — L2 · Automated

**2.3.6 Domain member**

- [ ] 2.3.6.1 Ensure 'Domain member: Digitally encrypt or sign secure channel data (always)' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.6.2 Ensure 'Domain member: Digitally encrypt secure channel data (when possible)' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.6.3 Ensure 'Domain member: Digitally sign secure channel data (when possible)' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.6.4 Ensure 'Domain member: Disable machine account password changes' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.6.5 Ensure 'Domain member: Maximum machine account password age' is set to '30 or fewer days, but not 0' — L1 · Automated
- [ ] 2.3.6.6 Ensure 'Domain member: Require strong (Windows 2000 or later) session key' is set to 'Enabled' — L1 · Automated

**2.3.7 Interactive logon**

- [ ] 2.3.7.1 Ensure 'Interactive logon: Do not require CTRL+ALT+DEL' is set to 'Disabled' — L2 · Automated
- [ ] 2.3.7.2 Ensure 'Interactive logon: Don't display last signed-in' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.7.3 Ensure 'Interactive logon: Machine inactivity limit' is set to '900 or fewer second(s), but not 0' — L1 · Automated
- [ ] 2.3.7.4 Configure 'Interactive logon: Message text for users attempting to log on' — L1 · Automated
- [ ] 2.3.7.5 Configure 'Interactive logon: Message title for users attempting to log on' — L1 · Automated
- [ ] 2.3.7.6 Ensure 'Interactive logon: Number of previous logons to cache (in case domain controller is not available)' is set to '4 or fewer logon(s)' — L2 · Automated
- [ ] 2.3.7.7 Ensure 'Interactive logon: Prompt user to change password before expiration' is set to 'between 5 and 14 days' — L1 · Automated
- [ ] 2.3.7.8 Ensure 'Interactive logon: Smart card removal behavior' is set to 'Lock Workstation' or higher — L1 · Automated

**2.3.8 Microsoft network client**

- [ ] 2.3.8.1 Ensure 'Microsoft network client: Digitally sign communications (always)' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.8.2 Ensure 'Microsoft network client: Send unencrypted password to third-party SMB servers' is set to 'Disabled' — L1 · Automated

**2.3.9 Microsoft network server**

- [ ] 2.3.9.1 Ensure 'Microsoft network server: Amount of idle time required before suspending session' is set to '15 or fewer minute(s)' — L1 · Automated
- [ ] 2.3.9.2 Ensure 'Microsoft network server: Digitally sign communications (always)' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.9.3 Ensure 'Microsoft network server: Disconnect clients when logon hours expire' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.9.4 Ensure 'Microsoft network server: Server SPN target name validation level' is set to 'Accept if provided by client' or higher — L1 · Automated

**2.3.10 Network access**

- [ ] 2.3.10.1 Ensure 'Network access: Allow anonymous SID/Name translation' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.10.2 Ensure 'Network access: Do not allow anonymous enumeration of SAM accounts' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.10.3 Ensure 'Network access: Do not allow anonymous enumeration of SAM accounts and shares' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.10.4 Ensure 'Network access: Do not allow storage of passwords and credentials for network authentication' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.10.5 Ensure 'Network access: Let Everyone permissions apply to anonymous users' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.10.6 Ensure 'Network access: Named Pipes that can be accessed anonymously' is set to 'None' — L1 · Automated
- [ ] 2.3.10.7 Ensure 'Network access: Remotely accessible registry paths' is configured — L1 · Automated
- [ ] 2.3.10.8 Ensure 'Network access: Remotely accessible registry paths and sub-paths' is configured — L1 · Automated
- [ ] 2.3.10.9 Ensure 'Network access: Restrict anonymous access to Named Pipes and Shares' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.10.10 Ensure 'Network access: Restrict clients allowed to make remote calls to SAM' is set to 'Administrators: Remote Access: Allow' — L1 · Automated
- [ ] 2.3.10.11 Ensure 'Network access: Shares that can be accessed anonymously' is set to 'None' — L1 · Automated
- [ ] 2.3.10.12 Ensure 'Network access: Sharing and security model for local accounts' is set to 'Classic - local users authenticate as themselves' — L1 · Automated

**2.3.11 Network security**

- [ ] 2.3.11.1 Ensure 'Network security: Allow Local System to use computer identity for NTLM' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.11.2 Ensure 'Network security: Allow LocalSystem NULL session fallback' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.11.3 Ensure 'Network Security: Allow PKU2U authentication requests to this computer to use online identities' is set to 'Disabled' — L1 · Automated
- [ ] 2.3.11.4 Ensure 'Network security: Configure encryption types allowed for Kerberos' is set to 'AES128_HMAC_SHA1, AES256_HMAC_SHA1, Future encryption types' — L1 · Automated
- [ ] 2.3.11.5 Ensure 'Network security: Force logoff when logon hours expire' is set to 'Enabled' — L1 · Manual
- [ ] 2.3.11.6 Ensure 'Network security: LAN Manager authentication level' is set to 'Send NTLMv2 response only. Refuse LM & NTLM' — L1 · Automated
- [ ] 2.3.11.7 Ensure 'Network security: LDAP client encryption requirements' is set to 'Negotiate sealing' or higher — L1 · Automated
- [ ] 2.3.11.8 Ensure 'Network security: LDAP client signing requirements' is set to 'Negotiate signing' or higher — L1 · Automated
- [ ] 2.3.11.9 Ensure 'Network security: Minimum session security for NTLM SSP based (including secure RPC) clients' is set to 'Require NTLMv2 session security, Require 128-bit encryption' — L1 · Automated
- [ ] 2.3.11.10 Ensure 'Network security: Minimum session security for NTLM SSP based (including secure RPC) servers' is set to 'Require NTLMv2 session security, Require 128-bit encryption' — L1 · Automated
- [ ] 2.3.11.11 Ensure 'Network security: Restrict NTLM: Audit Incoming NTLM Traffic' is set to 'Enable auditing for all accounts' — L1 · Automated
- [ ] 2.3.11.12 Ensure 'Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers' is set to 'Audit all' or higher — L1 · Automated

**2.3.14 System cryptography**

- [ ] 2.3.14.1 Ensure 'System cryptography: Force strong key protection for user keys stored on the computer' is set to 'User is prompted when the key is first used' or higher — L2 · Automated

**2.3.15 System objects**

- [ ] 2.3.15.1 Ensure 'System objects: Require case insensitivity for non-Windows subsystems' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.15.2 Ensure 'System objects: Strengthen default permissions of internal system objects (e.g. Symbolic Links)' is set to 'Enabled' — L1 · Automated

**2.3.17 User Account Control**

- [ ] 2.3.17.1 Ensure 'User Account Control: Admin Approval Mode for the Built-in Administrator account' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.17.2 Ensure 'User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode' is set to 'Prompt for consent on the secure desktop' or higher — L1 · Automated
- [ ] 2.3.17.3 Ensure 'User Account Control: Behavior of the elevation prompt for standard users' is set to 'Automatically deny elevation requests' — L1 · Automated
- [ ] 2.3.17.4 Ensure 'User Account Control: Detect application installations and prompt for elevation' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.17.5 Ensure 'User Account Control: Only elevate UIAccess applications that are installed in secure locations' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.17.6 Ensure 'User Account Control: Run all administrators in Admin Approval Mode' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.17.7 Ensure 'User Account Control: Switch to the secure desktop when prompting for elevation' is set to 'Enabled' — L1 · Automated
- [ ] 2.3.17.8 Ensure 'User Account Control: Virtualize file and registry write failures to per-user locations' is set to 'Enabled' — L1 · Automated

### 5 System Services

- [ ] 5.1 Ensure 'Bluetooth Audio Gateway Service (BTAGService)' is set to 'Disabled' — L2 · Automated
- [ ] 5.2 Ensure 'Bluetooth Support Service (bthserv)' is set to 'Disabled' — L2 · Automated
- [ ] 5.3 Ensure 'Computer Browser (Browser)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.4 Ensure 'Downloaded Maps Manager (MapsBroker)' is set to 'Disabled' — L2 · Automated
- [ ] 5.5 Ensure 'GameInput Service (GameInputSvc)' is set to 'Disabled' — L2 · Automated
- [ ] 5.6 Ensure 'Geolocation Service (lfsvc)' is set to 'Disabled' — L2 · Automated
- [ ] 5.7 Ensure 'IIS Admin Service (IISADMIN)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.8 Ensure 'Infrared monitor service (irmon)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.9 Ensure 'Link-Layer Topology Discovery Mapper (lltdsvc)' is set to 'Disabled' — L2 · Automated
- [ ] 5.10 Ensure 'Microsoft FTP Service (FTPSVC)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.11 Ensure 'Microsoft iSCSI Initiator Service (MSiSCSI)' is set to 'Disabled' — L2 · Automated
- [ ] 5.12 Ensure 'OpenSSH SSH Server (sshd)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.13 Ensure 'Peer Name Resolution Protocol (PNRPsvc)' is set to 'Disabled' or 'Not Installed' — L2 · Automated
- [ ] 5.14 Ensure 'Peer Networking Grouping (p2psvc)' is set to 'Disabled' or 'Not Installed' — L2 · Automated
- [ ] 5.15 Ensure 'Peer Networking Identity Manager (p2pimsvc)' is set to 'Disabled' or 'Not Installed' — L2 · Automated
- [ ] 5.16 Ensure 'PNRP Machine Name Publication Service (PNRPAutoReg)' is set to 'Disabled' or 'Not Installed' — L2 · Automated
- [ ] 5.17 Ensure 'Print Spooler (Spooler)' is set to 'Disabled' — L2 · Automated
- [ ] 5.18 Ensure 'Problem Reports and Solutions Control Panel Support (wercplsupport)' is set to 'Disabled' — L2 · Automated
- [ ] 5.19 Ensure 'Remote Access Auto Connection Manager (RasAuto)' is set to 'Disabled' — L2 · Automated
- [ ] 5.20 Ensure 'Remote Desktop Configuration (SessionEnv)' is set to 'Disabled' — L2 · Automated
- [ ] 5.21 Ensure 'Remote Desktop Services (TermService)' is set to 'Disabled' — L2 · Automated
- [ ] 5.22 Ensure 'Remote Desktop Services UserMode Port Redirector (UmRdpService)' is set to 'Disabled' — L2 · Automated
- [ ] 5.23 Ensure 'Remote Procedure Call (RPC) Locator (RpcLocator)' is set to 'Disabled' — L1 · Automated
- [ ] 5.24 Ensure 'Remote Registry (RemoteRegistry)' is set to 'Disabled' — L2 · Automated
- [ ] 5.25 Ensure 'Routing and Remote Access (RemoteAccess)' is set to 'Disabled' — L1 · Automated
- [ ] 5.26 Ensure 'Server (LanmanServer)' is set to 'Disabled' — L2 · Automated
- [ ] 5.27 Ensure 'Simple TCP/IP Services (simptcp)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.28 Ensure 'SNMP Service (SNMP)' is set to 'Disabled' or 'Not Installed' — L2 · Automated
- [ ] 5.29 Ensure 'Special Administration Console Helper (sacsvr)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.30 Ensure 'SSDP Discovery (SSDPSRV)' is set to 'Disabled' — L1 · Automated
- [ ] 5.31 Ensure 'UPnP Device Host (upnphost)' is set to 'Disabled' — L1 · Automated
- [ ] 5.32 Ensure 'Web Management Service (WMSvc)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.33 Ensure 'Windows Error Reporting Service (WerSvc)' is set to 'Disabled' — L2 · Automated
- [ ] 5.34 Ensure 'Windows Event Collector (Wecsvc)' is set to 'Disabled' — L2 · Automated
- [ ] 5.35 Ensure 'Windows Media Player Network Sharing Service (WMPNetworkSvc)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.36 Ensure 'Windows Mobile Hotspot Service (icssvc)' is set to 'Disabled' — L1 · Automated
- [ ] 5.37 Ensure 'Windows Push Notifications System Service (WpnService)' is set to 'Disabled' — L2 · Automated
- [ ] 5.38 Ensure 'Windows PushToInstall Service (PushToInstall)' is set to 'Disabled' — L2 · Automated
- [ ] 5.39 Ensure 'Windows Remote Management (WS-Management) (WinRM)' is set to 'Disabled' — L2 · Automated
- [ ] 5.40 Ensure 'World Wide Web Publishing Service (W3SVC)' is set to 'Disabled' or 'Not Installed' — L1 · Automated
- [ ] 5.41 Ensure 'Xbox Accessory Management Service (XboxGipSvc)' is set to 'Disabled' — L1 · Automated
- [ ] 5.42 Ensure 'Xbox Live Auth Manager (XblAuthManager)' is set to 'Disabled' — L1 · Automated
- [ ] 5.43 Ensure 'Xbox Live Game Save (XblGameSave)' is set to 'Disabled' — L1 · Automated
- [ ] 5.44 Ensure 'Xbox Live Networking Service (XboxNetApiSvc)' is set to 'Disabled' — L1 · Automated

### 9 Windows Defender Firewall with Advanced Security (formerly Windows Firewall with Advanced Security)

#### 9.1 Domain Profile

- [ ] 9.1.1 Ensure 'Windows Firewall: Domain: Firewall state' is set to 'On (recommended)' — L1 · Automated
- [ ] 9.1.2 Ensure 'Windows Firewall: Domain: Inbound connections' is set to 'Block (default)' — L1 · Automated
- [ ] 9.1.3 Ensure 'Windows Firewall: Domain: Settings: Display a notification' is set to 'No' — L1 · Automated
- [ ] 9.1.4 Ensure 'Windows Firewall: Domain: Logging: Name' is configured — L1 · Automated
- [ ] 9.1.5 Ensure 'Windows Firewall: Domain: Logging: Size limit (KB)' is set to '16,384 KB or greater' — L1 · Automated
- [ ] 9.1.6 Ensure 'Windows Firewall: Domain: Logging: Log dropped packets' is set to 'Yes' — L1 · Automated
- [ ] 9.1.7 Ensure 'Windows Firewall: Domain: Logging: Log successful connections' is set to 'Yes' — L1 · Automated

#### 9.2 Private Profile

- [ ] 9.2.1 Ensure 'Windows Firewall: Private: Firewall state' is set to 'On (recommended)' — L1 · Automated
- [ ] 9.2.2 Ensure 'Windows Firewall: Private: Inbound connections' is set to 'Block (default)' — L1 · Automated
- [ ] 9.2.3 Ensure 'Windows Firewall: Private: Settings: Display a notification' is set to 'No' — L1 · Automated
- [ ] 9.2.4 Ensure 'Windows Firewall: Private: Logging: Name' is configured — L1 · Automated
- [ ] 9.2.5 Ensure 'Windows Firewall: Private: Logging: Size limit (KB)' is set to '16,384 KB or greater' — L1 · Automated
- [ ] 9.2.6 Ensure 'Windows Firewall: Private: Logging: Log dropped packets' is set to 'Yes' — L1 · Automated
- [ ] 9.2.7 Ensure 'Windows Firewall: Private: Logging: Log successful connections' is set to 'Yes' — L1 · Automated

#### 9.3 Public Profile

- [ ] 9.3.1 Ensure 'Windows Firewall: Public: Firewall state' is set to 'On (recommended)' — L1 · Automated
- [ ] 9.3.2 Ensure 'Windows Firewall: Public: Inbound connections' is set to 'Block (default)' — L1 · Automated
- [ ] 9.3.3 Ensure 'Windows Firewall: Public: Settings: Display a notification' is set to 'No' — L1 · Automated
- [ ] 9.3.4 Ensure 'Windows Firewall: Public: Settings: Apply local firewall rules' is set to 'No' — L1 · Automated
- [ ] 9.3.5 Ensure 'Windows Firewall: Public: Settings: Apply local connection security rules' is set to 'No' — L1 · Automated
- [ ] 9.3.6 Ensure 'Windows Firewall: Public: Logging: Name' is configured — L1 · Automated
- [ ] 9.3.7 Ensure 'Windows Firewall: Public: Logging: Size limit (KB)' is set to '16,384 KB or greater' — L1 · Automated
- [ ] 9.3.8 Ensure 'Windows Firewall: Public: Logging: Log dropped packets' is set to 'Yes' — L1 · Automated
- [ ] 9.3.9 Ensure 'Windows Firewall: Public: Logging: Log successful connections' is set to 'Yes' — L1 · Automated

### 17 Advanced Audit Policy Configuration

#### 17.1 Account Logon

- [ ] 17.1.1 Ensure 'Audit Credential Validation' is set to 'Success and Failure' — L1 · Automated

#### 17.2 Account Management

- [ ] 17.2.1 Ensure 'Audit Application Group Management' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.2.2 Ensure 'Audit Security Group Management' is set to include 'Success' — L1 · Automated
- [ ] 17.2.3 Ensure 'Audit User Account Management' is set to 'Success and Failure' — L1 · Automated

#### 17.3 Detailed Tracking

- [ ] 17.3.1 Ensure 'Audit PNP Activity' is set to include 'Success' — L1 · Automated
- [ ] 17.3.2 Ensure 'Audit Process Creation' is set to include 'Success' — L1 · Automated

#### 17.5 Logon/Logoff

- [ ] 17.5.1 Ensure 'Audit Account Lockout' is set to include 'Failure' — L1 · Automated
- [ ] 17.5.2 Ensure 'Audit Group Membership' is set to include 'Success' — L1 · Automated
- [ ] 17.5.3 Ensure 'Audit Logoff' is set to include 'Success' — L1 · Automated
- [ ] 17.5.4 Ensure 'Audit Logon' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.5.5 Ensure 'Audit Other Logon/Logoff Events' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.5.6 Ensure 'Audit Special Logon' is set to include 'Success' — L1 · Automated

#### 17.6 Object Access

- [ ] 17.6.1 Ensure 'Audit Detailed File Share' is set to include 'Failure' — L1 · Automated
- [ ] 17.6.2 Ensure 'Audit File Share' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.6.3 Ensure 'Audit Other Object Access Events' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.6.4 Ensure 'Audit Removable Storage' is set to 'Success and Failure' — L1 · Automated

#### 17.7 Policy Change

- [ ] 17.7.1 Ensure 'Audit Audit Policy Change' is set to include 'Success' — L1 · Automated
- [ ] 17.7.2 Ensure 'Audit Authentication Policy Change' is set to include 'Success' — L1 · Automated
- [ ] 17.7.3 Ensure 'Audit Authorization Policy Change' is set to include 'Success' — L1 · Automated
- [ ] 17.7.4 Ensure 'Audit MPSSVC Rule-Level Policy Change' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.7.5 Ensure 'Audit Other Policy Change Events' is set to include 'Failure' — L1 · Automated

#### 17.8 Privilege Use

- [ ] 17.8.1 Ensure 'Audit Sensitive Privilege Use' is set to 'Success' — L1 · Automated

#### 17.9 System

- [ ] 17.9.1 Ensure 'Audit IPsec Driver' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.9.2 Ensure 'Audit Other System Events' is set to 'Success and Failure' — L1 · Automated
- [ ] 17.9.3 Ensure 'Audit Security State Change' is set to include 'Success' — L1 · Automated
- [ ] 17.9.4 Ensure 'Audit Security System Extension' is set to include 'Success' — L1 · Automated
- [ ] 17.9.5 Ensure 'Audit System Integrity' is set to 'Success and Failure' — L1 · Automated

### 18 Administrative Templates (Computer)

#### 18.1 Control Panel

**18.1.1 Personalization**

- [ ] 18.1.1.1 Ensure 'Prevent enabling lock screen camera' is set to 'Enabled' — L1 · Automated
- [ ] 18.1.1.2 Ensure 'Prevent enabling lock screen slide show' is set to 'Enabled' — L1 · Automated

**18.1.2 Regional and Language Options**

- [ ] 18.1.2.2 Ensure 'Allow users to enable online speech recognition services' is set to 'Disabled' — L1 · Automated
- [ ] 18.1.3 Ensure 'Allow Online Tips' is set to 'Disabled' — L2 · Automated

#### 18.4 MS Security Guide

- [ ] 18.4.1 Ensure 'Apply UAC restrictions to local accounts on network logons' is set to 'Enabled' — L1 · Automated
- [ ] 18.4.2 Ensure 'Configure SMB v1 client driver' is set to 'Enabled: Disable driver (recommended)' — L1 · Automated
- [ ] 18.4.3 Ensure 'Configure SMB v1 server' is set to 'Disabled' — L1 · Automated
- [ ] 18.4.4 Ensure 'Enable Certificate Padding' is set to 'Enabled' — L1 · Automated
- [ ] 18.4.5 Ensure 'Enable Structured Exception Handling Overwrite Protection (SEHOP)' is set to 'Enabled' — L1 · Automated
- [ ] 18.4.6 Ensure 'NetBT NodeType configuration' is set to 'Enabled: P-node (recommended)' — L1 · Automated
- [ ] 18.4.7 Ensure 'WDigest Authentication' is set to 'Disabled' — L1 · Automated

#### 18.5 MSS (Legacy)

- [ ] 18.5.1 Ensure 'MSS: (AutoAdminLogon) Enable Automatic Logon' is set to 'Disabled' — L1 · Automated
- [ ] 18.5.2 Ensure 'MSS: (DisableIPSourceRouting IPv6) IP source routing protection level' is set to 'Enabled: Highest protection, source routing is completely disabled' — L1 · Automated
- [ ] 18.5.3 Ensure 'MSS: (DisableIPSourceRouting) IP source routing protection level' is set to 'Enabled: Highest protection, source routing is completely disabled' — L1 · Automated
- [ ] 18.5.4 Ensure 'MSS: (DisableSavePassword) Prevent the dial-up password from being saved' is set to 'Enabled' — L2 · Automated
- [ ] 18.5.5 Ensure 'MSS: (EnableICMPRedirect) Allow ICMP redirects to override OSPF generated routes' is set to 'Disabled' — L1 · Automated
- [ ] 18.5.6 Ensure 'MSS: (KeepAliveTime) How often keep-alive packets are sent in milliseconds' is set to 'Enabled: 300,000 or 5 minutes' — L2 · Automated
- [ ] 18.5.7 Ensure 'MSS: (NoNameReleaseOnDemand) Allow the computer to ignore NetBIOS name release requests except from WINS servers' is set to 'Enabled' — L1 · Automated
- [ ] 18.5.8 Ensure 'MSS: (PerformRouterDiscovery) Allow IRDP to detect and configure Default Gateway addresses' is set to 'Disabled' — L2 · Automated
- [ ] 18.5.9 Ensure 'MSS: (SafeDllSearchMode) Enable Safe DLL search mode' is set to 'Enabled' — L1 · Automated
- [ ] 18.5.10 Ensure 'MSS: (TcpMaxDataRetransmissions IPv6) How many times unacknowledged data is retransmitted' is set to 'Enabled: 3' — L2 · Automated
- [ ] 18.5.11 Ensure 'MSS: (TcpMaxDataRetransmissions) How many times unacknowledged data is retransmitted' is set to 'Enabled: 3' — L2 · Automated
- [ ] 18.5.12 Ensure 'MSS: (WarningLevel) Percentage threshold for the security event log at which the system will generate a warning' is set to 'Enabled: 90% or less' — L1 · Automated

#### 18.6 Network

**18.6.4 DNS Client**

- [ ] 18.6.4.1 Ensure 'Configure multicast DNS (mDNS) protocol' is set to 'Disabled' — L1 · Automated
- [ ] 18.6.4.2 Ensure 'Configure NetBIOS settings' is set to 'Enabled: Disable NetBIOS name resolution on public networks' — L1 · Automated
- [ ] 18.6.4.3 Ensure 'Turn off default IPv6 DNS Servers' is set to 'Enabled' — L2 · Automated
- [ ] 18.6.4.4 Ensure 'Turn off multicast name resolution' is set to 'Enabled' — L1 · Automated

**18.6.5 Fonts**

- [ ] 18.6.5.1 Ensure 'Enable Font Providers' is set to 'Disabled' — L2 · Automated

**18.6.7 Lanman Server**

- [ ] 18.6.7.1 Ensure 'Audit client does not support encryption' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.7.2 Ensure 'Audit client does not support signing' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.7.3 Ensure 'Audit insecure guest logon' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.7.4 Ensure 'Enable authentication rate limiter' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.7.5 Ensure 'Enable remote mailslots' is set to 'Disabled' — L1 · Automated
- [ ] 18.6.7.6 Ensure 'Mandate the minimum version of SMB' is set to 'Enabled: 3.1.1' — L1 · Automated
- [ ] 18.6.7.7 Ensure 'Set authentication rate limiter delay (milliseconds)' is set to 'Enabled: 2000' or more — L1 · Automated

**18.6.8 Lanman Workstation**

- [ ] 18.6.8.1 Ensure 'Audit insecure guest logon' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.8.2 Ensure 'Audit server does not support encryption' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.8.3 Ensure 'Audit server does not support signing' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.8.4 Ensure 'Enable insecure guest logons' is set to 'Disabled' — L1 · Automated
- [ ] 18.6.8.5 Ensure 'Enable remote mailslots' is set to 'Disabled' — L1 · Automated
- [ ] 18.6.8.6 Ensure 'Mandate the minimum version of SMB' is set to 'Enabled: 3.1.1' — L1 · Automated
- [ ] 18.6.8.7 Ensure 'Require Encryption' is set to 'Enabled' — L1 · Automated

**18.6.9 Link-Layer Topology Discovery**

- [ ] 18.6.9.1 Ensure 'Turn on Mapper I/O (LLTDIO) driver' is set to 'Disabled' — L2 · Automated
- [ ] 18.6.9.2 Ensure 'Turn on Responder (RSPNDR) driver' is set to 'Disabled' — L2 · Automated

**18.6.10 Microsoft Peer-to-Peer Networking Services**

- [ ] 18.6.10.2 Ensure 'Turn off Microsoft Peer-to-Peer Networking Services' is set to 'Enabled' — L2 · Automated

**18.6.11 Network Connections**

- [ ] 18.6.11.2 Ensure 'Prohibit installation and configuration of Network Bridge on your DNS domain network' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.11.3 Ensure 'Prohibit use of Internet Connection Sharing on your DNS domain network' is set to 'Enabled' — L1 · Automated
- [ ] 18.6.11.4 Ensure 'Require domain users to elevate when setting a network's location' is set to 'Enabled' — L1 · Automated

**18.6.14 Network Provider**

- [ ] 18.6.14.1 Ensure 'Hardened UNC Paths' is set to 'Enabled, with "Require Mutual Authentication", "Require Integrity", and "Require Privacy" set for all NETLOGON and SYSVOL shares' — L1 · Automated

**18.6.19 TCPIP Settings**

**18.6.19.2 Parameters**

- [ ] 18.6.19.2.1 Disable IPv6 (Ensure TCPIP6 Parameter 'DisabledComponents' is set to '0xff (255)') — L2 · Automated

**18.6.20 Windows Connect Now**

- [ ] 18.6.20.1 Ensure 'Configuration of wireless settings using Windows Connect Now' is set to 'Disabled' — L2 · Automated
- [ ] 18.6.20.2 Ensure 'Prohibit access of the Windows Connect Now wizards' is set to 'Enabled' — L2 · Automated

**18.6.21 Windows Connection Manager**

- [ ] 18.6.21.1 Ensure 'Minimize the number of simultaneous connections to the Internet or a Windows Domain' is set to 'Enabled: 3 = Prevent Wi-Fi when on Ethernet' — L1 · Automated
- [ ] 18.6.21.2 Ensure 'Prohibit connection to non-domain networks when connected to domain authenticated network' is set to 'Enabled' — L1 · Automated

**18.6.23 WLAN Service**

**18.6.23.2 WLAN Settings**

- [ ] 18.6.23.2.1 Ensure 'Allow Windows to automatically connect to suggested open hotspots, to networks shared by contacts, and to hotspots offering paid services' is set to 'Disabled' — L1 · Automated

#### 18.7 Printers

- [ ] 18.7.1 Ensure 'Allow Print Spooler to accept client connections' is set to 'Disabled' — L1 · Automated
- [ ] 18.7.2 Ensure 'Configure Redirection Guard' is set to 'Enabled: Redirection Guard Enabled' — L1 · Automated
- [ ] 18.7.3 Ensure 'Configure RPC connection settings: Protocol to use for outgoing RPC connections' is set to 'Enabled: RPC over TCP' — L1 · Automated
- [ ] 18.7.4 Ensure 'Configure RPC connection settings: Use authentication for outgoing RPC connections' is set to 'Enabled: Default' — L1 · Automated
- [ ] 18.7.5 Ensure 'Configure RPC listener settings: Protocols to allow for incoming RPC connections' is set to 'Enabled: RPC over TCP' — L1 · Automated
- [ ] 18.7.6 Ensure 'Configure RPC listener settings: Authentication protocol to use for incoming RPC connections:' is set to 'Enabled: Negotiate' or higher — L1 · Automated
- [ ] 18.7.7 Ensure 'Configure RPC over TCP port' is set to 'Enabled: 0' — L1 · Automated
- [ ] 18.7.8 Ensure 'Configure RPC packet level privacy setting for incoming connections' is set to 'Enabled' — L1 · Automated
- [ ] 18.7.9 Ensure 'Configure Windows protected print' is set to 'Enabled' — L2 · Automated
- [ ] 18.7.10 Ensure 'Limits print driver installation to Administrators' is set to 'Enabled' — L1 · Automated
- [ ] 18.7.11 Ensure 'Manage processing of Queue-specific files' is set to 'Enabled: Limit Queuespecific files to Color profiles' — L1 · Automated
- [ ] 18.7.12 Ensure 'Point and Print Restrictions: When installing drivers for a new connection' is set to 'Enabled: Show warning and elevation prompt' — L1 · Automated
- [ ] 18.7.13 Ensure 'Point and Print Restrictions: When updating drivers for an existing connection' is set to 'Enabled: Show warning and elevation prompt' — L1 · Automated
- [ ] 18.7.14 Ensure 'Require IPPS for IPP printers' is set to 'Enabled' — L2 · Automated
- [ ] 18.7.15 Ensure 'Set TLS/SSL security policy for IPP printers: Disallow invalid certificate authority' is set to 'Enabled: Checked' — L2 · Automated
- [ ] 18.7.16 Ensure 'Set TLS/SSL security policy for IPP printers: Disallow non-server certificates' is set to 'Enabled: Checked' — L2 · Automated
- [ ] 18.7.17 Ensure 'Set TLS/SSL security policy for IPP printers: Disallow invalid certificate common name' is set to 'Enabled: Checked' — L2 · Automated
- [ ] 18.7.18 Ensure 'Set TLS/SSL security policy for IPP printers: Disallow invalid certificate date' is set to 'Enabled: Checked' — L2 · Automated

#### 18.8 Start Menu and Taskbar

**18.8.1 Notifications**

- [ ] 18.8.1.1 Ensure 'Turn off notifications network usage' is set to 'Enabled' — L2 · Automated
- [ ] 18.8.2 Ensure 'Remove Personalized Website Recommendations from the Recommended section in the Start Menu' is set to 'Enabled' — L2 · Automated

#### 18.9 System

**18.9.3 Audit Process Creation**

- [ ] 18.9.3.1 Ensure 'Include command line in process creation events' is set to 'Enabled' — L1 · Automated

**18.9.4 Credentials Delegation**

- [ ] 18.9.4.1 Ensure 'Encryption Oracle Remediation' is set to 'Enabled: Force Updated Clients' — L1 · Automated
- [ ] 18.9.4.2 Ensure 'Remote host allows delegation of non-exportable credentials' is set to 'Enabled' — L1 · Automated

**18.9.5 Device Guard**

- [ ] 18.9.5.1 Ensure 'Turn On Virtualization Based Security' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.5.2 Ensure 'Turn On Virtualization Based Security: Select Platform Security Level' is set to 'Secure Boot' or higher — L1 · Automated
- [ ] 18.9.5.3 Ensure 'Turn On Virtualization Based Security: Virtualization Based Protection of Code Integrity' is set to 'Enabled with UEFI lock' — L1 · Automated
- [ ] 18.9.5.4 Ensure 'Turn On Virtualization Based Security: Require UEFI Memory Attributes Table' is set to 'True (checked)' — L1 · Automated
- [ ] 18.9.5.5 Ensure 'Turn On Virtualization Based Security: Credential Guard Configuration' is set to 'Enabled with UEFI lock' — L1 · Automated
- [ ] 18.9.5.6 Ensure 'Turn On Virtualization Based Security: Secure Launch Configuration' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.5.7 Ensure 'Turn On Virtualization Based Security: Kernel-mode Hardware-enforced Stack Protection' is set to 'Enabled: Enabled in enforcement mode' — L1 · Automated

**18.9.7 Device Installation**

**18.9.7.1 Device Installation Restrictions**

- [ ] 18.9.7.1.1 Ensure 'Prevent installation of devices using drivers that match these device setup classes' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.9.7.1.2 Ensure 'Prevent installation of devices using drivers that match these device setup classes: Prevent installation of devices using drivers for these device setup' is set to 'IEEE 1394 device setup classes' — L1+BL / L2+BL / BL · Automated
- [ ] 18.9.7.1.3 Ensure 'Prevent installation of devices using drivers that match these device setup classes: Also apply to matching devices that are already installed.' is set to 'True' (checked) — L1+BL / L2+BL / BL · Automated
- [ ] 18.9.7.2 Ensure 'Prevent automatic download of applications associated with device metadata' is set to 'Enabled' — L1 · Automated

**18.9.13 Early Launch Antimalware**

- [ ] 18.9.13.1 Ensure 'Boot-Start Driver Initialization Policy' is set to 'Enabled: Good, unknown and bad but critical' — L1 · Automated

**18.9.17 Filesystem (formerly NTFS Filesystem)**

- [ ] 18.9.17.1 Ensure 'Enable / disable CLFS logfile authentication' is set to 'Enabled' — L1 · Automated

**18.9.19 Group Policy**

- [ ] 18.9.19.2 Ensure 'Configure security policy processing: Do not apply during periodic background processing' is set to 'Enabled: FALSE' — L1 · Automated
- [ ] 18.9.19.3 Ensure 'Configure security policy processing: Process even if the Group Policy objects have not changed' is set to 'Enabled: TRUE' — L1 · Automated
- [ ] 18.9.19.4 Ensure 'Continue experiences on this device' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.19.5 Ensure 'Turn off background refresh of Group Policy' is set to 'Disabled' — L1 · Automated

**18.9.20 Internet Communication Management**

**18.9.20.1 Internet Communication settings**

- [ ] 18.9.20.1.1 Ensure 'Turn off access to the Store' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.2 Ensure 'Turn off downloading of print drivers over HTTP' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.20.1.3 Ensure 'Turn off handwriting personalization data sharing' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.4 Ensure 'Turn off handwriting recognition error reporting' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.5 Ensure 'Turn off Internet Connection Wizard if URL connection is referring to Microsoft.com' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.6 Ensure 'Turn off Internet download for Web publishing and online ordering wizards' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.20.1.7 Ensure 'Turn off printing over HTTP' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.8 Ensure 'Turn off Registration if URL connection is referring to Microsoft.com' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.9 Ensure 'Turn off Search Companion content file updates' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.10 Ensure 'Turn off the "Order Prints" picture task' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.11 Ensure 'Turn off the "Publish to Web" task for files and folders' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.12 Ensure 'Turn off the Windows Messenger Customer Experience Improvement Program' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.13 Ensure 'Turn off Windows Customer Experience Improvement Program' is set to 'Enabled' — L2 · Automated
- [ ] 18.9.20.1.14 Ensure 'Turn off Windows Error Reporting' is set to 'Enabled' — L2 · Automated

**18.9.23 Kerberos**

- [ ] 18.9.23.1 Ensure 'Support device authentication using certificate' is set to 'Enabled: Automatic' — L2 · Automated

**18.9.24 Kernel DMA Protection**

- [ ] 18.9.24.1 Ensure 'Enumeration policy for external devices incompatible with Kernel DMA Protection' is set to 'Enabled: Block All' — L1+BL / L2+BL / BL · Automated

**18.9.26 LAPS**

- [ ] 18.9.26.1 Ensure 'Configure password backup directory' is set to 'Enabled: Active Directory' or 'Enabled: Azure Active Directory' — L1 · Automated
- [ ] 18.9.26.2 Ensure 'Do not allow password expiration time longer than required by policy' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.26.3 Ensure 'Enable password encryption' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.26.4 Ensure 'Password Settings: Password Complexity' is set to 'Enabled: Large letters + small letters + numbers + special characters' or 'Passphrase' — L1 · Automated
- [ ] 18.9.26.5 Ensure 'Password Settings: Password Length' is set to 'Enabled: 15 or more' — L1 · Automated
- [ ] 18.9.26.6 Ensure 'Password Settings: Password Age (Days)' is set to 'Enabled: 30 or fewer' — L1 · Automated
- [ ] 18.9.26.7 Ensure 'Post-authentication actions: Grace period (hours)' is set to 'Enabled: 8 or fewer hours, but not 0' — L1 · Automated
- [ ] 18.9.26.8 Ensure 'Post-authentication actions: Actions' is set to 'Enabled: Reset the password and logoff the managed account' or higher — L1 · Automated

**18.9.27 Local Security Authority**

- [ ] 18.9.27.1 Ensure 'Allow Custom SSPs and APs to be loaded into LSASS' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.27.2 Ensure 'Configures LSASS to run as a protected process' is set to 'Enabled: Enabled with UEFI Lock' — L1 · Automated

**18.9.28 Locale Services**

- [ ] 18.9.28.1 Ensure 'Disallow copying of user input methods to the system account for sign-in' is set to 'Enabled' — L2 · Automated

**18.9.29 Logon**

- [ ] 18.9.29.1 Ensure 'Block user from showing account details on sign-in' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.29.2 Ensure 'Do not display network selection UI' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.29.3 Ensure 'Do not enumerate connected users on domain-joined computers' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.29.4 Ensure 'Enumerate local users on domain-joined computers' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.29.5 Ensure 'Turn off app notifications on the lock screen' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.29.6 Ensure 'Turn off picture password sign-in' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.29.7 Ensure 'Turn on convenience PIN sign-in' is set to 'Disabled' — L1 · Automated

**18.9.31 Net Logon**

**18.9.31.1 DC Locator DNS Records**

- [ ] 18.9.31.1.1 Ensure 'Block NetBIOS-based discovery for domain controller location' is set to 'Enabled' — L1 · Automated

**18.9.33 OS Policies**

- [ ] 18.9.33.1 Ensure 'Allow Clipboard synchronization across devices' is set to 'Disabled' — L2 · Automated
- [ ] 18.9.33.2 Ensure 'Allow upload of User Activities' is set to 'Disabled' — L2 · Automated

**18.9.35 Power Management**

**18.9.35.6 Sleep Settings**

- [ ] 18.9.35.6.1 Ensure 'Allow network connectivity during connected-standby (on battery)' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.35.6.2 Ensure 'Allow network connectivity during connected-standby (plugged in)' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.35.6.3 Ensure 'Allow standby states (S1-S3) when sleeping (on battery)' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.9.35.6.4 Ensure 'Allow standby states (S1-S3) when sleeping (plugged in)' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.9.35.6.5 Ensure 'Require a password when a computer wakes (on battery)' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.35.6.6 Ensure 'Require a password when a computer wakes (plugged in)' is set to 'Enabled' — L1 · Automated

**18.9.37 Remote Assistance**

- [ ] 18.9.37.1 Ensure 'Configure Offer Remote Assistance' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.37.2 Ensure 'Configure Solicited Remote Assistance' is set to 'Disabled' — L1 · Automated

**18.9.38 Remote Procedure Call**

- [ ] 18.9.38.1 Ensure 'Enable RPC Endpoint Mapper Client Authentication' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.38.2 Ensure 'Restrict Unauthenticated RPC clients' is set to 'Enabled: Authenticated' — L1 · Automated

**18.9.41 Security Account Manager**

- [ ] 18.9.41.1 Ensure 'Configure SAM change password RPC methods policy' is set to 'Enabled: Block all change password RPC methods' — L1 · Automated

**18.9.49 Troubleshooting and Diagnostics**

**18.9.49.5 Microsoft Support Diagnostic Tool**

- [ ] 18.9.49.5.1 Ensure 'Microsoft Support Diagnostic Tool: Turn on MSDT interactive communication with support provider' is set to 'Disabled' — L2 · Automated

**18.9.49.11 Windows Performance PerfTrack**

- [ ] 18.9.49.11.1 Ensure 'Enable/Disable PerfTrack' is set to 'Disabled' — L2 · Automated

**18.9.51 User Profiles**

- [ ] 18.9.51.1 Ensure 'Turn off the advertising ID' is set to 'Enabled' — L2 · Automated

**18.9.53 Windows Time Service**

**18.9.53.1 Time Providers**

- [ ] 18.9.53.1.1 Ensure 'Enable Windows NTP Client' is set to 'Enabled' — L1 · Automated
- [ ] 18.9.53.1.2 Ensure 'Enable Windows NTP Server' is set to 'Disabled' — L1 · Automated
- [ ] 18.9.54 Ensure 'Configure the behavior of the sudo command' is set to 'Enabled: Disabled' — L1 · Automated

#### 18.10 Windows Components

**18.10.3 App and Device Inventory**

- [ ] 18.10.3.1 Ensure 'Turn off API Sampling' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.3.2 Ensure 'Turn off Application Footprint' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.3.3 Ensure 'Turn off Install Tracing' is set to 'Enabled' — L2 · Automated

**18.10.4 App Package Deployment**

- [ ] 18.10.4.1 Ensure 'Allow a Windows app to share application data between users' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.4.2 Ensure 'Not allow per-user unsigned packages to install by default (requires explicitly allow per install)' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.4.3 Ensure 'Prevent non-admin users from installing packaged Windows apps' is set to 'Enabled' — L1 · Automated

**18.10.5 App Privacy**

- [ ] 18.10.5.1 Ensure 'Let Windows apps activate with voice while the system is locked' is set to 'Enabled: Force Deny' — L1 · Automated

**18.10.6 App runtime**

- [ ] 18.10.6.1 Ensure 'Allow Microsoft accounts to be optional' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.6.2 Ensure 'Block launching Universal Windows apps with Windows Runtime API access from hosted content.' is set to 'Enabled' — L2 · Automated

**18.10.8 AutoPlay Policies**

- [ ] 18.10.8.1 Ensure 'Disallow Autoplay for non-volume devices' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.8.2 Ensure 'Set the default behavior for AutoRun' is set to 'Enabled: Do not execute any autorun commands' — L1 · Automated
- [ ] 18.10.8.3 Ensure 'Turn off Autoplay' is set to 'Enabled: All drives' — L1 · Automated

**18.10.9 Biometrics**

**18.10.9.1 Facial Features**

- [ ] 18.10.9.1.1 Ensure 'Configure enhanced anti-spoofing' is set to 'Enabled' — L1 · Automated

**18.10.10 BitLocker Drive Encryption**

**18.10.10.1 Fixed Data Drives**

- [ ] 18.10.10.1.1 Ensure 'Allow access to BitLocker-protected fixed data drives from earlier versions of Windows' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.2 Ensure 'Choose how BitLocker-protected fixed drives can be recovered' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.3 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Allow data recovery agent' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.4 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Recovery Password' is set to 'Enabled: Allow 48-digit recovery password' or higher — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.5 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Recovery Key' is set to 'Enabled: Allow 256-bit recovery key' or higher — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.6 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Omit recovery options from the BitLocker setup wizard' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.7 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Save BitLocker recovery information to AD DS for fixed data drives' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.8 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Configure storage of BitLocker recovery information to AD DS' is set to 'Enabled: Backup recovery passwords and key packages' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.9 Ensure 'Choose how BitLocker-protected fixed drives can be recovered: Do not enable BitLocker until recovery information is stored to AD DS for fixed data drives' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.10 Ensure 'Configure use of hardware-based encryption for fixed data drives' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.11 Ensure 'Configure use of passwords for fixed data drives' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.12 Ensure 'Configure use of smart cards on fixed data drives' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.1.13 Ensure 'Configure use of smart cards on fixed data drives: Require use of smart cards on fixed data drives' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated

**18.10.10.2 Operating System Drives**

- [ ] 18.10.10.2.1 Ensure 'Allow enhanced PINs for startup' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.2 Ensure 'Allow Secure Boot for integrity validation' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.3 Ensure 'Choose how BitLocker-protected operating system drives can be recovered' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.4 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Allow data recovery agent' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.5 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Recovery Password' is set to 'Enabled: Require 48-digit recovery password' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.6 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Recovery Key' is set to 'Enabled: Do not allow 256-bit recovery key' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.7 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Omit recovery options from the BitLocker setup wizard' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.8 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Save BitLocker recovery information to AD DS for operating system drives' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.9 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Configure storage of BitLocker recovery information to AD DS:' is set to 'Enabled: Store recovery passwords and key packages' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.10 Ensure 'Choose how BitLocker-protected operating system drives can be recovered: Do not enable BitLocker until recovery information is stored to AD DS for operating system drives' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.2.11 Ensure 'Configure use of hardware-based encryption for operating system drives' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated

**18.10.10.3 Removable Data Drives**

- [ ] 18.10.10.3.1 Ensure 'Allow access to BitLocker-protected removable data drives from earlier versions of Windows' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.2 Ensure 'Choose how BitLocker-protected removable drives can be recovered' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.3 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Allow data recovery agent' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.4 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Recovery Password' is set to 'Enabled: Do not allow 48-digit recovery password' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.5 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Recovery Key' is set to 'Enabled: Do not allow 256-bit recovery key' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.6 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Omit recovery options from the BitLocker setup wizard' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.7 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Save BitLocker recovery information to AD DS for removable data drives' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.8 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Configure storage of BitLocker recovery information to AD DS:' is set to 'Enabled: Backup recovery passwords and key packages' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.9 Ensure 'Choose how BitLocker-protected removable drives can be recovered: Do not enable BitLocker until recovery information is stored to AD DS for removable data drives' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.10 Ensure 'Configure use of hardware-based encryption for removable data drives' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.11 Ensure 'Configure use of passwords for removable data drives' is set to 'Disabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.12 Ensure 'Configure use of smart cards on removable data drives' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.13 Ensure 'Configure use of smart cards on removable data drives: Require use of smart cards on removable data drives' is set to 'Enabled: True' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.14 Ensure 'Deny write access to removable drives not protected by BitLocker' is set to 'Enabled' — L1+BL / L2+BL / BL · Automated
- [ ] 18.10.10.3.15 Ensure 'Deny write access to removable drives not protected by BitLocker: Do not allow write access to devices configured in another organization' is set to 'Enabled: False' — L1+BL / L2+BL / BL · Automated

**18.10.11 Camera**

- [ ] 18.10.11.1 Ensure 'Allow Use of Camera' is set to 'Disabled' — L2 · Automated

**18.10.13 Cloud Content**

- [ ] 18.10.13.1 Ensure 'Turn off cloud consumer account state content' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.13.2 Ensure 'Turn off cloud optimized content' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.13.3 Ensure 'Turn off Microsoft consumer experiences' is set to 'Enabled' — L1 · Automated

**18.10.14 Connect**

- [ ] 18.10.14.1 Ensure 'Require pin for pairing' is set to 'Enabled: First Time' OR 'Enabled: Always' — L1 · Automated

**18.10.15 Credential User Interface**

- [ ] 18.10.15.1 Ensure 'Do not display the password reveal button' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.15.2 Ensure 'Enumerate administrator accounts on elevation' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.15.3 Ensure 'Prevent the use of security questions for local accounts' is set to 'Enabled' — L1 · Automated

**18.10.16 Data Collection and Preview Builds**

- [ ] 18.10.16.1 Ensure 'Allow Diagnostic Data' is set to 'Enabled: Diagnostic data off (not recommended)' or 'Enabled: Send required diagnostic data' — L1 · Automated
- [ ] 18.10.16.2 Ensure 'Configure Authenticated Proxy usage for the Connected User Experience and Telemetry service' is set to 'Enabled: Disable Authenticated Proxy usage' — L2 · Automated
- [ ] 18.10.16.3 Ensure 'Do not show feedback notifications' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.16.4 Ensure 'Enable OneSettings Auditing' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.16.5 Ensure 'Limit Diagnostic Log Collection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.16.6 Ensure 'Limit Dump Collection' is set to 'Enabled' — L2 · Automated

**18.10.17 Delivery Optimization**

- [ ] 18.10.17.1 Ensure 'Download Mode' is NOT set to 'Enabled: Internet' — L1 · Automated

**18.10.18 Desktop App Installer**

- [ ] 18.10.18.1 Ensure 'Enable App Installer' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.18.2 Ensure 'Enable App Installer Experimental Features' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.18.3 Ensure 'Enable App Installer Hash Override' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.18.4 Ensure 'Enable App Installer Local Archive Malware Scan Override' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.18.5 Ensure 'Enable App Installer Microsoft Store Source Certificate Validation Bypass' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.18.6 Ensure 'Enable App Installer ms-appinstaller protocol' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.18.7 Ensure 'Enable Windows Package Manager command line interfaces' is set to 'Disabled' — L2 · Automated

**18.10.26 Event Log Service**

**18.10.26.1 Application**

- [ ] 18.10.26.1.1 Ensure 'Application: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.26.1.2 Ensure 'Application: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater' — L1 · Automated

**18.10.26.2 Security**

- [ ] 18.10.26.2.1 Ensure 'Security: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.26.2.2 Ensure 'Security: Specify the maximum log file size (KB)' is set to 'Enabled: 196,608 or greater' — L1 · Automated

**18.10.26.3 Setup**

- [ ] 18.10.26.3.1 Ensure 'Setup: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.26.3.2 Ensure 'Setup: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater' — L1 · Automated

**18.10.26.4 System**

- [ ] 18.10.26.4.1 Ensure 'System: Control Event Log behavior when the log file reaches its maximum size' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.26.4.2 Ensure 'System: Specify the maximum log file size (KB)' is set to 'Enabled: 32,768 or greater' — L1 · Automated

**18.10.29 File Explorer (formerly Windows Explorer)**

- [ ] 18.10.29.2 Ensure 'Turn off account-based insights, recent, favorite, and recommended files in File Explorer' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.29.3 Ensure 'Turn off Data Execution Prevention for Explorer' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.29.4 Ensure 'Do not apply the Mark of the Web tag to files copied from insecure sources' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.29.5 Ensure 'Turn off heap termination on corruption' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.29.6 Ensure 'Turn off shell protocol protected mode' is set to 'Disabled' — L1 · Automated

**18.10.36 Location and Sensors**

- [ ] 18.10.36.1 Ensure 'Turn off location' is set to 'Enabled' — L2 · Automated

**18.10.40 Messaging**

- [ ] 18.10.40.1 Ensure 'Allow Message Service Cloud Sync' is set to 'Disabled' — L2 · Automated

**18.10.41 Microsoft account**

- [ ] 18.10.41.1 Ensure 'Block all consumer Microsoft account user authentication' is set to 'Enabled' — L1 · Automated

**18.10.42 Microsoft Defender Antivirus (formerly Windows Defender and Windows Defender Antivirus)**

**18.10.42.4 Features**

- [ ] 18.10.42.4.1 Ensure 'Enable EDR in block mode' is set to 'Enabled' — L1 · Automated

**18.10.42.5 MAPS**

- [ ] 18.10.42.5.1 Ensure 'Configure local setting override for reporting to Microsoft MAPS' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.42.5.2 Ensure 'Join Microsoft MAPS' is set to 'Enabled: Advanced' — L1 · Automated

**18.10.42.6 Microsoft Defender Exploit Guard (formerly Windows Defender Exploit Guard)**

**18.10.42.6.1 Attack Surface Reduction**

- [ ] 18.10.42.6.1.1 Ensure 'Configure Attack Surface Reduction rules' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.6.1.2 Ensure 'Configure Attack Surface Reduction rules: Set the state for each ASR rule' is configured — L1 · Automated

**18.10.42.6.3 Network Protection**

- [ ] 18.10.42.6.3.1 Ensure 'Prevent users and apps from accessing dangerous websites' is set to 'Enabled: Block' — L1 · Automated

**18.10.42.7 MpEngine**

- [ ] 18.10.42.7.1 Ensure 'Enable file hash computation feature' is set to 'Enabled' — L1 · Automated

**18.10.42.8 Network Inspection System**

- [ ] 18.10.42.8.1 Ensure 'Convert warn verdict to block' is set to 'Enabled' — L2 · Automated

**18.10.42.10 Real-time Protection**

- [ ] 18.10.42.10.1 Ensure 'Configure real-time protection and Security Intelligence Updates during OOBE' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.10.2 Ensure 'Scan all downloaded files and attachments' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.10.3 Ensure 'Turn off real-time protection' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.42.10.4 Ensure 'Turn on behavior monitoring' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.10.5 Ensure 'Turn on script scanning' is set to 'Enabled' — L1 · Automated

**18.10.42.11 Remediation**

**18.10.42.11.1 Behavioral Network Blocks**

**18.10.42.11.1.1 Brute-Force Protection**

- [ ] 18.10.42.11.1.1.1 Ensure 'Configure Brute-Force Protection aggressiveness' is set to 'Enabled: Medium' or higher — L2 · Automated
- [ ] 18.10.42.11.1.1.2 Ensure 'Configure Remote Encryption Protection Mode' is set to 'Enabled: Audit' or higher — L1 · Automated

**18.10.42.11.1.2 Remote Encryption Protection**

- [ ] 18.10.42.11.1.2.1 Ensure 'Configure how aggressively Remote Encryption Protection blocks threats' is set to 'Enabled: Medium' or higher — L2 · Automated

**18.10.42.12 Reporting**

- [ ] 18.10.42.12.1 Ensure 'Configure Watson events' is set to 'Disabled' — L2 · Automated

**18.10.42.13 Scan**

- [ ] 18.10.42.13.1 Ensure 'Scan excluded files and directories during quick scans' is set to 'Enabled: 1' — L1 · Automated
- [ ] 18.10.42.13.2 Ensure 'Scan packed executables' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.13.3 Ensure 'Scan removable drives' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.13.4 Ensure 'Trigger a quick scan after X days without any scans' is set to 'Enabled: 7' — L1 · Automated
- [ ] 18.10.42.13.5 Ensure 'Turn on e-mail scanning' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.42.16 Ensure 'Configure detection for potentially unwanted applications' is set to 'Enabled: Block' — L1 · Automated
- [ ] 18.10.42.17 Ensure 'Control whether exclusions are visible to local users' is set to 'Enabled' — L1 · Automated

**18.10.43 Microsoft Defender Application Guard (formerly Windows Defender Application Guard)**

- [ ] 18.10.43.1 Ensure 'Allow auditing events in Microsoft Defender Application Guard' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.43.2 Ensure 'Allow camera and microphone access in Microsoft Defender Application Guard' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.43.3 Ensure 'Allow data persistence for Microsoft Defender Application Guard' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.43.4 Ensure 'Allow files to download and save to the host operating system from Microsoft Defender Application Guard' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.43.5 Ensure 'Configure Microsoft Defender Application Guard clipboard settings: Clipboard behavior setting' is set to 'Enabled: Enable clipboard operation from an isolated session to the host' — L1 · Automated
- [ ] 18.10.43.6 Ensure 'Turn on Microsoft Defender Application Guard in Managed Mode' is set to 'Enabled: 1' — L1 · Automated

**18.10.49 News and interests**

- [ ] 18.10.49.1 Ensure 'Enable news and interests on the taskbar' is set to 'Disabled' — L2 · Automated

**18.10.50 OneDrive (formerly SkyDrive)**

- [ ] 18.10.50.1 Ensure 'Prevent the usage of OneDrive for file storage' is set to 'Enabled' — L2 · Automated

**18.10.56 Push To Install**

- [ ] 18.10.56.1 Ensure 'Turn off Push To Install service' is set to 'Enabled' — L2 · Automated

**18.10.57 Remote Desktop Services (formerly Terminal Services)**

**18.10.57.2 Remote Desktop Connection Client**

- [ ] 18.10.57.2.2 Ensure 'Disable Cloud Clipboard integration for server-to-client data transfer' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.2.3 Ensure 'Do not allow passwords to be saved' is set to 'Enabled' — L1 · Automated

**18.10.57.3 Remote Desktop Session Host (formerly Terminal Server)**

**18.10.57.3.2 Connections**

- [ ] 18.10.57.3.2.1 Ensure 'Allow users to connect remotely by using Remote Desktop Services' is set to 'Disabled' — L2 · Automated

**18.10.57.3.3 Device and Resource Redirection**

- [ ] 18.10.57.3.3.1 Ensure 'Allow UI Automation redirection' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.57.3.3.2 Ensure 'Do not allow COM port redirection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.3.3.3 Ensure 'Do not allow drive redirection' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.57.3.3.4 Ensure 'Do not allow location redirection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.3.3.5 Ensure 'Do not allow LPT port redirection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.3.3.6 Ensure 'Do not allow supported Plug and Play device redirection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.3.3.7 Ensure 'Do not allow WebAuthn redirection' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.57.3.3.8 Ensure 'Restrict clipboard transfer from server to client' is set to 'Enabled: Disable clipboard transfers from server to client' — L2 · Automated

**18.10.57.3.9 Security**

- [ ] 18.10.57.3.9.1 Ensure 'Always prompt for password upon connection' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.57.3.9.2 Ensure 'Require secure RPC communication' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.57.3.9.3 Ensure 'Require use of specific security layer for remote (RDP) connections' is set to 'Enabled: SSL' — L1 · Automated
- [ ] 18.10.57.3.9.4 Ensure 'Require user authentication for remote connections by using Network Level Authentication' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.57.3.9.5 Ensure 'Set client connection encryption level' is set to 'Enabled: High Level' — L1 · Automated

**18.10.57.3.10 Session Time Limits**

- [ ] 18.10.57.3.10.1 Ensure 'Set time limit for active but idle Remote Desktop Services sessions' is set to 'Enabled: 15 minutes or less, but not Never (0)' — L2 · Automated
- [ ] 18.10.57.3.10.2 Ensure 'Set time limit for disconnected sessions' is set to 'Enabled: 1 minute' — L2 · Automated

**18.10.57.3.11 Temporary folders**

- [ ] 18.10.57.3.11.1 Ensure 'Do not delete temp folders upon exit' is set to 'Disabled' — L1 · Automated

**18.10.58 RSS Feeds**

- [ ] 18.10.58.1 Ensure 'Prevent downloading of enclosures' is set to 'Enabled' — L1 · Automated

**18.10.59 Search**

- [ ] 18.10.59.2 Ensure 'Allow Cloud Search' is set to 'Enabled: Disable Cloud Search' — L2 · Automated
- [ ] 18.10.59.3 Ensure 'Allow Cortana' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.59.4 Ensure 'Allow Cortana above lock screen' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.59.5 Ensure 'Allow indexing of encrypted files' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.59.6 Ensure 'Allow search and Cortana to use location' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.59.7 Ensure 'Allow search highlights' is set to 'Disabled' — L2 · Automated

**18.10.63 Software Protection Platform**

- [ ] 18.10.63.1 Ensure 'Turn off KMS Client Online AVS Validation' is set to 'Enabled' — L2 · Automated

**18.10.66 Store**

- [ ] 18.10.66.1 Ensure 'Disable all apps from Microsoft Store' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.66.2 Ensure 'Turn off Automatic Download and Install of updates' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.66.3 Ensure 'Turn off the offer to update to the latest version of Windows' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.66.4 Ensure 'Turn off the Store application' is set to 'Enabled' — L2 · Automated

**18.10.72 Widgets**

- [ ] 18.10.72.1 Ensure 'Allow widgets' is set to 'Disabled' — L2 · Automated

**18.10.73 Windows AI**

- [ ] 18.10.73.1 Ensure 'Allow Recall to be enabled' is set to 'Disabled' — L1 · Automated

**18.10.77 Windows Defender SmartScreen**

**18.10.77.1 Enhanced Phishing Protection**

- [ ] 18.10.77.1.1 Ensure 'Automatic Data Collection' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.77.1.2 Ensure 'Notify Malicious' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.77.1.3 Ensure 'Notify Password Reuse' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.77.1.4 Ensure 'Notify Unsafe App' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.77.1.5 Ensure 'Service Enabled' is set to 'Enabled' — L1 · Automated

**18.10.77.2 Explorer**

- [ ] 18.10.77.2.1 Ensure 'Configure Windows Defender SmartScreen' is set to 'Enabled: Warn and prevent bypass' — L1 · Automated

**18.10.79 Windows Game Recording and Broadcasting**

- [ ] 18.10.79.1 Ensure 'Enables or disables Windows Game Recording and Broadcasting' is set to 'Disabled' — L1 · Automated

**18.10.80 Windows Hello for Business (formerly Microsoft Passport for Work)**

- [ ] 18.10.80.1 Ensure 'Enable ESS with Supported Peripherals' is set to 'Enabled: 1' — L1 · Automated

**18.10.81 Windows Ink Workspace**

- [ ] 18.10.81.1 Ensure 'Allow suggested apps in Windows Ink Workspace' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.81.2 Ensure 'Allow Windows Ink Workspace' is set to 'Enabled: On, but disallow access above lock' OR 'Enabled: Disabled' — L1 · Automated

**18.10.82 Windows Installer**

- [ ] 18.10.82.1 Ensure 'Allow user control over installs' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.82.2 Ensure 'Always install with elevated privileges' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.82.3 Ensure 'Prevent Internet Explorer security prompt for Windows Installer scripts' is set to 'Disabled' — L2 · Automated

**18.10.83 Windows Logon Options**

- [ ] 18.10.83.1 Ensure 'Configure the transmission of the user's password in the content of MPR notifications sent by winlogon.' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.83.2 Ensure 'Sign-in and lock last interactive user automatically after a restart' is set to 'Disabled' — L1 · Automated

**18.10.88 Windows PowerShell**

- [ ] 18.10.88.1 Ensure 'Turn on PowerShell Script Block Logging' is set to 'Enabled' — L2 · Automated
- [ ] 18.10.88.2 Ensure 'Turn on PowerShell Transcription' is set to 'Enabled' — L2 · Automated

**18.10.90 Windows Remote Management (WinRM)**

**18.10.90.1 WinRM Client**

- [ ] 18.10.90.1.1 Ensure 'Allow Basic authentication' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.90.1.2 Ensure 'Allow unencrypted traffic' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.90.1.3 Ensure 'Disallow Digest authentication' is set to 'Enabled' — L1 · Automated

**18.10.90.2 WinRM Service**

- [ ] 18.10.90.2.1 Ensure 'Allow Basic authentication' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.90.2.2 Ensure 'Allow remote server management through WinRM' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.90.2.3 Ensure 'Allow unencrypted traffic' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.90.2.4 Ensure 'Disallow WinRM from storing RunAs credentials' is set to 'Enabled' — L1 · Automated

**18.10.91 Windows Remote Shell**

- [ ] 18.10.91.1 Ensure 'Allow Remote Shell Access' is set to 'Disabled' — L2 · Automated

**18.10.92 Windows Sandbox**

- [ ] 18.10.92.1 Ensure 'Allow clipboard sharing with Windows Sandbox' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.92.2 Ensure 'Allow mapping folders into Windows Sandbox' is set to 'Disabled' — L2 · Automated
- [ ] 18.10.92.3 Ensure 'Allow networking in Windows Sandbox' is set to 'Disabled' — L1 · Automated

**18.10.93 Windows Security (formerly Windows Defender Security Center)**

**18.10.93.2 App and browser protection**

- [ ] 18.10.93.2.1 Ensure 'Prevent users from modifying settings' is set to 'Enabled' — L1 · Automated

**18.10.94 Windows Update**

**18.10.94.1 Legacy Policies**

- [ ] 18.10.94.1.1 Ensure 'No auto-restart with logged on users for scheduled automatic updates installations' is set to 'Disabled' — L1 · Automated

**18.10.94.2 Manage end user experience**

- [ ] 18.10.94.2.1 Ensure 'Configure Automatic Updates' is set to 'Enabled' — L1 · Automated
- [ ] 18.10.94.2.2 Ensure 'Configure Automatic Updates: Scheduled install day' is set to '0 - Every day' — L1 · Automated
- [ ] 18.10.94.2.3 Ensure 'Enable features introduced via servicing that are off by default' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.94.2.4 Ensure 'Remove access to “Pause updates” feature' is set to 'Enabled' — L1 · Automated

**18.10.94.4 Manage updates offered from Windows Update (formerly Defer Windows Updates and Windows Update for Business)**

- [ ] 18.10.94.4.1 Ensure 'Manage preview builds' is set to 'Disabled' — L1 · Automated
- [ ] 18.10.94.4.2 Ensure 'Select when Quality Updates are received' is set to 'Enabled: 0 days' — L1 · Automated
- [ ] 18.10.94.4.3 Ensure 'Enable optional updates' is set to 'Disabled' — L1 · Automated

#### 18.11 Custom Settings

- [ ] 18.11.1 Ensure 'Disable HTTP proxy features: Disable WPAD' is set to 'Enabled: Checked' — L1 · Automated
- [ ] 18.11.2 Ensure 'Disable HTTP proxy features: Disable proxy authentication' is set to 'Enabled: Disable authentication over loopback interfaces' or higher — L1 · Automated

### 19 Administrative Templates (User)

#### 19.5 Start Menu and Taskbar

**19.5.1 Notifications**

- [ ] 19.5.1.1 Ensure 'Turn off toast notifications on the lock screen' is set to 'Enabled' — L1 · Automated

#### 19.6 System

**19.6.6 Internet Communication Management**

**19.6.6.1 Internet Communication settings**

- [ ] 19.6.6.1.1 Ensure 'Turn off Help Experience Improvement Program' is set to 'Enabled' — L2 · Automated

#### 19.7 Windows Components

**19.7.5 Attachment Manager**

- [ ] 19.7.5.1 Ensure 'Do not preserve zone information in file attachments' is set to 'Disabled' — L1 · Automated
- [ ] 19.7.5.2 Ensure 'Notify antivirus programs when opening attachments' is set to 'Enabled' — L1 · Automated

**19.7.8 Cloud Content**

- [ ] 19.7.8.1 Ensure 'Configure Windows spotlight on lock screen' is set to 'Disabled' — L1 · Automated
- [ ] 19.7.8.2 Ensure 'Do not suggest third-party content in Windows spotlight' is set to 'Enabled' — L1 · Automated
- [ ] 19.7.8.3 Ensure 'Do not use diagnostic data for tailored experiences' is set to 'Enabled' — L2 · Automated
- [ ] 19.7.8.4 Ensure 'Turn off all Windows spotlight features' is set to 'Enabled' — L2 · Automated
- [ ] 19.7.8.5 Ensure 'Turn off Spotlight collection on Desktop' is set to 'Enabled' — L1 · Automated

**19.7.26 Network Sharing**

- [ ] 19.7.26.1 Ensure 'Prevent users from sharing files within their profile.' is set to 'Enabled' — L1 · Automated

**19.7.46 Windows Media Player**

**19.7.46.2 Playback**

- [ ] 19.7.46.2.1 Ensure 'Prevent Codec Download' is set to 'Enabled' — L2 · Automated

## Source

CIS Microsoft Windows 11 Enterprise Benchmark v5.0.0 (01-27-2026), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[active-directory-pentesting/credentials/laps-toolkit]]
- [[active-directory-pentesting/credentials/group-policy-preferences]]
- [[evasion/amsi-bypass]]
- [[evasion/windows-defender-application-control-wdac-killing-edr]]
- [[active-directory-pentesting/windows-and-active-directory-attacks/ntlm-smb-relay]]
- [[active-directory-pentesting/credentials/llmnr-poisoning]]
