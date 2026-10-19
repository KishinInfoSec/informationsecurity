---
title: cis-palo-alto-firewall-11
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/network, source/cis]
description: "CIS Palo Alto Networks Firewall 11 Benchmark v1.2.0 checklist: admin access, management plane, policies, logging, with levels."
source_pdf: CIS_Palo_Alto_Firewall_11_Benchmark_v1.2.0.pdf
---

# CIS Palo Alto Networks Firewall 11 Benchmark v1.2.0 (10-03-2025)

## Overview

- **Target:** Palo Alto firewalls running PAN-OS version 11.x; the guide was tested against PAN-OS v11.x.
- **Benchmark version:** v1.2.0 (10-03-2025); change history entries are dated Oct 3, 2025.
- **Recommendations:** 79 total — 62 Automated, 17 Manual; every recommendation carries exactly one profile (Level 1 or Level 2) and one assessment status. Automated means the control can be fully validated to a pass/fail state; Manual means all or some steps need hands-on validation, and Manual items are typically in scope for audits.
- **Tooling:** CIS-CAT Pro Assessor and CIS Benchmarks Certified 3rd Party Tooling automate the Automated recommendations; all recommendations must still be addressed.
- **Exceptions:** recommendations are guidance, not requirements — exceptions are expected, should be reviewed cross-functionally and documented for audit, with a mitigation plan or a documented accepted-risk decision.
- **Notation:** titles below are as published in the benchmark, suffixed with profile (L1/L2) and assessment status (Automated/Manual). Rationale, audit and remediation procedures live in the official benchmark.

## Profile applicability

- **Level 1:** items that are practical and prudent, provide a clear security benefit, and do not negatively inhibit the utility of the technology beyond acceptable means.
- **Level 2:** extends the "Level 1" profile and is not a standalone profile — items are intended for environments or use cases where security is paramount, act as a defense in depth measure, and may negatively inhibit the utility or performance of the technology.
- **In this benchmark:** 69 Level 1 items and 10 Level 2 items (1.1.1.2, 1.2.5, 1.6.3, 1.7.1, 2.1, 2.2, 5.7, 6.16, 7.1, 8.3); assess Level 1 first, then add Level 2 on top.
- **MFA:** there is no standalone MFA recommendation here — multi-factor authentication appears only in the mapped CIS Controls guidance (v8 5.2: an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA). Local password rules below still apply (minimum length 12).

## Recommendation checklist

### 1 Device Setup (26)
Covers login banners, logging, management interfaces, password strength, device management authentication, SNMP polling and device services.
#### 1.1 General Settings
- [ ] 1.1.1.1 Syslog logging should be configured — L1 · Automated
- [ ] 1.1.1.2 SNMPv3 traps should be configured — L2 · Automated
- [ ] 1.1.2 Ensure 'Login Banner' is set — L1 · Automated
- [ ] 1.1.3 Ensure 'Enable Log on High DP Load' is enabled — L1 · Automated
#### 1.2 Management Interface Settings
- [ ] 1.2.1 Ensure 'Permitted IP Addresses' is set to those necessary for device management — L1 · Manual
- [ ] 1.2.2 Ensure 'Permitted IP Addresses' is set for all management profiles where SSH, HTTPS, or SNMP is enabled — L1 · Manual
- [ ] 1.2.3 Ensure HTTP and Telnet options are disabled for the management interface — L1 · Automated
- [ ] 1.2.4 Ensure HTTP and Telnet options are disabled for all management profiles — L1 · Manual
- [ ] 1.2.5 Ensure valid certificate is set for browser-based administrator interface — L2 · Manual
#### 1.3 Minimum Password Requirements
- [ ] 1.3.1 Ensure 'Minimum Password Complexity' is enabled — L1 · Automated
- [ ] 1.3.2 Ensure 'Minimum Length' is greater than or equal to 12 — L1 · Automated
- [ ] 1.3.3 Ensure 'Minimum Uppercase Letters' is greater than or equal to 1 — L1 · Automated
- [ ] 1.3.4 Ensure 'Minimum Lowercase Letters' is greater than or equal to 1 — L1 · Automated
- [ ] 1.3.5 Ensure 'Minimum Numeric Letters' is greater than or equal to 1 — L1 · Automated
- [ ] 1.3.6 Ensure 'Minimum Special Characters' is greater than or equal to 1 — L1 · Automated
- [ ] 1.3.7 Ensure 'Required Password Change Period' is less than or equal to 90 days — L1 · Automated
- [ ] 1.3.8 Ensure 'New Password Differs By Characters' is greater than or equal to 3 — L1 · Automated
- [ ] 1.3.9 Ensure 'Prevent Password Reuse Limit' is set to 24 or more passwords — L1 · Automated
- [ ] 1.3.10 Ensure 'Password Profiles' do not exist — L1 · Automated
#### 1.4 Authentication Settings (for Device Mgmt)
- [ ] 1.4.1 Ensure 'Idle timeout' is less than or equal to 10 minutes for device management — L1 · Automated
- [ ] 1.4.2 Ensure 'Failed Attempts' and 'Lockout Time' for Authentication Profile are properly configured — L1 · Automated
#### 1.5 SNMP Polling Settings
- [ ] 1.5.1 Ensure 'V3' is selected for SNMP polling — L1 · Automated
#### 1.6 Device Services Settings
- [ ] 1.6.1 Ensure 'Verify Update Server Identity' is enabled — L1 · Automated
- [ ] 1.6.2 Ensure redundant NTP servers are configured appropriately — L1 · Automated
- [ ] 1.6.3 Ensure that the Certificate Securing Remote Access VPNs is Valid — L2 · Manual
#### 1.7 VPN Settings
- [ ] 1.7.1 Enabling Post-Quantum (PQ) on IKEv2 VPNs — L2 · Manual

