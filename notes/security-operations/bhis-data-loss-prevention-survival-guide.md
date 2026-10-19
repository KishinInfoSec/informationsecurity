---
title: bhis-data-loss-prevention-survival-guide
tags: [security-operations, type/methodology, phase/exfiltration, phase/detection, source/bhis]
description: "BHIS webcast: DLP fundamentals, exfiltration methods, layered technical controls, and a 5-scenario purple-team testing plan."
source_pdf: SLIDES_Data-Loss-Protection-Survival-Guide.pdf
---

# Data Loss Prevention Survival Guide

## Understand the data landscape

- Structured data (customer DBs, employee records, financial systems) versus unstructured data (documents, email attachments, code repos, chat) — unstructured is the hardest to protect and most commonly leaked.
- Classification tiers: Public, Internal, Confidential, Restricted (trade secrets, M&A plans, regulated data such as HIPAA/PCI-DSS). Start with the "crown jewels": what would hurt most if leaked.
- Map where data lives: endpoints (first line of defense), network storage/file servers, cloud/SaaS (with APIs), and data in transit (email, file transfer, API calls).

## How data actually leaves

**Accidental:** wrong email recipient, misconfigured cloud storage permissions, lost/unencrypted devices, improper hardware disposal.

**Malicious:** forwarding to personal email, uploading to personal cloud storage, USB and external devices, screenshots/copy-paste/printing.

**Advanced:** DNS tunneling, steganography, encrypted C2 channels; evasion via file fragmentation, pre-encryption before upload, legitimate-tool abuse, slow exfiltration to blend with normal traffic; timing attacks (after-hours/weekend transfers, gradual theft over weeks or months).

## Insider threat

- Warning signs: access outside normal job function, unusually large downloads, odd-hour or weekend activity, personal devices or accounts, an access spike right before resignation or termination.
- Categories by access/intent: departing employees exfiltrating data, malicious insiders selling information, compromised accounts used by attackers, and negligent users causing accidental exposure.

## Building the foundation

1. Know your data: discover and classify, map access and ownership.
2. Control access: least privilege, quarterly access reviews, immediate removal on role change or departure.
3. Monitor activity: log all access and transfers, baseline normal behaviour, alert and investigate anomalies promptly.

## Technical controls

- **Email:** content inspection for SSNs/credit cards/confidential labels, block or auto-encrypt, quarantine suspicious attachments.
- **Endpoint:** monitor copy/paste to external drives and cloud, control USB/device access with allow-lists, block uploads to unapproved cloud services.
- **Network:** SSL-inspecting web filtering, block personal cloud storage domains, monitor DNS for tunneling.
- **Layered stack:** TLS-inspecting forward proxy/NGFW at the network edge; tenant restrictions for M365/Google plus a CASB for sanctioned-app governance; endpoint DLP agents for off-network coverage; DNS sinkholing for quick wins against known-malicious domains.
- **Cloud/modern workplace:** CASB for shadow-IT visibility and consistent SaaS DLP policy; data-centric security (automatic encryption by classification, rights management, persistent labels); user behaviour analytics for anomaly-based risk scoring.

## Purple team testing scenarios

1. **Email exfiltration:** send sensitive data to personal email, try attachments, encrypted and password-protected files. Success = alert within 5 minutes with a traceable full path.
2. **Cloud upload:** push files to personal Dropbox/OneDrive/Google Drive via browser, sync client and mobile app; try renamed extensions. Common gaps: mobile apps bypass web filters, extension renaming evades content inspection, personal VPN bypasses network controls.
3. **Insider threat simulation:** download an abnormal volume of customer data, access out-of-scope files, act after hours. Expect UEBA risk scoring, anomaly in access logs, and IR procedures triggered by the risk threshold.
4. **USB and physical exfiltration:** copy to USB, transfer to a personal mobile device, print sensitive documents. Confirms endpoint DLP write-blocking, device control policy, and print-job audit logging; also surfaces unmonitored printers.
5. **Advanced evasion:** pre-encrypt before upload, DNS tunnel, fragment large files, screenshot instead of copy. Each needs a different detection: timing/behavioural alerts, DNS anomaly detection, correlation of multiple small transfers, and screenshot-monitoring tools respectively.

Process for all scenarios: plan together (define success criteria and expected detections) → test safely (non-prod data, controlled environment, documented steps) → review collaboratively (compare detected vs missed, time-to-detect, alert quality) → improve and retest.

## Implementation roadmap

- Weeks 1-2: discover top 5 sensitive data types and map where they live.
- Quarter 1: quick wins — email DLP for SSNs/credit cards, basic USB control.
- Quarters 2-3: log cloud app usage, pilot endpoint DLP, run the first purple-team test, tune from results.
- Quarter 4+: roll out to all users, add cloud DLP/CASB, establish a regular testing cadence.

## Defender/Attacker takeaways

- Defender: start with email and endpoint controls for fast wins, then layer network, cloud and behavioural controls; test every layer with the purple-team scenarios above rather than trusting vendor claims.
- Defender: the insider-threat access-spike-before-departure pattern is one of the highest-signal indicators and is cheap to alert on with existing identity logs.
- Attacker-aware note: evasion techniques the deck tests for (pre-encryption, DNS tunneling, fragmentation, extension renaming, screenshotting) are exactly what a real exfiltration attempt would use; treat gaps found in scenario 5 as priority fixes.

## Source

BHIS/Antisyphon webcast "Data Loss Protection Survival Guide" by Ashley Knowles. Resource links on the closing slide include FFIEC/Federal Reserve guidance, Microsoft Purview DLP docs, and vendor blogs (BlackFog, Endpoint Protector, FRSecure, Nightfall AI, Storware); do not invent those URLs if citing further.

## Related

- [[tunneling-and-exfiltration/exfiltration]]
- [[tunneling-and-exfiltration/data-bouncing-external-data-exfiltration]]
- [[tunneling-and-exfiltration/rclone-data-exfiltration]]
- [[digital-forensics-and-incident-response/cisa-incident-response-playbook]]
- [[social-engineering/insider-attack]]
