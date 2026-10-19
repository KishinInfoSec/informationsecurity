---
title: cis-macos-26-tahoe
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/macos, source/cis]
description: "CIS Apple macOS 26 Tahoe Benchmark v1.0.0 checklist: system and user policies, logging, firewall, encryption, with levels."
source_pdf: CIS_Apple_macOS_26_Tahoe_Benchmark_v1.0.0.pdf
---
# CIS Apple macOS 26 Tahoe Benchmark v1.0.0 (10-31-2025)

## Overview

Prescriptive hardening guidance for Apple macOS 26 Tahoe, developed via CIS consensus review in collaboration with the macOS Security Compliance Project (mSCP). Every recommendation is marked Automated or Manual; remediation may use Graphical, Terminal, or Configuration Profile methods, and enterprise-managed devices are best served by profiles (a mix of profile management and command-line hardening scripts is the most comprehensive solution). Audit all Automated and Manual recommendations — tooling often skips Manual items that are still in audit scope. Sibling edition: [[grc-frameworks/cis-benchmarks/cis-macos-15-sequoia]].

## Profile Applicability

### Level 1
- Practical and prudent; provides a clear security benefit
- Does not inhibit the utility of the technology beyond acceptable means

### Level 2
- Extends the Level 1 profile (not a standalone profile)
- For environments or use cases where security is paramount, or as defense in depth
- May negatively inhibit utility or performance

This edition defines only Level 1 and Level 2 — no Desktop/Server profile splits.

## 1. Updates, Patches and Additional Security Software

| Control | Level | Check |
|---|---|---|
| 1.1 Ensure Apple-provided Software Updates Are Installed (Automated) | L1 | `defaults read /Library/Preferences/com.apple.SoftwareUpdate LastFullSuccessfulDate` must be within 30 days; no pending `RecommendedUpdates`; remediate with `softwareupdate -i -a` (add `-R` when a restart is required) |
| 1.2 Ensure Download New Updates When Available Is Enabled (Automated) | L1 | `com.apple.SoftwareUpdate` key `AutomaticDownload` = `true` |
| 1.3 Ensure Install of macOS Updates Is Enabled (Automated) | L1 | Install macOS updates selected under Software Update options |
| 1.4 Ensure Install Application Updates from the App Store Is Enabled (Automated) | L1 | App Store update install enabled |
| 1.5 Ensure Install Security Responses and System Files Is Enabled (Automated) | L1 | Security Responses and system file installation enabled |
| 1.6 Ensure Software Update Deferment Is Less Than or Equal to 30 Days (Automated) | L1 | `com.apple.applicationaccess` key `enforcedSoftwareUpdateDelay` ≤ 30; Apple has deprecated software deferment. No deferment profile passes |

## 2. System Settings — Apple Account, iCloud, Network

- **2.1.1.3** Ensure iCloud Drive Document and Desktop Sync Is Disabled (Automated, L2) — profile key `allowCloudDesktopAndDocuments` set to `<false/>` in `com.apple.applicationaccess`; prevents automatic sync of Desktop/Documents to a third-party public cloud.
- **2.1.1.1–2.1.1.6 / 2.1.2** Audit iCloud Passwords & Keychain, iCloud Drive, Security Keys Used With Apple Accounts, Freeform sync, Find My Mac, App Store Password Settings (Manual, L2) — evaluate against data residency and acceptable use requirements.
- **2.2.1** Ensure Firewall Is Enabled (Automated, L1) — `socketfilterfw --getglobalstate` returns enabled (State = 1 or 2); profile `com.apple.security.firewall` key `EnableFirewall` = `<true/>`. As of macOS 15 firewall logging is automatic; a separate logging recommendation was removed.
- **2.2.2** Ensure Firewall Stealth Mode Is Enabled (Automated, L1) — the computer does not respond to unsolicited probes; `socketfilterfw --getstealthmode` reports on. The `EnableStealthMode` key must be in the same profile as `EnableFirewall`.
- **2.3.1.1 / 2.3.1.2** Ensure AirDrop Is Disabled When Not Actively Transferring Files; Ensure AirPlay Receiver Is Disabled (Automated, L1).
- **2.3.3.1–2.3.3.7, 2.3.3.10** Ensure Screen Sharing, File Sharing, Printer Sharing, Remote Login, Remote Management, Remote Apple Events, Internet Sharing, and Bluetooth Sharing Are Disabled (Automated, L1). **2.3.3.8 / 2.3.3.9** Content Caching and Media Sharing disabled (L2). **2.3.3.11** Computer Name does not contain PII or protected organizational information (Manual, L2).
- **4.1** Ensure Bonjour Advertising Services Is Disabled (Automated, L2); **4.2** Ensure HTTP Server Is Disabled (Automated, L1); **4.3** Ensure NFS Server Is Disabled (Automated, L1).

