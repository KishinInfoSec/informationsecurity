---
title: bhis-inside-soc-triage-smarter-not-harder
tags: [security-operations, type/methodology, phase/detection, source/bhis]
description: "BHIS webcast: SOC triage fundamentals, alert anatomy, escalate-vs-close criteria, documentation templates, avoiding alert fatigue."
source_pdf: SLIDES_Inside SOC Triage Smarter Not Harder-1.pdf
---

# Inside SOC: Triage Smarter, Not Harder

## What triage is

Goals: determine severity and impact, identify real threats needing escalation, document decisions, filter false positives. Involves reviewing alert metadata, judging normal vs suspicious vs malicious, enriching with threat intel or internal context, and deciding to escalate, investigate further, or close.

**Triage mindset:** efficient but not rushed; decision-oriented and context-driven; curious, not complacent; consistent documentation; pattern-oriented; calm under pressure; skeptical, not paranoid.

## Anatomy of an alert

Core elements: alert/rule name, detection logic, timestamp, username, hostname, process ID/name, command line, file path, hashes, domain, source/destination IP and port.

Five questions to ask: is this normal for the user/host; does the command or domain look suspicious; have I seen this pattern before; do I have enough context; what logs or tools can verify this?

## The triage process

1. **Review the alert:** read carefully, check severity, rule name, detection logic and key metadata; ask what triggered it and what behaviour was flagged.
2. **Gather context:** check the user's role and behaviour history, the asset involved, enrich with threat intel, review related logs or prior alerts.
3. **Make a decision:** escalate (malicious or highly suspicious), investigate further (still unclear or potentially important), or close (benign, false positive, known behaviour).
4. **Document the outcome:** what was reviewed, what context was found, why you chose to escalate/close/investigate, including URLs or screenshots, per internal documentation standards.

## Real threat or just noise

**Real threat signals:** behaviour abnormal for the user/host, known hacking tools (Mimikatz, Metasploit), a multi-step alert sequence (execution → lateral movement → exfiltration).

**Expected noise:** scheduled PowerShell backups, admins using RMM tools (PsExec, RDP), known-good external domains (for example Microsoft telemetry), vulnerability scanners hitting systems.

**Tools:** SIEM/EDR enrichment, threat intel platforms (VirusTotal, URLScan), internal playbooks (what's the SOP for this alert type), host/user baselining.

**When in doubt:** search for past occurrences, default to "investigate more" instead of blindly escalating, ask a senior analyst, and document what you tried even if still unsure.

## Escalate or close

**Escalate:** confirmed malicious behaviour, matches known attack patterns, abnormal for the user/host, connections to suspicious/malicious IPs or domains, unauthorized tool use, activity on a critical system, persistence or backdoor indicators, requires containment or isolation.

**Close:** noisy or broad rule, expected behaviour of a known business process, covered by existing tuning/allow-list, benign network behaviour, triggered by internal tools, no indicators of compromise, test/lab environment, already-handled repeat alert.

## Common mistakes to avoid

| Mistake | Why harmful | Instead |
|---|---|---|
| Over-escalating without evidence | Wastes time, erodes trust, adds noise | Investigate, enrich, escalate with justification |
| Investigating low-risk alerts too deeply | Less time for higher-priority work, burnout | Use internal resources and documentation, close confidently when benign |
| Skipping context checks | False positives or missed threats | Check internal documentation before digging in |
| Weak or missing documentation | Audit gaps, repeated triage of the same alert | Clearly record what was investigated, found and decided |
| Not asking for help | Slows growth, raises mistake risk, burnout | Ask teammates when needed |
| Treating all alerts the same | Alert fatigue, burnout, time misallocation | Prioritize by asset value and known threat patterns |

Tips for the right call: escalation should be evidence-based, not fear-driven; if unsure, investigate until you have the evidence; use a checklist (is this abnormal, is there business risk, do I have enough context, can I articulate why it's suspicious); know your environment, since what's suspicious at one org may be routine at another.

## Documentation template

```
[Summary]       Brief description of the alert and what triggered it
[Actions Taken] Checks performed (tools, logs, enrichment sources)
[Findings]      Key context, suspicious or benign behaviour, notable evidence
[Decision]      Escalated / Closed / Investigate further — reasoning for the decision
```
Keep it specific, concise and consistent; link to tools or logs where allowed.

## Soft skills and alert fatigue

Communication (concise notes, good questions, sharing updates), active listening (understand context before reacting), collaboration (share shortcuts, pick up slack, give/receive feedback), composure (use playbooks under pressure, think before escalating).

Alert fatigue causes: poorly tuned detections, pressure to act fast on every alert, repetitive low-fidelity alerts, growing workload without automation. Symptoms: skimming alerts, escalating "to be safe," closing too quickly, burnout. Managing it: lean on internal documentation, use enrichment wisely, tune and improve detections, take breaks, lean on the team, and remember triage is about consistency and progress, not perfection.

## Defender/Attacker takeaways

- Defender: the five-question alert checklist and the documentation template are directly reusable as SOC onboarding material or a Sigma/EDR triage SOP.
- Defender: a multi-step alert sequence (execution → lateral movement → exfiltration) is the single strongest "real threat" signal in the deck; correlate before you decide.
- Attacker-aware note: known RMM tools (PsExec, RDP) are explicitly called out as expected noise in many environments — exactly why attackers favour living-off-the-land tooling over custom malware.

## Source

BHIS webcast "Inside SOC: Triage Smarter, Not Harder" by Tom DeJong (BHIS SOC Triage Lead). The live demo used Obsidian and LimaCharlie against Sigma-LimaCharlie detection rules; demo content is not transcribed here beyond the rule repository names.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-threat-hunting-tools]]
- [[owasp-top-10/web/a09-2021-security-logging-and-monitoring-failures]]
- [[post-exploitation/living-off-the-land-tools]]
