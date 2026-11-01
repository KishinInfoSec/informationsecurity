# Information Security Notes

A structured knowledge base of cybersecurity study notes covering offensive security, defensive operations, governance, and forensics. Built as an Obsidian vault and organized by topic so each area of study has its own easily browsable collection.

## About

This repository is a personal study vault for a range of security disciplines, including:

- **Offensive security** — penetration testing across Active Directory, web applications, APIs, cloud platforms, containers, mobile devices, and wireless networks
- **Defensive security** — threat hunting, SOC operations, network defense, and incident response
- **Governance, risk, and compliance** — summaries of major frameworks and standards (NIST, ISO 27001, SOC 2, PCI DSS, FedRAMP, GDPR, HIPAA)
- **Forensics** — digital forensics and incident response, from memory and network forensics to ransomware investigations
- **Certification prep** — notes aligned with CEH practical objectives
- **Emerging areas** — Web3/blockchain security, LLM and ML application security, and reverse engineering

## Repository Structure

Notes live under `notes/`, with one folder per topic and subfolders for deeper areas of study:

```
notes/
├── active-directory-pentesting/
├── api-testing/
├── apts/
├── ...
├── linux-security/
│   ├── persistence/
│   └── privilege-escalation/
└── ...
```

## Topic Index

| Topic                                                                                       | Description                                                                                                                       |     |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --- |
| [active-directory-pentesting](notes/active-directory-pentesting/)                           | AD attack paths, Kerberos attacks, credential attacks, automated tooling, and post-exploitation                                   |     |
| [ai](notes/ai/)                                                                             | AI-assistant tooling: a skill library for planning, PRD/story workflows, PR review, and code navigation, plus hooks for guardrails, logging, and session automation |     |
| [api-testing](notes/api-testing/)                                                           | API recon, endpoint discovery and interaction, mass assignment, server-side parameter pollution, and API vulnerability prevention |     |
| [apts](notes/apts/)                                                                         | Advanced Persistent Threat attack lifecycle and campaign structure                                                                |     |
| [awesome-hacking](notes/awesome-hacking/)                                                   | Curated lists of security resources and tools                                                                                     |     |
| [ceh](notes/ceh/)                                                                           | CEH practical preparation: tools, cryptography, network scanning, steganography, and engagement phases                            |     |
| [cloud-pentesting](notes/cloud-pentesting/)                                                 | Penetration testing for AWS and Azure environments                                                                                |     |
| [container-security](notes/container-security/)                                             | Docker and Kubernetes security                                                                                                    |     |
| [ctfs](notes/ctfs/)                                                                         | Capture-the-flag writeups, challenge solutions, and a general cheat sheet                                                         |     |
| [digital-forensics-and-incident-response](notes/digital-forensics-and-incident-response/)   | Windows, memory, network, email, and blockchain forensics; IR playbooks; ransomware investigations                                |     |
| [enumeration](notes/enumeration/)                                                           | Host enumeration, protocol and port enumeration, and web application enumeration                                                  |     |
| [evasion](notes/evasion/)                                                                   | AMSI bypass, WDAC/EDR evasion, and code obfuscation techniques                                                                    |     |
| [grc-frameworks](notes/grc-frameworks/)                                                     | Summaries of NIST CSF, ISO 27001, SOC 2, PCI DSS, FedRAMP, GDPR, HIPAA, SOX, CSA STAR, and CIS Benchmarks                         |     |
| [hacking-cheat-sheets](notes/hacking-cheat-sheets/)                                         | Quick references for reverse shells, SQL injection, command injection, Meterpreter, and PowerShell                                |     |
| [linux-security](notes/linux-security/)                                                     | Linux privilege escalation and persistence techniques                                                                             |     |
| [macos-security](notes/macos-security/)                                                     | Gaining access and endpoint security on macOS                                                                                     |     |
| [miscellaneous](notes/miscellaneous/)                                                       | Tools and setup guides: SSL/TLS decryption, GPG, OpenSSL, SSH, security VM setup, and related topics                              |     |
| [mobile-security](notes/mobile-security/)                                                   | Android and iOS application security                                                                                              |     |
| [network-security](notes/network-security/)                                                 | Protocol exploitation, network-based IDS with Suricata, SNMP authentication, and network AD topics                                |     |
| [owasp-top-10](notes/owasp-top-10/)                                                         | OWASP Top 10 (Web, 2021) coverage item by item, plus the LLM and machine learning top ten lists                                   |     |
| [password-cracking](notes/password-cracking/)                                               | John the Ripper, Hydra, cracking rules, custom wordlists, and Windows local password attacks                                      |     |
| [post-exploitation](notes/post-exploitation/)                                               | Mimikatz, PAC tampering, backdoors, Linux privilege escalation, living-off-the-land techniques, and Microsoft 365 tooling         |     |
| [reconnaissance](notes/reconnaissance/)                                                     | Passive and active recon, OSINT/doxing, and an intro to network penetration testing                                               |     |
| [reverse-engineering-and-malware-analysis](notes/reverse-engineering-and-malware-analysis/) | Binary and shellcode analysis, Android reverse engineering, and YARA rules                                                        |     |
| [scripting](notes/scripting/)                                                               | Scripting references for Bash, Python, Ruby, and Perl                                                                             |     |
| [security-operations](notes/security-operations/)                                           | SOC triage, data loss prevention, IR preparedness, data analytics, and active defense                                             |     |
| [social-engineering](notes/social-engineering/)                                             | Phishing detection bypass, MFA bypass, malicious files and USB drops, insider attacks, and 0-click attacks                        |     |
| [threat-hunting-research](notes/threat-hunting-research/)                                   | Hunting methodology, data collection and management, AD and network data sources, and attribution                                 |     |
| [tunneling-and-exfiltration](notes/tunneling-and-exfiltration/)                             | Tunneling, pivoting, port forwarding, and data exfiltration techniques                                                            |     |
| [vulnerability-research](notes/vulnerability-research/)                                     | Code review, CVE research, public exploit usage, and vulnerability scanning                                                       |     |
| [web-app-pentesting-notes](notes/web-app-pentesting-notes/)                                 | XSS/XSRF, SSTI, JWT attacks, GraphQL and NoSQL injection, race conditions, and Burp Suite tooling                                 |     |
| [web3-security](notes/web3-security/)                                                       | Blockchain audits, Web3 vulnerabilities, and smart contract hacking                                                               |     |
| [windows-security](notes/windows-security/)                                                 | Windows recon, exploitation, post-exploitation, and persistence                                                                   |     |
| [wireless-hacking](notes/wireless-hacking/)                                                 | Wi-Fi and Bluetooth attacks, and Zigbee security                                                                                  |     |

## Note Conventions

- Notes prefixed `bhis-` are derived from public Black Hills Information Security (BHIS) webcasts and courses
- Most topics store notes alongside nested subfolders for tools, techniques, or sub-disciplines
- Sensitive or licensed materials (course resources, payloads, benchmark files) are intentionally excluded via `.gitignore`

## Disclaimer

These notes are for educational purposes only. Use any techniques or knowledge contained here exclusively in environments you are authorized to test, such as labs, CTFs, or sanctioned engagements.