## 3. Date & Time

- **2.3.2.1** Ensure Set Time and Date Automatically Is Enabled (Automated, L1) — `systemsetup -getusingnetworktime` reports `Network Time: On`. Correct time is required for Kerberos (may fail if off by more than 5 minutes), file timestamps, and log entries. Default server is time.apple.com; internal time servers are acceptable. Verify offset with `sntp <your.time.server>` between -270.x and 270.x seconds.
- **2.3.2.2** Ensure the Time Service Is Enabled (Automated, L1) — `launchctl list | grep -c com.apple.timed` returns 1. If timed has been disabled, assume the OS has been compromised, back up files, and do a clean install.

## 4. Privacy & Security (Gatekeeper, FileVault, Lockdown Mode)

- **2.6.5** Ensure Gatekeeper Is Enabled (Automated, L1) — allowlisting restricts downloaded applications from launching; since macOS 13 Gatekeeper checks every application on every launch, not just quarantined apps. `spctl --status` reports `assessments enabled`; GUI 'Allow apps downloaded from' set to 'App Store and identified developers'. Profile `com.apple.systempolicy.control` keys `AllowIdentifiedDevelopers` and `EnableAssessment` = `<true/>`.
- **2.6.6** Ensure FileVault Is Enabled (Automated, L1) — encrypts the boot volume, requiring a password or recovery key; use with a saved escrow key. `fdesetup status` reports `FileVault is On`. As of macOS 26 Tahoe the recovery key can be requested on demand for devices not connected to an MDM. Profile `com.apple.MCX` key `dontAllowFDEDisable` = `<true/>` is required to pass the audit.
- **2.6.7** Audit Lockdown Mode (Manual, L2) — for users at elevated risk of advanced targeted attacks.
- **2.6.8** Ensure an Administrator Password Is Required to Access System-Wide Preferences (Automated, L1) — authorizationdb sections such as `system.preferences`, `system.preferences.network`, and `system.preferences.startupdisk` set to authenticate the user with group admin.
- **2.6.1.1–2.6.1.3 / 2.6.2.1** Location Services enabled, location icon in Control Center, Location Services access audit, Full Disk Access audit (L2).
- **2.6.3.1–2.6.3.5 / 2.6.4** Ensure Share Mac Analytics, Improve Siri & Dictation, Improve Assistive Voice Features, 'Share with app developers', and Share iCloud Analytics Are Disabled; Ensure Limit Ad Tracking Is Enabled (L1).
- **5.3.1 / 5.3.2** Ensure all user storage APFS (and CoreStorage) volumes are encrypted (Manual, L1) — `diskutil ap list`; encrypt every volume with "(No specific role)". Preboot, Recovery, and VM role disks are excluded.

## 5. System Integrity and Anti-Malware

