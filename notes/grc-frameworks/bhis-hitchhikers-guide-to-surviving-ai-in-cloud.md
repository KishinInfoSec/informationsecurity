---
title: bhis-hitchhikers-guide-to-surviving-ai-in-cloud
tags: [grc-frameworks, type/methodology, phase/hardening, platform/aws, source/bhis]
description: "BHIS webcast: securing agentic AI on AWS Bedrock across governance, infrastructure/data protection and model-behavior resilience."
source_pdf: SLIDES_The Hitchhikers Guide to Surviving AI in Cloud.pdf
---

# Securing AI in the Age of Cloud (The Hitchhiker's Guide framing)

A Hitchhiker's-Guide-themed talk on securing agentic AI workloads on AWS, built around three pillars: **Governance and Compliance**, **Infrastructure and Data Protection**, and **Resilience and Model Behavior**.

## The agentic revolution: context

- 16% of breaches in the last year began with AI-specific vectors (per the deck's cited stat).
- **Prompt injection is framed as the new SQL injection:** legacy input manipulation (SQL injection against a database) has a direct modern analogue (prompt injection against an LLM/AI assistant), with the same shape of attack — unauthorized instruction, model manipulation, data exfiltration, PII leak.
- **AI sandbox escapes are just sandbox escapes:** the deck draws a technical-equivalence diagram between traditional sandbox escape (KVM/seccomp-bpf/WASM, ROP, race conditions, memory corruption → host access) and AI-assistant/LLM sandbox escape (malicious prompt → code interpreter runtime vulnerability → arbitrary code execution/unexpected syscall access → host access). The difference is only the initial vector: natural language versus low-level code.
- **AI and general software supply chains share structure:** both follow requirements/planning → coding/data sourcing → testing/evaluation → packaging → deployment, with similar CI/CD-style lifecycle and dependency management, just with model training/optimization and model registries substituted for traditional coding and packaging stages.
- A concrete AWS Bedrock AgentCore privilege-escalation chain (via `pathfinding.cloud`): a principal with `iam:PassRole`, `bedrock-agentcore:CreateCodeInterpreter`, `bedrock-agentcore:StartCodeInterpreterSession` and `bedrock-agentcore:InvokeCodeInterpreter` can create and invoke a code interpreter with a privileged execution role. Interpreters run on Firecracker MicroVMs and can reach the MicroVM Metadata Service (MMDS) at `169.254.169.254` (analogous to EC2 IMDS); invoking arbitrary Python there can retrieve temporary credentials and gain the full permissions of that execution role.
- Leaked AI service secrets reportedly reached 1,275,105 in 2025, an 81% year-over-year surge (per the deck).

## Pillar 1: Governance and Compliance ("Squishy Stuff" vs "Not Squishy Stuff")

- **Squishy (needs judgment):** data sovereignty — does your data belong in that model/region; model provenance — do you trust that model.
- **Not squishy (just do it):** disable Bedrock models you don't use and disable regions you can't be in, both via Service Control Policies (SCPs). Example SCP pattern: deny `bedrock:InvokeModel`/`bedrock:InvokeModelWithResponseStream` on `arn:aws:bedrock:*::foundation-model/*` unless the model ID matches an allow-listed family (for example only Claude Sonnet models).
- An AI coding tool (shown generating the SCP JSON live) can draft these policies, but review them before applying.

## Pillar 2: Infrastructure and Data Protection

- **Build a network perimeter:** route SageMaker/Bedrock traffic through AWS PrivateLink from the customer VPC into the SageMaker-managed VPC rather than over the public internet; without a configured endpoint, a SageMaker container cannot reach either VPC resources or the internet gateway directly — connections should be denied by default until explicitly allowed.
- **AI workload threat-vector coverage table** (AWS-native vs gaps vs third-party runtime detection):

| Threat vector | AWS native method | Typical gap | Third-party runtime option |
|---|---|---|---|
| Model poisoning | Partial — CloudTrail, SageMaker Model Monitor | No behavioral detection of poisoned inference outputs | Runtime anomaly detection on model decisions |
| Training data contamination | Partial — S3 access logging, Macie | No runtime data-integrity validation | AI-aware data access monitoring |
| Prompt injection | Partial — Bedrock Guardrails | Limited to configured static patterns | Input/output behavioral analysis across turns |
| Agent escape attempts | None native | No runtime process/network monitoring | eBPF-based process/network detection, CADR correlation |
| Tool/API misuse | Partial — CloudTrail API logging | No behavioral anomaly detection on tool patterns | Behavioral baselines with deviation alerting |
| AI-mediated lateral movement | Partial — GuardDuty findings | Limited to known threat signatures | Cross cloud/cluster attack-story correlation (CADR) |
| Malicious AI dependencies | None native | No runtime dependency monitoring | Runtime-derived AI bill of materials |

- **CloudTrail's blind spot:** CloudTrail logs the `bedrock:InvokeModel` call itself (who, when, role) but cannot tell you what the agent actually *did* with its permitted tools afterward — an unauthorized action taken with a legitimate, permitted tool call looks identical to CloudTrail as a legitimate one. Opening unexpected network connections, misusing permitted tools, and exfiltrating data via sanctioned tool calls all fall in this gap.
- Static long-lived credentials are called out as a recurring, avoidable risk even on managed AI platforms ("if static credentials are so bad, why do we keep creating ways to make them?") — prefer short-lived, scoped roles over API keys.
- **Guardrails flow:** user input → FM inference → Guardrail (content filters, denied topics, sensitive-info filters, word filters, contextual grounding checks, automated reasoning checks) → final response. A RAG pipeline (RetrieveAndGenerate API → embedding search over a knowledge base → augmented prompt → InvokeModel → Guardrails check) is shown as the reference AI-stack shape to secure end to end.

## Pillar 3: Resilience and Model Behavior

- Observability: an LLM agent's actions (tool calls, API calls) should flow through OpenTelemetry (traces, metrics, logs) into a dashboard, the same way any production service is instrumented. Claude Code supports this via environment variables (`CLAUDE_CODE_ENABLE_TELEMETRY=1`, OTLP exporter/endpoint/auth configuration) — see `code.claude.com/docs/en/monitoring-usage`.
- Business case for this telemetry: cost control (token/call volume drives spend) and an agent-cost-accounting tool example (`github.com/rtk-ai/rtk`) for tracking and savings.
- "You still have to have logs": Amazon Security Lake centralizes findings and logs from GuardDuty, Inspector, IAM Access Analyzer and 50+ partner sources (via VPC, CloudTrail, S3, Lambda, Route 53, EKS, WAF) into normalized OCSF data in S3, queryable via Athena, OpenSearch or SageMaker — AI agent activity needs to land in the same pipeline as everything else, not a separate silo.
- Token-cost-reduction tooling (`rtk` CLI proxy, agent compaction) is mentioned as a cost-saving angle that also reduces blast radius by limiting context exposure per call.

## Defender/Attacker takeaways

- Defender: SCPs to allow-list only the Bedrock model families and regions you actually use closes an entire class of "silently enabled by default" exposure — do this before anything else.
- Defender: treat "the agent called an allowed tool" as insufficient evidence of safety; CloudTrail shows the call, not the intent or downstream effect, so pair it with behavioral/runtime monitoring for agent actions.
- Attacker-aware note: the AgentCore code-interpreter privilege-escalation chain (`iam:PassRole` + code-interpreter creation/invocation permissions → MMDS credential theft) is a concrete, documented path worth checking for in any Bedrock AgentCore deployment.

## Source

BHIS/Antisyphon webcast "Securing AI in the Age of Cloud" by Andrew Krug (`andrewkrug.com`, author of the Antisyphon course "Securing the Cloud: Foundations"). Figures (16% of breaches, 1,275,105 leaked secrets, 81% YoY) are as presented on the slides and not independently verified; do not treat them as sourced beyond this deck.

## Related

- [[cloud-pentesting/aws-pentesting/aws-environments/identity-and-access-management]]
- [[cloud-pentesting/aws-pentesting/attacks-and-methodology/exploiting-aws-misconfigurations]]
- [[cloud-pentesting/aws-pentesting/attacks-and-methodology/aws-pentest-methodology]]
- [[miscellaneous/enterprise-agentic-ai-platform]]
- [[owasp-top-10/llm/owasp-top-10-for-llm-applications]]
- [[cloud-pentesting/aws-pentesting/tools/cloudsplaining]]
