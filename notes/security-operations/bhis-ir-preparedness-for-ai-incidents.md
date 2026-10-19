---
title: bhis-ir-preparedness-for-ai-incidents
tags: [security-operations, type/methodology, phase/forensics, platform/web, source/bhis]
description: "BHIS Anti-Cast: AI incident types (threat-actor use, GenAI targeting, internally generated), readiness planning and premortems."
source_pdf: SLIDES_Antisyphon Anti-Cast IR in AI.pdf
---

# Preparing IR for AI Incidents

## Framing and challenges

- No concrete, agreed definition of an "AI incident"; a wide variety of vectors share only "AI" as the common thread.
- Hype obscures signal; teams rapidly adopt agents and AI coding tools with little visibility; threat actors adopt the same tools with a low barrier to entry; governance has not kept pace.
- Context from past incidents: Cuckoo's Egg (1986), the Morris Worm and CERT/CC (1988), ILOVEYOU (1999, containment focus), Stuxnet (2010), the APT1 report (2013), the Sony hack (2014), the rise of ransomware-as-a-service (2017), and a 2025 Anthropic report on threat actors operating at machine speed with AI assistance. History rhymes rather than repeats.

## Three AI incident categories

### 1. Threat actor use of AI
- Automated intelligence gathering and targeting; rapid CVE exploitation (minutes); "vibe-hacking" and AI-assisted scripting; MCP used for actions on objective.
- Cases cited: a jailbroken Claude chatbot used against a Mexican government target (roughly 20 vulnerabilities identified); a 2026 FortiGate campaign (600+ devices compromised Jan 11-Feb 18, single-factor auth and weak credentials, AI-assisted); an Anthropic analysis describing threat actor GTG-1002 using an agentic coding tool to handle 80-90% of operational tasks.
- Key point: responders now face machine-speed attacks; AI-assisted tooling lowers the barrier to entry to near zero.

### 2. GenAI targeting (the org's own AI is the target)
- Vectors: "ignore previous instructions" style prompt injection, supply-chain or data-store attacks, abuse of an org's own AI implementation, non-human identity targeting.
- Cases cited: a dealership chatbot manipulated into agreeing to a $1 car sale via a crafted system-prompt override; Microsoft 365 Copilot "EchoLeak" (CVE-2025-32711, hidden instructions in a document footer exfiltrating email data); a Google Cloud "LLMjacking" incident exposing roughly 3,000 API keys for unauthorized LLM use.
- Key point: hosting LLMs and chatbots widens the attack surface; non-human identities tied to that infrastructure carry disclosure risk, and outputs are implicitly trusted unless validated.

### 3. Internally generated AI incidents
- Rapid self-service automation stand-up (agent frameworks, AI coding tools, editor integrations); shadow AI; plain carelessness (data loss, resource exhaustion).
- Cases cited: "nullifAI" — malicious code hidden in an open-source model on Hugging Face; a developer pointing an AI coding agent at a proprietary database or confidential store; vibe-coding vulnerabilities from rushed AI-generated code; an API-key exposure incident involving roughly 1.5 million leaked tokens.
- Key point: users can connect the org to AI faster than governance can track; shadow AI is a blind spot you cannot plan around until you find it.

## AI readiness planning

Key assumptions: incidents share little beyond "AI" as a label; adoption outpaces readiness; the overall risk picture is still being worked out; you cannot respond to machine-speed attacks at human speed; legacy IR processes are still a useful foundation if adapted.

Eight-step plan:
1. Establish a clear, concise definition (OWASP's: an AI system's behavior or misbehavior leading to unintended, harmful or risk-elevating outcomes; or: a breach of confidentiality, integrity or availability where AI use by a legitimate user or threat actor is a proximate cause).
2. Establish incident criteria across the three categories above, with threat-actor-weaponized AI treated as automatically high severity, inadvertent disclosure tied to existing data-loss processes, and prompt injection handled by verifying guardrails and input filtering.
3. Rework existing processes: automate isolation, containment, visibility and non-human-identity management where possible; rigid swimlane flows become a liability, not an asset, at machine speed.
4. Tie in additional stakeholders beyond the usual legal/comms/executive/IT list: DevOps, ML engineers, data scientists.
5. Run information sharing: a monthly AI workgroup, an "AI fluency index" temperature check, and direct questions to every team using AI (use cases, which LLMs/RAGs/MCPs, what data, how much).
6. Run an AI incident premortem: review the IRP with stakeholders, convene a 1-hour premortem, set a scenario, identify and rank IRP failure points, remediate gaps.
7. Continuously review: quarterly readiness review asking whether the IRP was exercised in the last 90 days, whether new threats need a premortem, and whether new AI tools (for example autonomous coding agents) are in use.
8. Hypothesize, test and improve: turn premortem scenarios into exercises, for example a dev wiring the codebase to an externally visible bot or MCP server, a threat actor using AI to modify scripts live, or a chatbot leaking confidential data.

## Defender/Attacker takeaways

- Defender: pre-load escalation, isolation and containment actions specifically for AI incidents; the escalation path likely differs from a standard IR plan.
- Defender: an AI fluency survey across teams is the cheapest way to find shadow AI before it becomes an incident.
- Attacker-aware note: prompt injection and agentic tool misuse (MCP, coding agents) are now observed attack paths, not theoretical ones, per the cited case studies.

## Source

BHIS/Antisyphon Anti-Cast "Preparing IR for AI Incidents", Gerard Johansen. Deck built from a stated prompt to an AI assistant (noted on the deck's own slide 3) summarizing an incident-manager presentation; dates and figures are as shown on the slides.

## Related

- [[digital-forensics-and-incident-response/cisa-incident-response-playbook]]
- [[miscellaneous/enterprise-agentic-ai-platform]]
- [[owasp-top-10/llm/owasp-top-10-for-llm-applications]]
- [[web-app-pentesting-notes/llm-attacks/indirect-prompt-injection]]
- [[web-app-pentesting-notes/llm-attacks/exploiting-llm-apis-functions-and-plugins]]