- **5.1.2** Ensure System Integrity Protection Status (SIP) Is Enabled (Automated, L1) — `csrutil status` reports enabled. SIP restricts access to System domain locations and runtime attachment to system processes; can only be enabled from the Recovery Partition. With SIP enabled, Library Validation cannot be disabled.
- **5.1.3** Ensure Apple Mobile File Integrity (AMFI) Is Enabled (Automated, L1) — `nvram -p | grep -c "amfi_get_out_of_my_way=1"` returns 0. AMFI is the kernel module enforcing code signing and library validation.
- **5.1.4** Ensure Signed System Volume (SSV) Is Enabled (Automated, L1).
- **5.10** Ensure XProtect Is Running and Updated (Automated, L1) — Apple's native signature-based antivirus; `xprotect status` reports launch and background scans enabled, `xprotect update` pulls latest signatures. XProtect can only be disabled while SIP is disabled — if it is off with SIP on, assume compromise and investigate.
- **6.3.1** Ensure Automatic Opening of Safe Files in Safari Is Disabled (Automated, L1) — profile `com.apple.Safari` key `AutoOpenSafeDownloads` = `<false/>`; guards against drive-by attacks that download and execute "safe" files.
- **6.3.3 / 6.3.4 / 6.3.6 / 6.3.7** Warn When Visiting a Fraudulent Website, Prevent Cross-site Tracking, Advertising Privacy Protection, Show Full Website Address in Safari (Automated, L1).
- **6.4.1** Ensure Secure Keyboard Entry Terminal.app Is Enabled (Automated, L1) — profile `com.apple.Terminal` key `SecureKeyboardEntry` = `<true/>` (system-wide profile is the compliant method); prevents keyloggers capturing Terminal input.

## 6. Auditing and Logging

| Control | Level | Check |
|---|---|---|
| 3.1 Ensure Security Auditing Is Enabled (Automated) | L1 | `launchctl list | grep -i auditd` shows `com.apple.auditd`; load via `launchctl load -w /System/Library/LaunchDaemons/com.apple.auditd.plist` and copy `audit_control.example`. auditd is deprecated (Big Sur) and off by default since Sonoma; an EndpointSecurity API tool is the suggested alternative |
| 3.2 Ensure Security Auditing Flags For User-Attributable Events Are Configured Per Local Organizational Requirements (Automated) | L2 | `flags:` in `/etc/security/audit_control` includes `aa`, `ad`, `-ex`, `-fm`, `-fr`, `-fw`, `lo` |
| 3.3 Ensure install.log Is Retained for 365 or More Days and No Maximum Size (Automated) | L1 | `/etc/asl/com.apple.install` has `ttl` ≥ 365 and no `all_max=` |
| 3.4 Ensure Security Auditing Retention Is Enabled (Automated) | L1 | `expire-after:60d OR 5G` in `/etc/security/audit_control` |
| 3.5 Ensure Access to Audit Records Is Controlled (Automated) | L1 | `/etc/security/audit_control` and `/var/audit` owned root:wheel, read-only, no macOS ACLs |
| 3.6 Audit Software Inventory (Manual) | L2 | Maintain auditable software inventory |
| 5.11 Ensure Logging Is Enabled for Sudo (Automated) | L1 | `Defaults log_allowed` in `/etc/sudoers.d/`; sudo unified-log logging is disabled by default since macOS 15 and should be enabled |

## 7. System Access, Authentication and Authorization

- **5.2.1** Password Account Lockout Threshold configured (Automated, L1) — Max Failed Attempts ≤ 5; profile `com.apple.mobiledevice.passwordpolicy` key `maxFailedAttempts` is the preferred method (`pwpolicy -setglobalpolicy` is deprecated).
- **5.2.2** Password Minimum Length ≥ 15 (Automated, L1). Where FileVault confidentiality dominates, a longer passphrase may suffice over added complexity.
- **5.2.3–5.2.6** Complex Password must contain alphabetic, numeric, special, and upper/lowercase characters (Manual, L2).
- **5.2.7 / 5.2.8** Password Age configured; Password History set to at least 24 (Automated, L1).
- **5.4** Ensure the Sudo Timeout Period Is Set to Zero (Automated, L1) — `Defaults timestamp_timeout=0` in `/etc/sudoers.d/` (survives OS updates, unlike editing sudoers directly); `/etc/sudoers.d` must be root:wheel. Note: organizations with heavy sudo use may choose to accept the risk.
- **5.5** Ensure a Separate Timestamp Is Enabled for Each User/tty Combo (Automated, L1) — tty tickets limit root access to a specific terminal.
- **5.6** Ensure the "root" Account Is Disabled (Automated, L1) — `dscl . -read /Users/root AuthenticationAuthority` returns no key; root shell set to `/usr/bin/false`; `dsenableroot -d` to disable.
- **5.7** Ensure an Administrator Account Cannot Login to Another User's Active and Locked Session (Automated, L1). Note: can conflict with Platform Single-Sign-On (PSSO) syncing.
- **5.8** Ensure a Login Window Banner Exists (Automated, L2) — `/Library/Security/PolicyBanner.txt` or `.rtf`, world-readable (`chmod o+r`).
- **5.9** Ensure the Guest Home Folder Does Not Exist (Automated, L1).
- **2.11.1** Inactivity Interval of 15 Minutes Or Less for the Screen Saver (Automated, L1); **2.11.2** Require Password After Screen Saver Begins or Display Is Turned Off for 5 Seconds or Immediately (Automated, L1); **2.11.3** Custom Message for the Login Screen (Automated, L1); **2.11.4** Login Window Displays as Name and Password (Automated, L1); **2.11.5** Show Password Hints Is Disabled (Automated, L1). **2.12.1** User accounts do not have a password hint (Automated, L1); **2.12.2** Audit Touch ID (Manual, L1).
- **2.13.1 / 2.13.2 / 2.13.3** Guest Account disabled, Guest Access to Shared Folders disabled, Automatic Login disabled (Automated, L1).