### 2 User Identification (8)
IP address mapping and User-ID functionality.
- [ ] 2.1 Ensure that IP addresses are mapped to usernames — L2 · Automated
- [ ] 2.2 Ensure that WMI probing is disabled — L2 · Automated
- [ ] 2.3 Ensure that User-ID is only enabled for internal trusted interfaces — L1 · Automated
- [ ] 2.4 Ensure that 'Include/Exclude Networks' is used if User-ID is enabled — L1 · Automated
- [ ] 2.5 Ensure that the User-ID Agent has minimal permissions if User-ID is enabled — L1 · Manual
- [ ] 2.6 Ensure that the User-ID service account does not have interactive logon rights — L1 · Automated
- [ ] 2.7 Ensure remote access capabilities for the User-ID service account are forbidden. — L1 · Manual
- [ ] 2.8 Ensure that security policies restrict User-ID Agent traffic from crossing into untrusted zones — L1 · Automated

### 3 High Availability (3)
- [ ] 3.1 Ensure a fully-synchronized High Availability peer is configured — L1 · Automated
- [ ] 3.2 Ensure 'High Availability' requires Link Monitoring and/or Path Monitoring — L1 · Automated
- [ ] 3.3 Ensure 'Passive Link State' and 'Preemptive' are configured appropriately — L1 · Automated

### 4 Dynamic Updates (2)
- [ ] 4.1 Ensure 'Antivirus Update Schedule' is set to download and install updates hourly — L1 · Automated
- [ ] 4.2 Ensure 'Applications and Threats Update Schedule' is set to download and install updates at daily or shorter intervals — L1 · Automated

### 5 WildFire (8)
WildFire is the cloud-based malware detection, analysis and blocking service native to Palo Alto next generation firewalls.
- [ ] 5.1 Ensure that WildFire file size upload limits are maximized — L1 · Automated
- [ ] 5.2 Ensure a WildFire Analysis profile is enabled for all security policies — L1 · Automated
- [ ] 5.3 Ensure forwarding of decrypted content to WildFire is enabled — L1 · Automated
- [ ] 5.4 Ensure all WildFire session information settings are enabled — L1 · Automated
- [ ] 5.5 Ensure alerts are enabled for malicious files detected by WildFire — L1 · Automated
- [ ] 5.6 Ensure 'WildFire Update Schedule' is set to download and install updates in real-time — L1 · Automated
- [ ] 5.7 Choosing Wildfire public cloud region — L2 · Manual
- [ ] 5.8 Ensure that 'Inline Cloud Analysis' on Wildfire profiles is enabled — L1 · Manual

