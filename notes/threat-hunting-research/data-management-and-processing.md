---
title: data-management-and-processing
tags: [threat-hunting-research, type/reference]
---

# Data Management and Processing

## Data Processing

### Intro to Data Processing

1. **Definition of Data Processing**:
   * Data processing involves transforming collected data into a format usable by your organization. This is crucial because raw data from various sources often comes in different formats and needs to be standardized.\

2. **Approaches to Data Processing**:
   * **Automated Processing**: Uses tools like regular expressions, statistical algorithms, machine learning, and natural language processing to handle large volumes of data. These methods help identify patterns, similarities, and relevant information.
   * **Human-Based Processing**: Relies on human analysts to process data manually. This is essential for tasks that require adaptive reasoning and problem-solving, which machines can't fully replicate. Analysts can provide context and meaning that automated systems might miss.\

3. **Stages of Data Processing**:
   * **Sorting and Filtering (Pre-processing)**: Cleaning up raw data by removing duplicates, incomplete, or incorrect data. This stage ensures that only high-quality data moves forward.
   * **Normalization**: Converting data into a standard format suitable for your needs. For example, if you're adding indicators to a watch list, the format should be compatible with your SIEM (Security Information and Event Management) system.
   * **Storage and Integration**: Storing processed data in a way that it can be easily accessed and integrated with other systems. This stage will be covered in more detail in future videos.\

4. **Importance of Data Processing**:
   * Processing data is essential to avoid generating duplicate alerts and to make the data usable for threat intelligence. Without processing, it would be challenging to correlate events and make assessments based on raw data alone.\

## Storage and Integration

* **Storage**: After processing data from multiple sources, it's crucial to store it properly for future use, such as temporal and campaign analysis. Proper storage ensures compliance with data protection laws like GDPR and allows easy access for your team when needed.\

* **Integration**: Actionable indicators from your processed data need to be integrated back into your security devices and products. This helps in making your security measures more effective. However, avoid integrating non-curated or non-vetted feeds as they can generate excessive noise and alerts, overwhelming your analysts.

## Threat Intelligence Platforms

**Threat Intelligence Platforms (TIPs)**:

* **Definition**: TIPs are software tools that organize multiple threat intelligence feeds into a single stream. They help you get alerts and manipulate data efficiently.

\
**Who Uses TIPs**:

1. **Security Operations Center (SOC) Teams**: They use TIPs to automate daily tasks.
2. **Threat Intelligence Teams**: They use TIPs to assess and predict threats based on enriched data.
3. **Executive and Management Teams**: They use TIPs for dashboards that display threat trends to aid decision-making.

\
**Common Capabilities**:

1. **Collect**: TIPs automatically gather data from various sources (open source, paid feeds, reports, etc.).
2. **Manage**: TIPs process data by sorting, normalizing, deduplicating, and enriching it, freeing analysts to focus on analysis.
3. **Integrate**: TIPs deliver processed data to systems that use it to improve threat detection.

\
**Examples of TIPs**:

* **OTX (Open Threat Exchange)**: A community platform sharing millions of threats daily.
* **MISP (Malware Information Sharing Platform)**: An open-source platform for sharing and correlating indicators of compromise.
* **CRITS (Collaborative Research into Threats)**: An open-source repository for storing and discovering threat data.
* **ThreatConnect**: Offers both free and paid platforms with features like orchestration and customizable dashboards.
* **STAXX**: An open-source platform compatible with STIX and TAXII standards, providing threat trends and enrichment.\

## Common CTI Standards

1.  **Importance of Standards**:

    * Standards define how information is represented in files or communications, which is crucial for sharing and interpreting data accurately in cyber threat intelligence.


2. **Scoring Standards**:
   * **CVSS (Common Vulnerability Scoring System):**
     * Measures the severity of vulnerabilities using three metrics: base, temporal, and environmental.
     * Scores range from 0 to 10, with 10 being the most critical.
     * Example: Bluekeep (CVE-2019-0708) has a critical score of 9.8.\

3. **Threat Description or Taxonomy Standards**:
   * **OpenIOC**:
     * Introduced by Mandiant in 2011.
     * Provides a standard format for describing threat artifacts using an XML schema.\

   * **CybOX (Cyber Observable Expression)**:
     * Standardized language for representing observables, now integrated into STIX 2.0.\

   *   **STIX (Structured Threat Information Expression)**:

       * Structured language for describing cyber threat information.
       * Allows for consistent sharing, storing, and analysis of threat data.
       * Defines relationships between constructs, like linking a campaign to a threat actor.


4. **Traffic Light Protocol (TLP)**:
   * **Purpose**: TLP is a simple protocol used to label sensitive information to ensure that only the correct audience has access to it.
   * **Color Codes**:
     * **Red**: Information is highly sensitive and should only be used by you. Do not share it with anyone, even within your organization.
     * **Amber**: Information can be shared within your organization on a need-to-know basis and with clients or customers who need it to protect themselves.
     * **Green**: Information is not very sensitive and can be shared with partners or peers, but not via public channels like websites.
     * **White**: Information is public and can be shared freely, considering standard copyright rules.\

5. **Trusted Automated Exchange of Indicator Information (TAXII)**:
   * **Purpose**: TAXII is an application protocol for exchanging threat intelligence over HTTPS. It defines a RESTful API and requirements for TAXII clients and servers.
   * **Key Features**:
     * **Supports STIX**: TAXII is designed to support the exchange of threat intelligence represented in STIX format.
     * **Design Principles**: Minimizes operational changes needed for adoption, integrates easily with existing sharing agreements, and supports various threat-sharing models (Hub and Spoke, Peer to Peer, Source Subscriber).
     * **Examples**: Free TAXII servers like Limo and Hail TAXII are compatible with TAXII 2 and STIX 2.
