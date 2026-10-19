---
title: bhis-ir-preparedness-checklist
tags: [security-operations, type/cheatsheet, phase/forensics, source/bhis]
description: "BHIS webcast: 10-point incident-response readiness checklist covering IR plans, insurance, logging, comms, backups and playbooks."
source_pdf: SLIDES_IR-Preparedness-Checklist-03032026.pdf
---

# Incident-Preparedness Checklist: 10 Things

Framed as "close enough for horseshoes and hand grenades": simple, effective, repeatable readiness steps rather than a perfect plan.

## The 10 things

1. **Your IR plan is probably useless if it's not simple.** Keep it short (roughly ten pages is already too long) and modular. Contents: roles and responsibilities, contact info including third parties, severity/priority matrices, escalation and emergency powers.
2. **Your cyber insurance provider should be a partner, not an adversary.** Define in the IR plan when and how to engage them, which DFIR vendors are pre-approved, how privileged and confidential communications work, and forensic data acquisition/retention expectations and coverage scope ("return to original condition").
3. **Your log detail and retention are probably inadequate.** Map internal and regulatory retention requirements across IaaS/PaaS/SaaS, ERP, CRM, finance and proprietary systems; decide what "acceptable risk" means for each. The slide example: a 14-day log retention window cannot answer "what happened 15 days ago" if discovery lags initial access.
4. **Know your most important asset.** Identify Tier 0 (identity, connectivity, data infrastructure) and Tier 1 (most critical business systems, for example payroll) priorities before an incident, not during one.
5. **Implement out-of-band communications before a crisis and test them regularly.** Accessible and socialized out-of-band channels, offline contact info (primary, secondary, tertiary), a dedicated cyber-executive liaison role, segregated call/war rooms, and a predefined communication cadence.
6. **Your staff are awesome but not superhuman.** Define a staff rotation policy: maximum shift duration, a monitoring role for breaks/food/fluids, and a plan to send people home. Nobody operates at peak for 24 straight hours.
7. **Effective IR takes training and practice, not videos.** Invest in incident-response training, tactical planning, tactical forensics and evidence acquisition/preservation, then practice regularly with hands-on-keyboard exercises and plan tests.
8. **You must have immutable backups.** Implement them, then actually test restoration and test immutability; confirm retention and recovery time objectives. Treat this as due diligence, not optional insurance.
9. **You have zero hours to fix internet-facing vulnerabilities.** Prioritize manual attack-surface monitoring of anything internet-facing: firewall upgrades/replacements/rule changes, and cloud infrastructure deployment and changes get zero margin for error.
10. **Build the two IR playbooks you need most: egress and authentication.** Pre-define and document the authority and criteria for (a) disconnecting the internet (deny everything, with a granular, tested allow-list for business-critical sites and services by provider/location/geo) and (b) changing all passwords (prioritized by privileged, domain admin and enterprise admin accounts first, and not just AD-integrated accounts).

## Summary list

Create a succinct, tactical IR plan; build a clear and cooperative relationship with your insurance provider; review log retention for all business-critical services; define asset restoration and recovery priorities; implement and test emergency communications; define sustainable staff rotation policies; train and equip emergency response teams; implement and test immutable backups; implement change management for all internet-facing systems; develop and test egress and authentication playbooks.

## Defender/Attacker takeaways

- Defender: the two playbooks worth having ready before anything else are "cut the internet" and "rotate every privileged credential" — both need pre-approved authority so a responder isn't blocked mid-incident.
- Defender: test backup immutability and restoration on a schedule; an untested backup is not a control.
- Attacker-aware note: short log retention windows are exactly what let an intrusion go undetected between initial access and discovery; pushing retention is a detection investment, not just compliance.

## Source

BHIS/Antisyphon webcast "Do It, Do It Now!!! [Incident-Preparedness Checklist]" by Patterson Cake (@SecureCake), dated 2026-03-03 per the filename. Resources referenced: `git.new/simple-ir-plan`, `git.new/ir-guides`, `git.new/rtworkflow`.

## Related

- [[digital-forensics-and-incident-response/cisa-incident-response-playbook]]
- [[digital-forensics-and-incident-response/privacy-research]]
- [[threat-hunting-research/threat-hunting]]
- [[digital-forensics-and-incident-response/ransomware-forensics/decrypting-intermittent-encryption]]
- [[digital-forensics-and-incident-response/memory-forensics/memory-analysis-volatility3]]
