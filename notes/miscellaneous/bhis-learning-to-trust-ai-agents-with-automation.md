---
title: bhis-learning-to-trust-ai-agents-with-automation
tags: [miscellaneous, type/cheatsheet, source/bhis]
description: "BHIS webcast: picking a coding agent, context/config concepts, prompting tips, guardrails for giving an agent command execution."
source_pdf: SLIDES_Mar 26 - Learning to Trust AI Agents with Automation w_ Ethan Robish.pdf
---

# Learning to Trust AI Agents with Automation

A practitioner talk on adopting AI coding agents safely, illustrated with live show-and-tell demos (OpenCode, Claude, free models, OpenWork, plan mode, permissions/hooks/containers).

## Getting started

- Tip: pick one agent and start learning rather than evaluating everything at once.
- Subscription concerns are addressed by free/open options: OpenCode (open-source agent harness) and free-tier models.
- "I don't code, why do I need an agent?" — agents are general task runners, not just dev tools: cited example is a tweet noting Claude Code was misnamed, since it can do anything achievable by executing commands on a computer. Possibilities: troubleshooting audio in a video file, system administration, bespoke software development.
- OpenWork demoed as a browser- and task-automation-oriented agent UI.

## Working with the agent

- Tip: ask the agent itself how to interact with it better — "how do I get you to remember so I don't have to repeat myself", "how can I prevent you from executing dangerous commands on my system", "any suggestions for how to better interact with you".
- AI always makes things up (confabulation); tip — tell the agent to fetch current documentation from the web rather than rely on training data.
- The "Plinko problem": AI responses degrade over a long conversation — early turns keep grounded, high-accuracy responses; past a "point of no return" corrections stop working and hallucination/looping becomes likely, because token drift only moves one direction, like a Plinko chip. Tip: starting a fresh conversation or changing approach can beat continuing to argue with an LLM.

## Core concepts

- **Connections:** Tools, MCP (Model Context Protocol).
- **Context:** AGENTS.md/CLAUDE.md project instruction files, agents/subagents, skills, commands.
- **Config:** user vs project scope, plugins, permissions, hooks.

## Guiding an agent

- Tip: spend about 80% of your time planning, 20% executing.
- The agentic loop (perceive → plan → act → observe → repeat) benefits from giving the agent a way to check its own work (tests, lint, a defined success condition).
- Demonstrated workflow (Ethan's): 1) initialize the project with scaffolding, 2) brainstorm (a "superpowers" skill/process), 3) review the generated spec file (a "plannotator" step), 4) write a plan, 5) execute the plan, 6) repeat from step 2 for the next unit of work.
- Plan mode: let the agent produce a reviewable plan before it touches anything.

## Guardrails for command execution

Four layers, in increasing isolation: **permissions** (allow/deny specific tools and commands), **hooks** (intercept and gate tool calls), **containers** (isolate the agent's filesystem/process access), **virtual machines** or **hosted** environments (full isolation from the host).

## Learning more

Resources listed on the closing slide: the agent's own documentation; Anthropic's prompt-engineering best-practices guide; `anthropic.skilljar.com`; two community GitHub guides ("OpenCode Everything You Need to Know" and "Claude Code Everything You Need to Know" by wesammustafa); Simon Willison's agentic engineering patterns guide; `factory.strongdm.ai/techniques`.

## Defender/Attacker takeaways

- Defender/operator: treat "give an agent command execution on my system" as a real risk decision — use the permissions/hooks/container/VM ladder deliberately rather than granting full shell access by default.
- Practical tip for any security team adopting agents: the context-degradation point ("Plinko problem") means long investigation sessions with an agent should be restarted periodically rather than endlessly corrected.

## Source

BHIS/Antisyphon webcast "Learning to Trust AI Agents with Automation" by Ethan Robish, dated March 26 in the filename (year not shown). Several slides are demo-only ("Show & Tell") with no accompanying text; those are summarized at the level of what was demoed.

## Related

- [[miscellaneous/enterprise-agentic-ai-platform]]
- [[security-operations/bhis-effective-ai-for-practical-secops]]
- [[owasp-top-10/llm/owasp-top-10-for-llm-applications]]
