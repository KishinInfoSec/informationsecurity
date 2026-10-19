---
title: bhis-active-defense-in-the-age-of-ai-class-notes
tags: [security-operations, active-defense, type/reference, phase/detection, source/bhis]
description: "Day-by-day labs, slide ranges and takeaways from the 4-day Antisyphon class Active Defense and Cyber Deception in the Age of AI."
source_pdf: Day 1 Active Defense and Cyber Deception in the Age of AI.pdf
---

# Active Defense and Cyber Deception in the Age of AI: Class Notes (Days 1-4)

Handouts from John Strand's four-day Antisyphon class (June 29 to July 2, 2026). Each day's PDF lists the recording, labs, shared resources and short takeaways. The slide content itself is summarized in [[security-operations/active-defense/bhis-active-defense-foundations-and-threat-emulation]], [[security-operations/active-defense/bhis-active-defense-annoyance-and-honeypots]] and [[security-operations/active-defense/bhis-active-defense-attribution-and-cyber-deception]].

## Schedule and labs

| Day | Date | Slides | Labs |
|---|---|---|---|
| 1 | 2026-06-29 | 1-51 | n8n (part 1); Atomic Red Team and Bluespawn |
| 2 | 2026-06-30 | 52-89 | Advanced C2 PCAP analysis; AC Hunter 2 (RITA); SpiderTrap; HoneyUser |
| 3 | 2026-07-01 | 90-130 | Honeyport (solve with AI in 30 minutes, solution at slide 100); Portspoof; Cowrie; Web honeypot |
| 4 | 2026-07-02 | 131-end | Beelzebub (RITA VM); Canary Tokens; Honey Share |

Lab write-ups live in the BHIS FreeLabFriday_Labs repository (n8n), the `strandjs/IntroLabs` repository (IntroClass tools: bluespawn, pcap, RITA, Spidertrap, honeyuser, Portspoof, Cowrie, webhoneypot, honeyshare) and `strandjs/SOC_Analyst_Labs` (section 08 deception systems: Beelzebub, Canary Token labs).

## Takeaways written in class

- Do not get attached to your VMs; destroy them when idle to save credits.
- Talk to your lawyer; do not put malware where everyone can reach it; learn from other people's cases; use warning banners.
- It is illegal to set lethal traps on your own property.
- Active defense is an engaged defense; segment your network.
- Poison versus venom: with poison you touched it, with venom it reached out and touched you. Tell your pentest team where the deception lives.
- If it is free, you (or your information) are the product.
- Threat hunting is sometimes shortened to "thrunting".

## Tools and projects mentioned

- Detection and emulation: Atomic Red Team, Bluespawn, Caldera, RITA / AC-Hunter, LimaCharlie, MITRE Engage.
- Deception: Canarytokens, OpenCanary, Cowrie, Portspoof, TrustedSec Artillery, weblabyrinth, SpiderTrap, Beelzebub, HoneyBadger, the ADHD (Active Defense Harbinger Distribution) VM.
- Scanning and orchestration: masscan, naabu, n8n, Tailscale, Knocknoc, Netbird, Zscaler (network access options discussed in class).
- Defender toolkit links shared: CredDefense Toolkit, Backdoors and Breaches card game, Velociraptor and network threat hunting courses.
- AI context: local/private LLM talks, a threat hunting in the agentic age session, the AI SecOps podcast and a "do not outsource analysis to AI" article.

## Book recommendations

- *Takedown* (the pursuit and capture of Kevin Mitnick, by the man who did it) and *Offensive Countermeasures*.

## Source

Antisyphon Training class handouts for "Active Defense and Cyber Deception in the Age of AI" (Days 1-4), presenter John Strand, with BHIS/Antisyphon staff links. Dates from the handout headers.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-threat-hunting-tools]]
- [[threat-hunting-research/network-data/hunting-the-undetected]]
- [[miscellaneous/enterprise-agentic-ai-platform]]
- [[threat-hunting-research/attribution]]
