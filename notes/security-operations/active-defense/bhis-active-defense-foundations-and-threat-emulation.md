---
title: bhis-active-defense-foundations-and-threat-emulation
tags: [security-operations, active-defense, type/methodology, phase/detection, source/bhis]
description: "BHIS ADCD part 1: active defense and deception concepts, legal footing, why defenses fail, threat emulation, n8n workflows."
source_pdf: ACM_2DayJune_2026.pdf
---

# Active Defense and Cyber Deception: Foundations and Threat Emulation

Part 1 of 3 from the BHIS/Antisyphon "Active Defense, Offensive Countermeasures, and Cyber Deception" course deck (slides 1-81). Part 2 covers [[security-operations/active-defense/bhis-active-defense-annoyance-and-honeypots]], part 3 covers [[security-operations/active-defense/bhis-active-defense-attribution-and-cyber-deception]]. Daily lab lists are in [[security-operations/active-defense/bhis-active-defense-in-the-age-of-ai-class-notes]].

## Core definitions

- **Active defense:** limited offensive action and counterattack to deny the adversary a contested position. Proactive and reactive; assumes the adversary is already inside.
- **Passive defense:** static measures that reduce likelihood or impact without taking the initiative.
- **Prevent / Detect / Respond:** prevention is ideal, detection is mandatory, detection without response is of little value.
- **Offensive countermeasures:** offensive techniques used with a defensive posture. The deck uses the Aikido analogy: redirect and block, never initiate.
- **Poison, not venom:** poison is something the attacker has to take or touch (a document, honeyport, honeypot); venom is injected into the attacker's system. Only do poison.
- **Cyber deception:** deliberately deceiving attackers to slow them and raise detection odds. Goal is `Dt + Rt < At` (detection time plus reaction time shorter than attack time). It complements other layers and does not replace them.
- **Disrupt the OODA loop:** observe-orient-decide-act; deception forces the attacker to re-observe and re-orient.
- Framing: **MITRE Engage** is the adversary-engagement framework the course maps to.

## Legal footing (summary)

- Vet tactics with legal, HR and management first; get a warrant where appropriate; never build lethal or damaging traps.
- Do not place malware where it is publicly reachable; prevent collateral damage; make the attacker come to you first.
- Use warning banners and terms of use that state monitoring and access checks; do not hide what you are doing.
- Full legal case discussion is in part 3.

## Why current strategies fail

- Prevention-heavy advice has not changed for years ("patch, strong passwords, anti-malware, firewalls") and now arrives labelled "next-gen AI".
- Good testing firms bypass these defenses routinely; nation-states are better funded.
- Expect compromise from zero-days, phishing, advanced malware and supply-chain issues. Compromise is acceptable; months of persistence and minutes of lateral movement are not.
- Offensive AI speeds up API fuzzing and post-exploitation (BloodHound, PingCastle-style enumeration), so lateral movement takes moments. This raises the need for deception.
- Basics still matter: AI is cheaper and better when you have the context fundamentals provide.

## Network-level controls the deck recommends

- Segment down to desktop level and between subnets; consider an "infected" VLAN.
- Treat the internal network as hostile: host firewalls set like a coffee-shop profile (block inbound, alert on attempts, exceptions for admin networks).
- Block SMB/RPC between subnets unless needed. Pass-the-Hash, Pass-the-Ticket and token impersonation still work and rarely trip IDS.
- Detect insiders: one account touching thousands of files or hundreds of hosts; plan attribution (see Word web bugs in part 3).

## Threat emulation

- Think post-exploitation, not just missing patches. Run free emulation tools and learn what you can actually detect.
- Tools named: Atomic Red Team, Caldera, Sigma-based detection, BloodHound, and commercial offerings.
- Warning: vendors may tune only to specific Atomic/MITRE test cases; a few modifications bypass them.
- Mindset shift from "can we be hacked?" to "what can we detect?": find gaps, fill them, move on.
- Lab: advanced C2 PCAP analysis, then RITA / AC-Hunter to find beaconing. Takeaway: signature on one Base64 string is easy to evade; allow-listing internet egress is stronger but often politically hard.

## AI and orchestration

- n8n example: auto-enrich alerts from Canarytokens, honeyports and honeypots, correlate, threshold, ticket, and hand a human one consolidated item.
- Think in workflows and cost: let AI do basic analysis first, or iterate with a feedback loop; for example let an agent run nmap or write a scanner.
- MCP servers expose tools to an agent (reactive); orchestration such as n8n wires tools together (proactive). Use both.
- Core deception data sources to parse: honeyports, Beelzebub, SpiderTrap, web honeypots.

## Safe setup (summary of slides 71-78)

- Never connect directly to a suspected attacker system before IR collection is done.
- Run deception callbacks on a third-party host and domain that is not attributable to your organization, behind an anonymizing proxy; all components (honeydocs, HoneyBadger, Canarytokens, honeyports, SpiderTrap) call back to one cloud-hosted orchestration system.
- Treat that infrastructure as disposable.

## Defender/Attacker takeaways

- Defender: assume breach, segment, firewall internally, instrument deception where attackers must touch it, and measure detection with emulation.
- Defender: keep a legal checklist (discuss, document, plan, consult, do not hide).
- Attacker view: honey assets look valuable by design, so any interaction should be treated as a possible tripwire; consider why a port or share is too easy.

## Source

BHIS/Antisyphon "Active Defense, Offensive Countermeasures, and Cyber Deception", John Strand with Bryce Galbraith and Paul Asadoorian (deck copyright 2026, file dated June 2026). Slides 1-81 summarized here.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-threat-hunting-tools]]
- [[threat-hunting-research/network-data/hunting-the-undetected]]
- [[apts/apt-attack-lifecycle]]
- [[social-engineering/insider-attack]]
- [[reconnaissance/active-recon/stealth-scanning-strategies]]
