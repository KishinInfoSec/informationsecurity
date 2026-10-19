---
title: bhis-intro-to-network-penetration-testing
tags: [reconnaissance, type/methodology, phase/recon, phase/enumeration, phase/exploitation, platform/network, source/bhis]
description: "BHIS webcast: pentest frameworks, OSINT through exploitation phases, internal/external/web/credential testing tools, and reporting."
source_pdf: SLIDES_Introduction-to-Network-Penetration-Testing-v2.pdf
---

# Introduction to Network Penetration Testing

## Frameworks

- **NIST CSF**, **OSSTMM** (peer-reviewed methodology and metrics), **PTES** (comprehensive assessment standard), **OWASP CPT Framework** (continuous/automated testing), **PTF** (TrustedSec's Python tool-installation framework for Debian/Ubuntu/Arch).
- **MITRE ATT&CK:** knowledge base of real-world adversary TTPs; used for threat modeling, red/blue teaming, control validation and IR improvement.

## Core testing phases

OSINT → live asset discovery → port discovery → vulnerability identification → exploitation (without disrupting service or locking out accounts) → web service analysis → password spraying/credential stuffing (only if approved).

## OSINT

Cloud enumeration (AADInternals, AirCross, CloudEnum), document metadata enumeration (SerpAPI), user/email enumeration (Hunter.io, LinkedIn), attack surface mapping (ARIN, Amass, DNSTwist, SubFinder, Cert.sh, DNS-Triage). Always verify scope with the customer before any active discovery — discovered assets may be out of scope.

## Live discovery and scanning

- **Masscan:** very fast large-range port sweeps for initial broad discovery.
- **Nmap:** detailed discovery, service version detection, OS fingerprinting, scriptable vulnerability checks.
- **Asset verification:** confirm ownership via ARIN records, certificate info and banners before scanning or exploiting — never hit a system that is not actually in scope.
- **Vulnerability scanners:** Nessus/Tenable (extensive plugin library), Nuclei (fast, YAML templates, open source), Qualys (cloud continuous monitoring), Nexpose (Rapid7 on-prem).

## External network testing

- Software version analysis against CVE/NVD using Nmap fingerprinting, Wappalyzer, httpx, Nmap scripts.
- Cryptographic configuration review: Testssl.sh, Qualys SSL Labs, for weak ciphers, expired certs, bad trust chains.
- SSH review: SSH-Audit, Nmap scripts, for insecure protocols/auth methods.
- Sensitive-service discovery checklist: should it be exposed, is it a management login portal, is MFA present, is it necessary for functionality.

## Internal network testing

- Database testing: MSSQL and MySQL scans for misconfigurations, weak credentials, privesc paths.
- Default credentials: a fundamental step across network devices, servers and applications.
- File services: anonymous FTP, NFS shares, SMB null sessions, SMBv1, SMB signing, share enumeration.
- Printers: often have web UIs and default creds, are AD-joined, can leak sensitive print-job history; be careful — scanning can trigger unwanted print jobs on older models.
- Network-layer analysis: IPv6, SLAAC, LLMNR, NBNS, mDNS via tcpdump capture; Responder, Pretender, Pcredz, Eavesarp for credential/protocol abuse.

## Web application triage

- EyeWitness/GoWitness for quick screenshot overviews; Feroxbuster/GoBuster for hidden content; prioritize OWASP Top 10 categories (injection, broken access control, misconfiguration). Deeper scanning: Nuclei, Burp Suite, Nikto.

## Credential attacks

- Get the client's password policy and lockout threshold before spraying; target employee accounts only, never mixed customer/employee portals.
- A successful spray without access still validates alerting and rate-limit controls.
- MFA testing matters because MFA options vary widely; tools: FindMeAccess, MFASweep.
- External spraying: Burp Intruder, credmaster (note: AWS API Gateway use for testing violates AWS policy), DomainPasswordSpray.
- Internal spraying: Talon, NetExec, Kerbrute, Pre2k.

## Avoiding rabbit holes

Fulfil the statement-of-work objectives first; set a specific goal before starting; time-box each technique (pivot after ~5 minutes if unproductive); keep a running to-do list of things to try and revisit.

## Exploitation discipline

Never run an exploit blindly — review the code to understand exactly what it does and what side effects occur; assess whether it could crash the target; test in a lab replica first where possible. Ask: what's the end goal here?

## Reporting

Tailor to both technical and business audiences (how vs why it matters); structure as facts, then context, then opinions; use screenshots to illustrate, not decorate; the report is the primary deliverable — "your report matters more than your hacking."

## Building skills

- Platforms: Antisyphon workshops, Hack The Box, TryHackMe.
- Home lab: a hypervisor (VMware Workstation/Player, VirtualBox, Proxmox, Parallels), vulnerable targets (Metasploitable, OWASP BWAPP, DVWA, VulnHub VMs), 16GB+ RAM (32GB recommended), isolated/segmented lab network with no internet exposure for lab VMs, Kali Linux or Parrot OS as the attack platform.
- Staying current: CVE feeds and vendor bulletins, Infosec community (X/Twitter, LinkedIn, Discord, r/netsec), conferences and meetups, podcasts (Darknet Diaries, Risky Business, Security Now), BHIS Newscast and similar webcasts.

## Defender/Attacker takeaways

- Defender: the internal network-layer checklist (LLMNR/NBNS/mDNS exposure, SMB signing, null sessions) is a fast, high-value internal hardening pass.
- Defender: printer web interfaces and stored print logs are an underrated internal data-exposure risk.
- Attacker: rabbit-hole discipline (time-boxing, a running to-do list) is as much a professional skill as any tool on this list.

## Source

BHIS webcast "Introduction to Network Penetration Testing" by Ashley Knowles (13 years in cyber security, vulnerability and risk management, internal red team lead, BHIS consultant).

## Related

- [[vulnerability-research/scanning/nuclei]]
- [[reconnaissance/passive-recon/dns-recon-and-route-mapping]]
- [[reconnaissance/active-recon/stealth-scanning-strategies]]
- host-enumeration
- [[password-cracking/hydra]]
- [[web-app-pentesting-notes/web-app-pentesting-tools/burp-suite]]
- [[web-app-pentesting-notes/web-app-pentesting-tools/fuzzing-ffuf-tool]]
