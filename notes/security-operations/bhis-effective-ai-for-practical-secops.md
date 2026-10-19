---
title: bhis-effective-ai-for-practical-secops
tags: [security-operations, type/methodology, phase/detection, source/bhis]
description: "BHIS webcast: real SOC AI workflows (agents, case titling, QA review, detection drafting), costs, blockers, and sample prompts."
source_pdf: SLIDES_Effective-AI-for-Practical-SecOps.pdf
---

# Effective AI for Practical SecOps

Workflows the speaker's SOC runs in production, not vendor demos or theory. Thesis: AI augments analysts, it does not replace them — "force multipliers only work if you have force to multiply." Train the humans first, then give them AI tools.

## What augmentation looks like

- AI-generated investigation summaries (analyst still validates findings).
- Threat intel correlation surfaced faster (analyst still decides priority).
- Draft detections in seconds (analyst still tunes and tests). Pattern: AI does the grunt work, humans keep the judgment calls.

## Consider before implementing anything

- **Cost:** token-heavy workflows and long context add up fast; estimate volume, set billing alerts, be cautious with usage-based billing; weigh cloud AI convenience against self-hosted cost and data control.
- **Policy and legal:** decide what can go to external AI services (avoid customer data/PII), check provider data retention, consider on-prem/local-only requirements.
- **Data sensitivity:** sanitize or abstract before pasting into a prompt (example: "User A accessed System B" instead of real usernames/hostnames); even without training on your data, providers may retain it. Idea: a local model just for sanitization.
- **Team buy-in:** acknowledge analyst skepticism as reasonable, address fears directly (augmentation not automation), start with small low-stakes wins, make adoption opt-in rather than mandated.
- **Fundamentals first (PEBKAC):** master core security concepts before leaning on AI, learn prompt engineering, always validate AI output, know when human judgment is required instead.

## Start-this-week workflows

- **Curated team agents:** shared agents in ChatGPT/Copilot/Claude Projects, preloaded with runbooks, detection logic and environment specifics. Build pattern: give role context ("You are a senior SOC analyst at..."), feed documentation, define output format, share the prompt with the team. Agent ideas: detection code reviewer, SOC analyst assistant, threat intel summarizer, project manager.
- **Detection code review agent:** a second set of eyes — catches syntax issues, suggests optimizations, flags overly broad queries, identifies coverage gaps. Prompt pattern: give the rule, environment details (SIEM, log sources), one good example, and ask for YAML syntax check, false-positive potential, performance, coverage gaps, MITRE tagging, with a required checklist-style output.
- **Version-controlled prompts:** store prompts in GitHub for change tracking and rollback; share a prompt library across the SOC; treat prompts as code.
- **SOC analyst agent:** turns raw logs into structured triage notes, natural-language activity descriptions into draft queries, alert context into pivot points, findings into customer-facing language, and can explain/deobfuscate PowerShell on request. Prompt pattern: extract key fields, flag suspicious indicators, suggest pivot points, provide a severity assessment, and for hunts generate SIEM queries and link MITRE techniques; explicitly scope environment (OS, EDR, SIEM, log sources).
- **Quick wins:** Raycast InfoSec extensions (APT fact sheet, CVE lookup, CTI analyst context, VirusTotal lookup) for in-line answers during investigation — `github.com/Nynir/Raycast-InfoSec`.

## Build-this-month workflows

- **Case titling and summaries:** replace generic alert titles ("High Severity CrowdStrike Alert") with specific ones ("Cobalt Strike beacon detected on &lt;host&gt;"), generated from host, user and alert detail fields with example title structures and output constraints (length, must include the key indicator and affected asset).
- **Automated ticket QA review:** AI reviews a completed ticket against playbook/rubric criteria, flags missing evidence (screenshots, log snippets, queries), unclear language, inconsistent formatting and recurring mistakes. Two modes: pre-emptive flagging during ticket creation, or a final gate before customer escalation. Define "good ticket" criteria explicitly and watch for the model latching onto example data as a template to copy rather than a standard to check against.
- **Detection engineering first drafts:** feed a threat report, IOC or MITRE technique, get a draft query in your SIEM's language; the analyst still owns validation, tuning, documentation and testing. Prompt pattern: research via MITRE ATT&CK and existing Sigma rules, pick the best telemetry source (native EDR over generic logs), generate detection logic with MITRE tags, suggest false-positive exclusions, and validate that exclusions cannot be trivially abused.

## Where AI often fails

- Real-time accuracy (it hallucinates — trust but verify); final escalation decisions need human judgment; novel/unprecedented attacks can exceed its context; it cannot replace experience-built analyst intuition; do not trust it unvalidated when you need guaranteed accuracy. Most of these can be mitigated with validation steps built into the workflow.

## Defender/Attacker takeaways

- Defender: the highest-leverage, lowest-risk starting points are a shared curated agent and a detection-code-review agent — both cost little and have a human in the loop by design.
- Defender: version-control your prompts like code; this is what makes AI workflows auditable and repeatable across a SOC.
- Human-in-the-loop is "not optional, it's the whole point" for every workflow described.

## Source

BHIS webcast "Effective AI for Practical SecOps" by Hayden Covington (SOC SecOps Lead, Black Hills Information Security). A companion Notion resource page and a Raycast-InfoSec repository are linked on the closing slides; URLs not transcribed here beyond the repo path above.

## Related

- [[threat-hunting-research/threat-hunting]]
- [[threat-hunting-research/network-data/network-threat-hunting-tools]]
- [[miscellaneous/enterprise-agentic-ai-platform]]
- [[web-app-pentesting-notes/llm-attacks/exploiting-llm-apis-functions-and-plugins]]
