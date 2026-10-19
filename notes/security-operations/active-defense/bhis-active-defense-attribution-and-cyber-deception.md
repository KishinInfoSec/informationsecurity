---
title: bhis-active-defense-attribution-and-cyber-deception
tags: [security-operations, active-defense, type/methodology, phase/detection, source/bhis]
description: "BHIS ADCD part 3: legal cases, attribution against Tor, Canarytokens, Word web bugs, AD honey accounts and shares, HoneyBadger."
source_pdf: ACM_2DayJune_2026.pdf
---

# Active Defense: Legal Issues, Attribution and Cyber Deception

Part 3 of 3 from the BHIS/Antisyphon active defense course deck (slides 135-218). Earlier parts: [[security-operations/active-defense/bhis-active-defense-foundations-and-threat-emulation]] and [[security-operations/active-defense/bhis-active-defense-annoyance-and-honeypots]]. Class-day lab list: [[security-operations/active-defense/bhis-active-defense-in-the-age-of-ai-class-notes]].

## Legal issues (case law highlights)

- There is little settled case law; the trend matters more than any single ruling.
- **US v. Heckenkamp:** a university sysadmin accessed a threatening machine; the student's consent to network terms justified it.
- **Susan v. Absolute:** tracking software that took photos and intercepted communications of a stolen-laptop user crossed wiretap laws; tracking IP or location is a different thing from intercepting content. Absolute settled.
- **Conxion (1999):** a host reflected a DoS back at the attackers with a rewrite rule and was not prosecuted, but "not prosecuted" is not "legal".
- **Microsoft vs Waledac botnet (2010):** civil ex parte order to take over domains, then "other technical measures".
- Use your warning banner: it documents consent and permission checks, and can authorise access checks (VPN or NAC posture scripts can collect information about a connecting system).
- Callbacks you already accept every day: software updates, licence checks, phone tracking.
- **Hallmarks of legality:** discuss, document, plan, consult, do not hide, do not be evil. Options are annoyance, attribution, attack; the deck stays with the first two.

## Attribution

- Why bother: against nation-states you rarely catch the actor, but you learn what they want and what they already have, which sizes your defenses. Active defense provides threat intelligence.
- Attackers use indirection: Tor, botnets, SOCKS5 and proxychains (even Nmap, Nessus and Metasploit through proxies).
- Scan behavior leaks: a ping-sweep style scan sends ICMP, SYN to 443, ACK to 80 and an ICMP timestamp from the real source; a TCP connect scan through proxychains (`proxychains nmap -Pn -sT -p 80 <host>`) is the "right way" for the attacker. Misconfigured proxying exposes the real address.

## Canarytokens and honeytokens

- Canarytokens (from Thinkst): create tokens that alert on use (web, DNS, document, cloned site, AWS key, and others). Webhooks can feed n8n.
- You can use the hosted service (embed an iframe or an MD5-keyed callback) or run the engine yourself (custom DNS server, results database).
- Placement ideas: a `robots.txt` entry pointing at a tempting directory, cloned sites, Word documents on shares, compromised systems, or sent to spammers.
- Token variants shown: cloned-website token, Wi-Fi geolocation (collects nearby access point data via `netsh wlan`), and Word documents.
- Lab: Canarytokens (day 4).

## Word web bugs (honeydocs)

- A document that references a URL on your server; opening it triggers a direct connection that reveals the opener's IP address. No macros needed.
- Works with Word, LibreOffice Writer, AbiWord and Apple TextEdit in different forms; Canarytoken Word docs work less well on Linux document processors.
- Minimal pattern: HTML with an invisible 1x1 `<img>` and a stylesheet link pointing at a `web-bug-server` endpoint with an id parameter.
- Enterprise use: a "sensitive" file an intruder downloads gives you their IP and helps law enforcement and threat intelligence, with no persistent access and from your own stolen intellectual property.
- Psychology matters: most active defense is 80-90% thinking about what entices an attacker.

## Cyber deception on the cheap

- Commercial vendors named: Javelin Networks, Cymmetria, Illusive Networks, Attivo Networks, TrapX, Acalvio.
- Goal: stand up deception and attribution components in under half a day.
- Active Directory: a **HoneyAdmin** account that is obvious (admin-looking name), logon hours disabled so legitimate use is impossible, a cheap SIEM (Kiwi syslog) and alerts on logon attempts and password-spray patterns against it.
- **HoneyShares / honeydocs:** shares with tempting content and alerting; lab provided. Related tool: Deploy-Deception (PowerShell) for forging AD trust objects.
- **Infinitely recursive Windows directories:** slow exfiltration and some tools (`dir /S`, Meterpreter listings) loop; can also crash services such as backups, so test carefully.

## HoneyBadger and location macros

- HoneyBadger (Tim Tomes) records an attacker's geolocation using, in order of quality: nearby Wi-Fi access point details sent to a geolocation API, browser permission prompt, then IP geolocation (spoofable by VPN or Tor).
- Document macros can be generated to deliver location callbacks; `exe2vba.rb` (Metasploit tools directory) converts an executable into VBA for test documents.
- The trick is making the attacker believe running or opening it is okay.

## Case notes from the closing slides

- "Just two weeks at a bank" and "taking over a botnet" case studies, then a four-part summary: active vs passive defense, offensive countermeasures, deception equation, and "it's about getting into the fight". A capstone challenge set ends the course.

## Defender/Attacker takeaways

- Defender: write the banner, keep documentation, and stay at annoyance and attribution; callbacks should be passive (poison).
- Defender: seed tokens where attackers look (shares, robots.txt, AWS keys, documents) and send all alerts to one pipeline.
- Attacker view: open untrusted documents and tokens in a sandbox with no network identity, strip document metadata, and never run proxied scans through a misconfigured client.

## Source

BHIS/Antisyphon "Active Defense, Offensive Countermeasures, and Cyber Deception", John Strand with Bryce Galbraith and Paul Asadoorian (deck file dated June 2026). Slides 135-218 summarized; several AD and token slides are screenshots with no text, so those parts are summarized at title level.

## Related

- [[threat-hunting-research/attribution]]
- [[social-engineering/insider-attack]]
- [[cloud-pentesting/aws-pentesting/initial-access/leaked-secrets]]
- [[tunneling-and-exfiltration/pivoting/socks-ssh-pivoting]]
- [[reconnaissance/active-recon/stealth-scanning-strategies]]
- [[threat-hunting-research/active-directory/active-directory-architecture]]
