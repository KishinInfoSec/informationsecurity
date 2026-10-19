---
title: bhis-bypassing-modern-phishing-detections
tags: [social-engineering, type/methodology, phase/initial-access, phase/credential-access, platform/web, source/bhis]
description: "BHIS webcast: bypassing email defenses with physical postcards plus AitM login pages, emotional hijacking, and how to defend."
source_pdf: How to Bypass Modern Phishing Detections w Michael Allen (v2) 1.pdf
---

# How to Bypass Modern Phishing Detections ("Pushing the Envelope")

## Core idea: attack where the defender is weakest

Email, chat and SMS are heavily monitored and users are trained for them. Defenders also watch endpoints, the corporate network and VPN, and use MFA and geolocation. The deck's alternative is to deliver the lure through channels defenders cannot see or scrutinize:

| Channel | Why it works |
|---|---|
| Physical mail to the user's home | Unmonitored, unexpected, no attachment or URL to scan; QR codes are hard to inspect |
| User's phone browser and home internet | Outside corporate network and endpoint tooling |
| AitM login page | Beats MFA and geolocation that stop classic credential harvesting |

## Campaign pattern (red team, 2024 to 2025)

- Mailed branded postcards (a "peer recognition award" signed by HR, with a gift-card reward) that send recipients to a pixel-perfect clone of the company login portal.
- The portal is an **adversary-in-the-middle** proxy (Evilginx 3 is shown) that captures credentials and session cookies even with MFA; a later phase covered post-exploitation of the stolen sessions.
- Lessons learned:
  1. Do not buy gift cards from a personal account (even physical or print-at-home).
  2. About 10 postcards per organization is enough; most targeted users log in.
  3. People really want the gift card: not only unsophisticated users; logins from people on vacation; the same person logging in several times (some changed the password then tried again); logins continued two months after the campaign ended despite warnings.

## Why it works: emotional hijacking

- Ingredients: a small but enticing reward ($50 gift card), authority (signed by head of HR, company logo), a polished look (no typos, perfect portal clone) and an emotional trigger.
- People operate logically or emotionally, not both; emotional reactions are faster ("stick or snake?"). The amygdala overrides the prefrontal cortex.
- Delivery context helps: a Saturday, not in work mode, a pleasant surprise, recipients tell others and become invested, so questioning the ruse means questioning whether they deserved the award.

## Defense

1. **Secure the humans:** concept-based awareness that survives novel attacks, regular practice across many channels (email, phone, SMS, Teams, LinkedIn, post, USB drops), and positive reinforcement for desired behaviour. Teach people to notice an emotional reaction, stop, ask whether the situation is what it appears to be and whether the action is risky (logging in, opening a file, a payment, disclosing information), and find a third party they choose to verify with.
2. **Secure the machines:**
   - Either of these stops current AitM attacks: phishing-resistant MFA (FIDO2/U2F/WebAuthn), or allow logins only from the internal network or VPN. Start with highly privileged users if cost is a concern.
   - Others sometimes detect AitM: impossible-travel alerts, alerts on logins from cloud providers, Tor, VPNs or never-seen devices and browsers, and canary tokens on the login portal.

## Defender/Attacker takeaways

- Defender: assume a lure can arrive by any channel, including paper; rely on phishing-resistant MFA and conditional access rather than user vigilance alone.
- Defender: monitor for repeat logins and logins long after a campaign; treat reuse of a changed password as a sign of a compromised session.
- Attacker (authorised engagements): get written scope for physical mail, keep the volume small, use clean infrastructure and never purchase rewards from personal accounts.

## Source

BHIS webcast "How to Bypass Modern Phishing Detections" (deck subtitle "Pushing the Envelope: Lessons Learned From Another Year of Phishing Through the Mail"), Michael Allen (BHIS Red Team Practice Lead, @Wh1t3Rh1n0). Deck date not shown; it references March and October 2024 campaigns. Some slides are screenshots without text, so campaign mechanics are summarized from the slide titles and lessons.

## Related

- [[social-engineering/phishing-mail]]
- [[social-engineering/mfa-bypass]]
- [[social-engineering/spear-phishing-methods-vip]]
- [[social-engineering/link-attacks]]
- [[digital-forensics-and-incident-response/email-forensics/business-email-compromise-investigations]]
- [[cloud-pentesting/azure-pentesting/stealing-access-tokens]]
