---
title: external-data
tags: [threat-hunting-research, data-collection, type/reference]
---

# External Data

## Community Data Sources

1.  **Community Data Sources**:

    * These are external sources where organizations share threat intelligence within a community to enhance cybersecurity.


2. **Types of Community Data Sources**:
   *   **Information Sharing and Analysis Centers (ISACs)**:

       * **Sector-Based ISACs**: Focus on specific industries (e.g., financial, automotive).
       * **Country-Based ISACs**: Focus on cooperation within a specific country.
       * **International ISACs**: Connect organizations globally.


   * **Information Sharing and Analysis Organizations (ISAOs)**:
     * More flexible than ISACs, not limited to critical infrastructure sectors.
     * Can be based on various criteria like geography, roles, or specific interests.\

3. **Benefits of Joining ISACs/ISAOs**:
   * **Risk Mitigation**: Access to shared intelligence helps in reducing risks.
   * **Rapid Response**: Quick coordination and response during emergencies.
   * **Training and Reporting**: Access to training, webinars, white papers, and threat reports.
   * **Collaboration**: Enhanced collaboration between public and private sectors.

***

## Private Data Sources

1. **Private Data Sources**:
   * These are threat intelligence sources available through paid subscriptions. They are provided by various vendors, including traditional security service providers and specialized threat intelligence vendors.\

2. **Types of Private Data Sources**:
   * **Narrative-Based Reports**:
     * Also known as finished intelligence, these reports provide detailed descriptions of events related to intrusions or incidents.
     * They include TTPs (Tactics, Techniques, and Procedures), campaign investigations, and sometimes attribution.
     * Advantages: Rich in detail, full of indicators, and provide a comprehensive picture of threats.
     * Disadvantages: Time-consuming to produce, difficult to make actionable, and require custom tools for processing.
     * Examples of vendors: FireEye, Kaspersky, Recorded Future, Flashpoint, Intel 471.\

   * **Threat Intelligence Feeds**:
     * Real-time and continuous streams of data providing information on potential cyber threats and risks.
     * Include simple indicators like malware hashes, suspicious domains, or IPs associated with malicious activities.
     * Advantages: Actionable, easy to integrate, up-to-date, and vetted information.
     * Disadvantages: Lack context compared to reports, come in large volumes, and sometimes lack relevance.
     * Examples of vendors: Recorded Future, Malware Patrol, I-Blocklist, TruSTAR, IBM X-Force, Anomali.\

3. **Relevance and Quality**:
   * The relevance of threat intelligence is crucial. Intelligence that is not relevant to your organization’s threat model is useless.
   * Quality can be subjective and depends on factors like the sector, technologies used, location, and size of the company.
   * It is recommended to define your own use cases and requirements before looking for threat intelligence solutions.\


***

### Threat Intelligence Platforms

1.  **Threat Intelligence Platforms**:

    * These are software or portals developed by security vendors that organize multiple threat intelligence feeds into a single stream.
    * They provide real-time alerts, normalize data, remove duplicates, and allow user-set rules.


2.  **Advantages**:

    * **Indicators with Context**: They offer actionable intelligence with context.
    * **Enrichment**: Useful for adding more information to existing data.
    * **Aggregation**: Combine multiple feeds and sometimes include narrative-based reports.
    * **Integration**: Can be integrated with SIEM solutions and firewalls.


3.  **Disadvantages**:

    * **Cost**: These platforms can be expensive, especially if they include premium feeds from closed sources.


4. **Examples of Platforms**:
   * Anomali ThreatStream, IntSights, Recorded Future, EclecticIQ, ThreatQuotient, Soltra from NC4, TruSTAR.

## Public Data Sources

1.  **Public Threat Intelligence Sources**:

    * These are freely available to anyone and usually have no cost associated with access.
    * Types include threat bulletins, feeds, and platforms.


2.  **Challenges**:

    * **Trustworthiness**: Public sources often have uncurated indicators, leading to noise and false positives.
    * **Lack of Context**: Indicators like IPs, hashes, or domains may lack detailed context about their roles in malicious activities.
    * **Outdated Data**: Some sources keep old data, making validation harder and potentially wasting time on irrelevant alerts.


3. **Examples of Public Threat Intelligence Feeds**:
   * **Cybercrime Tracker**: Provides URLs and IPs associated with malicious activities.
   * **URLhaus**: Shares malicious URLs used for malware distribution.
   * **Ransomware Tracker**: Tracks ransomware-related domains, IPs, and URLs.
   * **OpenPhish**: Offers feeds on phishing campaigns.
   * **I-Blocklist**: Maintains lists of IP addresses related to various categories like web attacks and proxies.
   * **Cyber Cure Platform**: Provides lists of infected IPs, malware URLs, and hash files.\

4. **Feed Aggregators**:
   * **LIMO**: Aggregates multiple threat intelligence feeds and is compatible with STIX and TAXII protocols.
   * **Hail A TAXII**: Another feed aggregator that collects open-source threat intelligence feeds in STIX format.

***

### Threat Intelligence Platforms

1. **Public Threat Intelligence Platforms**:
   * These platforms organize multiple threat intelligence feeds into a single stream, making it easier to manage and utilize the data.
   * They can be used for enrichment, adding more context to existing data.\

2. **Examples of Public Threat Intelligence Platforms**:
   * **STAXX by Anomali**: A platform that aggregates threat intelligence feeds.
   * **MISP**: An open-source threat intelligence platform.
   * **CRITs**: Another open-source platform for threat intelligence.
   * **OTX (Open Threat Exchange) by Alien Labs**: A community-driven platform for sharing threat intelligence.
   * **OpenCTI**: An open-source platform for managing cyber threat intelligence.
   * **CIF (Collective Intelligence Framework) by CSIRT Gadget**: A platform for sharing and managing threat intelligence.\

3.  **Benefits**:

    * **Enrichment**: These platforms can add valuable context to threat data, making it more actionable.
    * **Aggregation**: They combine multiple feeds into a single stream, simplifying data management.
    * **Accessibility**: Many of these platforms are available for free, making them accessible to organizations of all sizes.


4. **Challenges**:
   * **Trustworthiness**: Public threat intelligence sources may have uncurated indicators, leading to noise and false positives.
   * **Maintenance**: Some platforms may require significant effort to maintain and keep up-to-date.
