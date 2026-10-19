---
title: analysis
tags: [threat-hunting-research, type/methodology]
---

# Analysis

## Analysis Techniques

*   **Structured Analytics Techniques (SATs):** These are methods to organize and stimulate thinking about intelligence problems. They help make the analysis process conscious and transparent, reducing errors caused by cognitive biases. Examples include:

    * Analysis of Competing Hypothesis
    * Devil's Advocacy
    * Team A/Team B
    * Red Team Analysis


* **Modeling Techniques:** These techniques help in analyzing cyber attacks by creating models that represent attack scenarios. They also help reduce biases. Examples include:
  * Attack Graph or Tree
  * Diamond Model
  * Attack Model
  * Cyber Kill Chain

## Analysis of Competing Hypothesis

### ACH Steps

The "Analysis of Competing Hypothesis" (ACH) is a technique used to evaluate multiple possible explanations for an event and determine which one is most likely based on the available evidence.

1. **Enumerate Hypotheses:** List all possible explanations without considering their feasibility.
2. **Support Hypotheses:** Gather evidence that supports or refutes each hypothesis.
3. **Compare Evidence:** Use a matrix to compare evidence for each hypothesis.
4. **Refine Matrix:** Remove non-diagnostic evidence and add any overlooked evidence.
5. **Prioritize Hypotheses:** Rank hypotheses by their likelihood based on the evidence.
6. **Determine Evidentiary Dependence:** Assess the confidence in the evidence and its impact if it were invalid.
7. **Report Conclusions:** Summarize the findings, including all considered hypotheses and key evidence.
8. **Qualify Needs:** Note that evidence may change over time and how these changes could affect conclusions.

\
The Wannacry ransomware incident is used as an example. Four hypotheses were considered:

* H1: Sophisticated financially-motivated cyber criminal actor
* H2: Unsophisticated financially-motivated cyber criminal actor
* H3: Nation-state actor conducting a disruptive operation
* H4: Nation-state actor aiming to discredit the NSA

\
After comparing the evidence, H2 (unsophisticated financially-motivated cyber criminal actor) was found to be the strongest hypothesis.\
\

## Cyber Kill Chain and Courses of Action

1.  **Cyber Kill Chain**: This is a model that outlines the steps an attacker takes to compromise a target. It includes:

    * **Reconnaissance**: Gathering information about the target.
    * **Weaponization**: Creating a malicious payload.
    * **Delivery**: Sending the payload to the target (e.g., via phishing).
    * **Exploitation**: Using the payload to exploit a vulnerability.
    * **Installation**: Installing malware or gaining access.
    * **Command and Control (C2)**: Establishing control over the compromised system.
    * **Actions on Objectives**: Achieving the attacker's goals, such as data exfiltration.


2.  **Courses of Action Matrix**: This model helps defenders decide how to respond to each phase of the Cyber Kill Chain. Actions can be:

    * **Passive**: Actions like discovering and detecting threats without directly affecting the attacker.
    * **Active**: Actions like denying, disrupting, degrading, deceiving, or destroying the attacker's efforts.


3. **Example**: In a phishing scenario, during the delivery phase, you might:
   * **Detect** suspicious emails.
   * **Deny** by blocking the sender.
   * **Disrupt** by quarantining the email.
   * **Degrade** by stripping attachments.
   * **Deceive** by rerouting emails to a honeypot.

## Cyber Kill Chain and Diamond Model

**Cyber Kill Chain**\
The Cyber Kill Chain is a model developed by Lockheed Martin to describe the stages an attacker goes through to compromise a target. It consists of seven steps:

1. **Reconnaissance**: Gathering information about the target.
2. **Weaponization**: Creating a malicious payload using exploits.
3. **Delivery**: Sending the payload to the target (e.g., via phishing).
4. **Exploitation**: Exploiting a vulnerability to gain access.
5. **Installation**: Installing malware or obtaining credentials.
6. **Command and Control (C2)**: Setting up a command and control channel to navigate the network.
7. **Actions on Objectives**: Achieving the attacker's goals, such as data exfiltration.

\
**Diamond Model**\
The Diamond Model, developed by the Centre for Cyber Threat Intelligence and Threat Research, focuses on four core elements in an attack:

1. **Adversary**: The actor or group responsible for the attack.
2. **Capability**: The tools or techniques used by the adversary.
3. **Infrastructure**: The physical or logical structures used to deliver the capability (e.g., C2 servers).
4. **Victim**: The target of the attack.

\
**Mapping Cyber Kill Chain and Diamond Model**

Analysts understand the sequence of events and the relationships between the adversary, infrastructure, capability, and victim.

* **Reconnaissance**: The adversary gathers information about the victim.
* **Weaponization**: The adversary creates a phishing email (capability) and a malicious payload (infrastructure).
* **Delivery**: The phishing email is sent to the victim.
* **Exploitation**: The victim clicks the link, and the malware is executed.
* **Installation**: The malware installs itself on the victim's system.
* **C2**: The malware sets up a command and control channel.
* **Actions on Objectives**: The malware exfiltrates data from the victim's system.\