### 6 Security Profiles (25)
Antivirus, anti-spyware, Vulnerability Protection, URL filtering and logging, data filtering and Zone Protection Profiles.
- [ ] 6.1 Ensure that antivirus profiles are set to reset-both on all decoders except 'imap' and 'pop3' — L1 · Automated
- [ ] 6.2 Ensure a secure antivirus profile is applied to all relevant security policies — L1 · Manual
- [ ] 6.3 Ensure an anti-spyware profile is configured to block on specified spyware severity levels, categories, and threats — L1 · Automated
- [ ] 6.4 Ensure DNS sinkholing is configured on all anti-spyware profiles in use — L1 · Automated
- [ ] 6.5 Ensure a secure anti-spyware profile is applied to all security policies permitting traffic to the Internet — L1 · Automated
- [ ] 6.6 Ensure a Vulnerability Protection Profile is set to block attacks against critical and high vulnerabilities, and set to default on medium, low, and informational vulnerabilities — L1 · Automated
- [ ] 6.7 Ensure a secure Vulnerability Protection Profile is applied to all security rules allowing traffic — L1 · Automated
- [ ] 6.8 Ensure that PAN-DB URL Filtering is used — L1 · Automated
- [ ] 6.9 Ensure that URL Filtering uses the action of "block" or "override" on the URL categories — L1 · Automated
- [ ] 6.10 Ensure that access to every URL is logged — L1 · Automated
- [ ] 6.11 Ensure all HTTP Header Logging options are enabled — L1 · Automated
- [ ] 6.12 Ensure secure URL filtering is enabled for all security policies allowing traffic to the Internet — L1 · Automated
- [ ] 6.13 Ensure alerting after a threshold of credit card or Social Security numbers is detected is enabled — L1 · Automated
- [ ] 6.14 Ensure a secure Data Filtering profile is applied to all security policies allowing traffic to or from the Internet — L1 · Automated
- [ ] 6.15 Ensure that a Zone Protection Profile with an enabled SYN Flood Action of SYN Cookies is attached to all untrusted zones — L1 · Automated
- [ ] 6.16 Ensure that a Zone Protection Profile with tuned Flood Protection settings enabled for all flood types is attached to all untrusted zones — L2 · Automated
- [ ] 6.17 Ensure that all zones have Zone Protection Profiles with all Reconnaissance Protection settings enabled, tuned, and set to appropriate actions — L1 · Automated
- [ ] 6.18 Ensure all zones have Zone Protection Profiles that drop specially crafted packets — L1 · Automated
- [ ] 6.19 Ensure that User Credential Submission uses the action of "block" or "continue" on the URL categories — L1 · Automated
- [ ] 6.20 Ensure that 'Wildfire Inline ML Action' on antivirus profiles are set to reset-both on all decoders except 'imap' and 'pop3' — L1 · Manual
- [ ] 6.21 Ensure that 'Wildfire Inline ML' on antivirus profiles are set to enable for all file types — L1 · Automated
- [ ] 6.22 Ensure that 'Inline Cloud Analysis' on Vulnerability Protection profiles are enabled if 'Advanced Threat Prevention' is available — L1 · Automated
- [ ] 6.23 Ensure that 'Cloud Inline Categorization' on URL Filtering profiles are enabled if 'Advanced Threat Prevention' is available — L1 · Automated
- [ ] 6.24 Ensure that 'Inline Cloud Analysis' on Anti-Spyware profiles are enabled if 'Advanced Threat Prevention' is available — L1 · Manual
- [ ] 6.25 Ensure that 'DNS Policies' is configured on Anti-Spyware profiles if 'DNS Security' license is available — L1 · Manual

### 7 Security Policies (4)
Application and service security policy hygiene.
- [ ] 7.1 Ensure application security policies exist when allowing traffic from an untrusted zone to a more trusted zone — L2 · Automated
- [ ] 7.2 Ensure 'Service setting of ANY' in a security policy allowing traffic does not exist — L1 · Automated
- [ ] 7.3 Ensure 'Security Policy' denying any/all traffic to/from IP addresses on Trusted Threat Intelligence Sources Exists — L1 · Automated
- [ ] 7.4 Ensure that logging is enabled on built-in default security policies — L1 · Manual

### 8 Decryption (3)
SSL Forward Proxy and SSL Inbound Inspection policy coverage.
- [ ] 8.1 Ensure 'SSL Forward Proxy Policy' for traffic destined to the Internet is configured — L1 · Automated
- [ ] 8.2 Ensure 'SSL Inbound Inspection' is required for all untrusted traffic destined for servers using SSL or TLS — L1 · Manual
- [ ] 8.3 Ensure that the Certificate used for Decryption is Trusted — L2 · Manual

## Source

CIS Palo Alto Firewall 11 Benchmark v1.2.0 (10-03-2025), Center for Internet Security.

## Related

- [[grc-frameworks/cis-benchmarks/cis-aws-foundations]]
- [[network-security/installing-and-configuring-network-based-ids-in-ubuntu-suricata]]