## 8. Backup, Power and Remaining System Settings

- **2.3.4.1** Ensure Backup Automatically Is Enabled If Time Machine Is Enabled (Automated, L2); **2.3.4.2** Ensure Time Machine Volumes Are Encrypted If Time Machine Is Enabled (Automated, L1).
- **2.10.1.1** Ensure the OS Is Not Active When Resuming from Standby (Intel) (Manual, L2); **2.10.1.2** Ensure Sleep and Display Sleep Is Enabled on Apple Silicon Devices (Automated, L2) — FileVault requires keys held in memory to resume; **2.10.2** Ensure Power Nap Is Disabled for Intel Macs (Automated, L1); **2.10.3** Ensure Wake for Network Access Is Disabled (Automated, L1).
- **2.5.1.1–2.5.1.4** Ensure External Intelligence Extensions, Writing Tools, Mail Summarization, and Notes Summarization Are Disabled (Automated, L1); **2.5.2.1 / 2.5.2.2** Ensure Siri and Listen for (Siri) Are Disabled (L1) — Apple Intelligence controls assume the organization utilizes AI-powered products.
- **2.9.1** Ensure Help Apple Improve Search Is Disabled (Automated, L1); **2.18.1** Ensure On-Device Dictation Is Enabled (Automated, L1); **2.4.1 / 2.8.1 / 2.15.1 / 2.17.1 / 6.1.1 / 6.5.1** Menu Bar and Control Center icons, Universal Control, Notifications, Internet Accounts for authorized use, Show All Filename Extensions, Passwords (Manual, L1). **2.7.1 / 2.7.2 / 2.14.1 / 2.16.1 / 6.2.1 / 6.3.2 / 6.3.5 / 6.3.8** Screen Saver corners, iPhone Mirroring, Game Center, Wallet & Apple Pay, Protect Mail Activity, Safari history, Hide IP Address, AutoFill (L2).

## 9. Supplemental Guidance

- The Benchmark was developed as part of a working group collaboration with the mSCP, authoritative through NIST SP 800-219 (Automated Secure Configuration Guidance from the mSCP).
- Apple Push Notification Service (APNs) is an encrypted and authenticated protocol; MDM tools use it to manage enrolled devices.
- Mobile configuration profiles are XML payloads (`.mobileconfig`) that automate settings, accounts, restrictions, and credentials; a profile can prevent even authorized technical personnel from changing a payload setting, so review profiles or plan temporary removal when changes are needed.
- Any recommendation that is user specific but has a profile that sets a system-wide setting is compliant only with the profile installed — user-specific settings moved to Additional Information no longer pass the audit.
- Recommendations are guidance, not requirements: exceptions are expected, must be documented cross-functionally for audit, and should be mitigated or formally risk-accepted.
- Latest version of the guide: https://www.cisecurity.org/cis-benchmarks/ ; profile reference: https://developer.apple.com/documentation/devicemanagement
