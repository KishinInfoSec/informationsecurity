---
title: bhis-active-defense-annoyance-and-honeypots
tags: [security-operations, active-defense, type/tool, phase/detection, source/bhis]
description: "BHIS ADCD part 2: annoyance tactics, SpiderTrap, honey users, honeyports, Portspoof, Cowrie, Artillery, AI honeypots."
source_pdf: ACM_2DayJune_2026.pdf
---

# Active Defense: Annoyance, Honeypots and Honeyports

Part 2 of 3 from the BHIS/Antisyphon active defense course deck (slides 82-134). Concepts and legal framing are in [[security-operations/active-defense/bhis-active-defense-foundations-and-threat-emulation]]; attribution and tokens are in [[security-operations/active-defense/bhis-active-defense-attribution-and-cyber-deception]].

## Honeypot ideas

- A "honeything" is anything only an attacker should touch: honeytoken, honeyrecord, honeytable, honeycred, honeyport, honeydoc, honeypot, honeynet. Any interaction is malicious and gets an immediate response.
- Focus on **production** honeypots (find malicious internal systems/users, attacks AV and IDS miss, feed incident handling), not research honeypots that become time sinks.
- They tell you about attackers: skill, motivation, what they search for, what else they could reach.
- They detect what other tools miss, especially post-exploitation and trusted insiders.

## Annoyance tools and tricks

| Tool / idea | What it does |
|---|---|
| PHPIDS + PHP tarpit rule | Redirect detected attackers to a silly page; the deck debates whether taunting is wise |
| Server banner changes | Make the web server look like something else (change identity headers) |
| HoneyDNS | Zone full of records pointing at unused IP space; log, alert and optionally drop sources that query them |
| SpiderTrap | Generates endless links so crawlers (wget -m, scanners) loop forever; can feed it a directory wordlist; configure robots.txt so search engines are not trapped |
| Weblabyrinth | PHP SpiderTrap extension: random HTTP errors, an IDS-trigger string, politely turns away Googlebot |
| Portspoof | Returns random responses to service-identification probes so a service scan can take hours and results are unreliable |

## Honey users and OpenCanary

- **Honey users:** fake Domain Admin or service accounts, plus mailboxes or social profiles; write SIEM rules so any use alerts.
- **OpenCanary:** Python collection that emulates FTP, HTTP, SMB, SSH, Telnet and more; alerts by email, syslog or SMS.
- **Fail2Ban:** blocks IPs after repeated auth failures logged to auth.log; install it widely.

## Honeyports

A honeyport is a port that triggers an action (alert, blocklist) on connection.

- Lab goal: build an auto-drop script from the CLI (iptables DROP rule, bash loop, netcat listener, `cut`/`awk` to extract the IP). Build it for Linux and Windows to understand it even when you cannot install tools.
- Trigger behaviour: a plain `nmap` SYN scan shows the port open; a full connect scan (`-sT`) completes the handshake and triggers the block.
- Value: visibility where IDS/IPS are blind (normal protocols over open ports, zero-days); works in air-gapped networks; low interaction and low production impact.
- Risks: interfering with vulnerability scans (use exceptions or authenticated scanning); spoofed blocking of legitimate hosts needs a full established connection, which is hard to fake.
- Related tools: a PowerShell honeyport script; **Artillery** (TrustedSec) opens honeyports for common services (135/445, 1433, 5900) with file monitoring and email alerts, but the default port set is predictable.

## Cowrie / Kippo (SSH honeypot)

- Cowrie lets the attacker "log in" to a fake SSH service, capturing credentials and every command.
- Enterprise use: see what attackers want (backdoor, files, DDoS booter); compare failed-login usernames against valid domain accounts to find users who reuse work email on third-party sites that were breached.
- Lab: attack a partner's Cowrie, watch logs, then reverse roles; change the default password.

## Application-specific honeypots and fingerprinting

- Mimic uniform environments (for example SCADA) so the trap blends in, internally or on the perimeter (useful to show management that attacks happen).
- **Problem:** many honeypots are fingerprintable by default values, so scanners such as Nessus and Shodan flag them. Change defaults (for example Conpot serial number, system name, description).
- **AI on AI:** generate honey data dynamically with an LLM (Beelzebub supports SSH, HTTP, Telnet and MCP servers); hallucinations are a feature here.

## Defender/Attacker takeaways

- Defender: start with honeyports and honey users (cheap, near-zero false positives), route alerts to one place, and change default banners.
- Defender: avoid actions that could harm third parties; blocklisting source IPs is the safe response.
- Attacker view: consistent, scripted-looking service banners, endlessly deep directories and unusually permissive services are deception tells; time-box crawling and verify with a manual look.

## Source

BHIS/Antisyphon "Active Defense, Offensive Countermeasures, and Cyber Deception", John Strand with Bryce Galbraith and Paul Asadoorian (deck file dated June 2026). Slides 82-134 summarized here; class days 2 and 3 covered most of this material.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-threat-hunting-tools]]
- [[enumeration/protocols-and-ports/22-ssh]]
- [[enumeration/protocols-and-ports/445-smb]]
- [[reconnaissance/active-recon/stealth-scanning-strategies]]
- [[network-security/installing-and-configuring-network-based-ids-in-ubuntu-suricata]]
