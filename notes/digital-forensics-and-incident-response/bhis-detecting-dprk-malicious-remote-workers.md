---
title: bhis-detecting-dprk-malicious-remote-workers
tags: [digital-forensics-and-incident-response, type/methodology, phase/detection, source/bhis]
description: "Antisyphon webcast on North Korean IT-worker schemes: attacker playbook, deepfake interviews, SOC telemetry, hiring red flags."
source_pdf: SLIDES_2026-03-11 AntiSyphon - DPRK Hiring.pdf
---

# How to Detect Malicious Remote Workers (DPRK IT-Worker Schemes)

Question the talk poses: could a nation-state actor get hired and stay invisible to your SOC?

## Attacker's playbook

- Campaign names called out: Contagious Interview and WageMole; investigations referenced from CrowdStrike, Okta and Unit 42.
- **Identity building:** stolen SSNs, addresses and credentials; AI-generated profile photos; GenAI-written resumes tuned to job posts.
- **Stateside facilitators ("laptop farms"):** a US address for laptop delivery, hosting company-issued devices, forwarding payroll, handling stolen identities for tax reporting, installing remote access software, accepting payments to forward to North Korea, providing references.
- **Live deepfakes:** face swap, real-time voice cloning and virtual webcams in interviews (demo shown). The KnowBe4 case (July 2024) is the cited example of a hire that turned out to be a DPRK worker.
- **Scale:** DOJ actions and "NK farmers" arrests; figures on the slide include 309 companies in one operation, 100+ in another, 200 FBI victim notifications and 29 laptop farms raided. A Mandiant CTO quote at RSAC 2025: hundreds of Fortune 500 companies have hired these workers.
- Risks include data theft and extortion once the worker is dismissed, not only salary fraud.

## SOC playbook

| Telemetry | What to look for |
|---|---|
| Identity logs | Concurrent logins from geographically impossible IP pairs; VPN-origin flags in Okta/Azure AD; Astrill VPN ASN traffic as a primary indicator |
| Endpoint/EDR | New RMM or remote tooling (RustDesk, AnyDesk, TinyPilot, VS Code Dev Tunnels); USB insertion; Raspberry Pi/KVM connections; session or log manipulation |
| Network | Traffic to Astrill VPN ASNs; odd outbound traffic to personal GitHub repos |
| DLP | Unusual code-repo download volume; SharePoint/OneDrive bulk access; email forwarding rules created by new hires; large off-hours transfers |

- Deepfake detection tools and VOIP number/identity lookups can supplement, but are not reliable on their own.

## Hiring red flags

- Same phone number or email on multiple applicant resumes; reused VoIP numbers.
- Application address differs from resume or laptop delivery address.
- Reluctance to turn on the webcam or show the physical environment.
- Request to forward the laptop to a third-party address.
- HR tip: be curious; ask about their surroundings and local knowledge, and ask unexpected personal-context questions during video calls.

## Human risk

- Apply the **FAIK** framework (Perry Carpenter): Freeze and feel, Analyze the narrative and emotional triggers, Investigate claims and sources, Know, confirm and keep vigilant.
- Trust and verify, stay skeptical but polite; use out-of-band confirmation and phishing-resistant MFA for sensitive actions.
- Build an AI-ready security team: cross-functional threat modeling, tool familiarity and upskilling.

## Defender/Attacker takeaways

- Defender: add insider-risk monitoring for new hires (remote tooling, forwarding rules, bulk downloads) and pair HR identity verification with SOC telemetry.
- Defender: verify identity in person or via trusted document checks before shipping hardware; ship only to the verified address.
- Attacker lens: they rely on third-party facilitators and common VPN ASNs, which are the detectable seams.

## Source

Antisyphon webcast "How to Detect Malicious Remote Workers / Did We Just Hire a North Korean?" by James R. McQuiggan (advisory CISO), 2026-03-11. Statistics are as presented on the slides and not independently verified.

## Related

- [[social-engineering/insider-attack]]
- [[digital-forensics-and-incident-response/email-forensics/business-email-compromise-investigations]]
- [[apts/apt-attack-lifecycle]]
- [[threat-hunting-research/campaign-analysis]]
- [[threat-hunting-research/attribution]]
- [[threat-hunting-research/threat-hunting]]
