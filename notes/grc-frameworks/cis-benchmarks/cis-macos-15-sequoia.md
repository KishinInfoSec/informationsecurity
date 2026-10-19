---
title: cis-macos-15-sequoia
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/macos, source/cis]
description: "CIS Apple macOS 15.0 Sequoia Benchmark v2.0.0 checklist: system and user policies, logging, firewall, encryption, with levels."
source_pdf: CIS_Apple_macOS_15.0_Sequoia_Benchmark_v2.0.0.pdf
---
# CIS Apple macOS 15.0 Sequoia Benchmark v2.0.0 (10-31-2025)

## Overview

The CIS Apple macOS 15.0 Sequoia Benchmark v2.0.0 provides prescriptive hardening guidance for macOS 15.0 Sequoia. Recommendations are designated as Automated or Manual for assessment; implementation may use command-line, graphical, or configuration profiles as applicable to managed environments.

## Profile Applicability

### Level 1
- Practical and prudent configuration baseline
- Provides clear security benefit
- Does not inhibit utility beyond acceptable means

### Level 2
- Extends Level 1 (not standalone)
- Intended for environments where security is paramount (defense in depth)
- May negatively impact utility or performance

## Key Sections and Representative Controls

### 1. System Updates and Software Integrity
- **1.1** Ensure Apple-provided Software Updates Are Installed (Automated, L1) — verify and apply available Apple updates; may require restart during maintenance windows.
- **1.5** Ensure Install Security Responses and System Files Is Enabled (Automated) — enable automatic installation of security responses and system files from Apple.
- **1.6** Ensure Software Update Deferment Is ≤ 30 Days (Automated) — limit update deferral per organizational policy.

### 2. System Settings — Apple Account & iCloud
- **2.1.1.3** Ensure iCloud Drive Document and Desktop Sync Is Disabled (Automated, L2 in that context) — prevent automatic sync of Desktop/Documents to iCloud where enterprise data policy prohibits it.
- **2.1.1.1–2.1.1.6** Audit iCloud Passwords & Keychain, iCloud Drive use, Security Keys, Freeform sync to iCloud, Find My Mac (Manual, L2) — evaluate against acceptable use/data residency requirements.
- **2.1.2** Audit App Store Password Settings (Manual, L2) — assess purchase/grace period and free purchase password requirements.

### 3. Network & Firewall
- **2.2.1** Ensure Firewall Is Enabled (Automated, L1) — enable macOS Application Layer Firewall (ALF); Packet Filter (PF) available for advanced cases.
- **2.2.2** Ensure Firewall Stealth Mode Is Enabled (Automated, L1) — reduce network fingerprinting by blocking ICMP replies/stealthing behavior.
- **4.1** Ensure Bonjour Advertising Services Is Disabled (Automated) — disable mDNS/Bonjour advertising where not required.
- **4.2** Ensure HTTP Server Is Disabled (Automated) — disable built-in web server if unused.
- **4.3** Ensure NFS Server Is Disabled (Automated) — disable NFS server if unused.

### 4. General & Time Synchronization
- **2.3.1.1** Ensure AirDrop Is Disabled When Not Actively Transferring Files (Automated) — limit ad-hoc file sharing.
- **2.3.1.2** Ensure AirPlay Receiver Is Disabled (Automated) — disable AirPlay reception unless needed.
- **2.3.2.1** Ensure Set Time and Date Automatically Is Enabled (Automated, L1) — use NTP/time service for accurate time.
- **2.3.2.2** Ensure the Time Service Is Enabled (Automated, L1) — ensure timed service is active for time synchronization.

### 5. Security Protections (Integrity & Encryption)
- **2.6.5** Ensure Gatekeeper Is Enabled (Automated, L1) — restrict app execution to App Store and identified developers.
- **2.6.6** Ensure FileVault Is Enabled (Automated, L1) — encrypt boot volume; maintain secure escrow/recovery key per policy.
- **2.6.7** Audit Lockdown Mode (Manual, L2) — consider for users at elevated risk of advanced attacks; can exclude specific trusted sites if needed.
- **5.1.2** Ensure System Integrity Protection Status (SIP) Is Enabled (Automated) — verify SIP active to protect system integrity.
- **5.1.3** Ensure Apple Mobile File Integrity (AMFI) Is Enabled (Automated) — enforce code signing/runtime integrity.

### 6. Auditing & Logging
- **3.1** Ensure Security Auditing Is Enabled (Automated) — enable audit subsystem.
- **3.2** Ensure Security Auditing Flags For User-Attributable Events Are Configured Per Local Organizational Requirements (Automated) — configure audit flags to meet policy.
- **3.3** Ensure install.log Is Retained for 365 or More Days and No Maximum Size (Automated) — retain installation logs with appropriate retention.
- **3.4** Ensure Security Auditing Retention Is Enabled (Automated) — configure audit log retention.
- **3.5** Ensure Access to Audit Records Is Controlled (Automated) — restrict access to audit artifacts.
- **3.6** Audit Software Inventory (Manual) — maintain auditable software inventory.

### 7. Management Notes
- Recommendations can be enforced via configuration profiles in managed environments; profiles may restrict changes by authorized personnel.
- Some controls are user-specific in effect; profile-based enforcement establishes system-wide compliance posture where applicable.
- Organizations should evaluate exceptions, document them, and prioritize remediation based on risk/time/cost.

## Notes
- Benchmark tested against target platform context in the document; version-specific behaviors apply (macOS 15.0 Sequoia, v2.0.0).
- Implementation details (exact commands, profile keys, audit procedures) are defined per control in the source benchmark.
- No URLs were fabricated; any URLs appearing in the original PDF context are referenced by their presence in the source material only where retained per policy.