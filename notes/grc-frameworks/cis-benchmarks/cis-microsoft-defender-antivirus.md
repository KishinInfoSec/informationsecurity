---
title: cis-microsoft-defender-antivirus
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/windows, source/cis]
description: "CIS Microsoft Defender Antivirus Benchmark v1.0.0 checklist: real-time protection, exclusions, scanning, reporting, with levels."
source_pdf: CIS_Microsoft_Defender_Antivirus_Benchmark_v1.0.0.pdf
---

# CIS Microsoft Defender Antivirus Benchmark v1.0.0 (02-20-2026)

## Overview

CIS benchmark for hardening Microsoft Defender Antivirus on Windows workstations and servers. Recommendations carry Profile Applicability (Level 1/Level 2 × Workstation/Server), are marked Automated or Manual, and each includes Description, Rationale, Impact, Audit, Remediation (Group Policy UI path + registry location), Default Value, References, and CIS Controls v8 mappings. The benchmark states that automated assessment can skip Manual items, but *all* recommendations should be addressed.

## Profile definitions

- **Level 1 – Workstation/Server**: corporate/enterprise baseline; practical and prudent, clear security benefit, does not inhibit usability beyond acceptable means.
- **Level 2 – Workstation/Server**: extends L1 for high-security/sensitive-data environments; may reduce manageability/performance and limit remote management. L2 requires applying both L1 and L2 settings.

## Sections

| # | Area |
|---|------|
| 1.1 | Client Interface (hide local user access to client UI) |
| 1.2 | Device Control |
| 1.3 | Exclusions |
| 1.4 | Features |
| 1.5 | MAPS (cloud protection service reporting) |
| 1.6 | Microsoft Defender Exploit Guard (ASR rules, dangerous-website access) |
| 1.7 | MpEngine |
| 1.8 | Network Inspection System |
| 1.9 | Quarantine |
| 1.10 | Real-time Protection |
| 1.11 | Remediation (ransomware/brute-force/remote-encryption protection) |
| 1.12 | Reporting |
| 1.13 | Scan (schedule, types, e-mail scanning) |
| 1.14 | Security Intelligence Updates |
| 1.15 | Threats (default actions by alert level) |
| 1.16–1.18 | PUA detection, exclusion visibility, routine remediation |

## High-signal recommendations

### MAPS / cloud (1.5, 1.7)
- `Configure local setting override for reporting to Microsoft MAPS` → **Disabled** (L1 Server + Workstation) so cloud-reporting decisions stay centrally managed; registry `HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet:LocalSettingOverrideSpynetReporting` (REG_DWORD 0). Default: Disabled.
- `Send file samples when further analysis is required` → **Enabled: Send safe samples automatically** or higher.
- `Select cloud protection level` → **Enabled: Moderate blocking level** or higher (1.7.2).

### Attack Surface Reduction (1.6)
- `Configure Attack Surface Reduction rules` → **Enabled**; each individual ASR rule is a separate recommendation (1.6.1.2–1.6.1.17 set per-rule state to `1` = block mode), covering rules such as blocking credential stealing from LSASS, executable content from email/webmail, obfuscated/malicious scripts, process injections, ransomware, unsigned/persistence-from-USB, Office child processes, PSExec/WMI abuse, script-based persistence, and untrusted/blocked executable files.
- `Prevent users and apps from accessing dangerous websites` → **Enabled: Block** (1.6.3.1).

### Real-time protection (1.10)
- `Configure monitoring for incoming and outgoing file and program activity` → **Enabled: bi-directional (full on access)**.
- `Monitor file and program activity on your computer`, `Scan all downloaded files and attachments` → **Enabled**.
- `Turn on process scanning whenever real-time protection is enabled` → **Enabled**.
- OOBE real-time protection and Security Intelligence Updates stay enabled (1.10.2).

### Remediation / ransomware (1.11)
- `Configure Brute-Force Protection aggressiveness` → Enabled (recommended aggressiveness).
- `Configure Remote Encryption Protection Mode` → **Enabled: Audit** or stricter; related items tune how aggressively remote-encryption threats are blocked (1.11.1.x).

### Scanning (1.13)
- `Check for the latest virus and spyware security intelligence before running a scheduled scan` → Enabled.
- `Scan excluded files and directories during quick scans` → Enabled: 1.
- Scheduled scan: day of week set (Enabled: 0 or as chosen), scan type **Quick** by default, time-of-day/daily quick-scan hour set (Enabled: 1 or higher).
- `Trigger a quick scan after X days without any scans` → **Enabled: 7**.
- `Turn on e-mail scanning` → Enabled (1.13.11).

### Updates, threats, PUA (1.14–1.18)
- `Specify the interval to check for security intelligence updates` → **Enabled: 4 or fewer hours, but not 0**.
- Threat default actions are pinned per alert level for both real-time and scheduled scans (1.15.1–1.15.4).
- `Configure detection for potentially unwanted applications` → **Enabled: Block** (1.16).
- `Control whether exclusions are visible to local users` → **Enabled** (1.17) — exclusion transparency for local users.
- `Turn off routine remediation` → **Disabled** (1.18) — keep automatic remediation on.

## Deployment notes

- Most settings are Group Policy backed by `WindowsDefender.admx/adml` (Windows 8.1/Server 2012 R2 admin templates or newer); every recommendation documents the GP UI path plus its registry location for audit.
- Benchmarks map recommendations to CIS Controls v8 (e.g. 4.8 disable unnecessary services, 10.5 enable anti-exploitation features).

## Related

- [[grc-frameworks/cis-benchmarks/cis-windows-11-enterprise]] — OS-level hardening to pair with AV settings.
