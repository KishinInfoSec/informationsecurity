---
title: campaign-analysis
tags: [threat-hunting-research, type/methodology]
---

# Campaign Analysis

## Introduction to Campaigns

**What is a Campaign?**

* A campaign is a series of incidents that occur over a specific time period and are related by shared indicators, tools, infrastructure, or TTPs (Tactics, Techniques, and Procedures).
* These incidents are performed by the same threat actors or have a shared objective.

\
**Starting a Campaign Analysis**

* **Identify Trends**: Look for patterns in intrusions over time.
* **Keep Detailed Reports**: Maintain detailed incident reports, including indicators, as they can be useful for future analysis.
* **Use External Intelligence**: Collect intelligence from multiple sources like iSaaS, ISOs, vendors, and resources.

\
**Key Indicators**

* Consistent indicators across intrusions help identify whether the trend targets a specific sector, country, or organization.
* Compare key indicators and TTPs to identify adversaries.

\
**Techniques for Campaign Analysis**

* **ACH (Analysis of Competing Hypothesis)**: Replace hypothesis with campaign hypothesis and identify candidate campaigns for correlations.
* **Cyber Kill Chain and Diamond Model**: Use these models to correlate intrusions based on key indicators.
* **Other Techniques**: Data analysis, temporal analysis, visual analysis, and heatmap analysis.

\
**Importance of Campaign Analysis**

* Helps anticipate future intrusions.
* Even unsuccessful intrusions are useful as adversaries may try them again.\

## Heatmap Analysis

**Heatmap Analysis** is a technique used to visualize data, making it easier to identify trends and patterns.\
\
**What is a Heatmap?**

* A heatmap is a graphical representation of data where values are depicted by color.
* It uses a warm-to-cool color spectrum to show activity levels, with red indicating high activity and green indicating low activity.

\
**Why Use Heatmaps in Cyber Threat Intelligence?**

* Heatmaps help make complex data sets comprehensible and actionable.
* They allow you to quickly see trends and understand what actions to take next.
* In cyber threat intelligence, heatmaps can show intrusion attempts and help identify knowledge gaps about adversaries.

\
**Creating a Heatmap in Excel**

1. **Prepare Your Data**: Create an Excel spreadsheet with rows representing activities per month and columns representing different campaigns.
2. **Select Data**: Highlight the numerical data you want to visualize.
3.  **Apply Conditional Formatting**:

    * Go to the Home menu.
    * Choose Conditional Formatting.
    * Select a color scale (e.g., red to green) where red indicates the highest activity level.


4. **Analyze Results**: Look at the heatmap to identify high activity periods (red areas) and low activity periods (green areas).

\
**Benefits of Heatmap Analysis**

* **Identify Trends**: Quickly see periods of high and low activity.
* **Understand Adversaries**: Determine patterns in intrusion attempts, such as increased activity during certain months.
* **Prioritize Actions**: Use the insights to decide on the best course of action to address threats.\

## Visual Analysis

\
**What is Visual Analysis?**

* **Graph Analysis**: Also known as visual or link analysis, it involves the visual representation of nodes (entities) and edges (connections) in a graph.
* **Purpose**: Helps analyze and visualize threat trends by showing relationships and patterns in data.

\
**Why is Visual Analysis Important?**

1. **Faster Information Processing**: The human brain processes visual information much quicker than written data, leading to faster comprehension and action.
2. **Insight Discovery**: Interacting with visual data helps uncover insights that might be missed in traditional data formats.
3. **Pattern Recognition**: Visualizing data helps identify patterns and context, making it easier to understand complex relationships.
4. **Accessibility**: Graph visualization tools can be used by non-technical users, making insights accessible to a broader audience.

\
**Benefits of Graph Technology**

* **Combines Multidimensional Data**: Aggregates data from multiple sources into a single comprehensive model.
* **Scalability**: Can handle large amounts of data, scaling up to billions of nodes and edges.
* **Suspicious Activity Detection**: More easily identifies suspicious patterns and anomalies by analyzing the dynamics between entities.

\
**Tools for Visual Analysis**

1. **KeyLines**: A JavaScript SDK for interactive graph visualization that works with various data sources and formats.
2. **Linkurious**: Allows analysts to visually investigate large data collections, search for patterns, and reduce noise through data filters and visual styles.
3. **Maltego**: A widely used data mining tool in cybersecurity that creates directed graphs for analysis. The Community Edition is available for free with some limitations.

\
**Practical Application**

* **Graph Visualization**: Useful for visualizing relationships and understanding the context of data.
* **Combining Data**: Aggregates data from different sources to identify suspicious patterns and behaviors.
* **User-Friendly**: Tools like Maltego and Linkurious make it easier for users without programming skills to interact with and analyze data.\

## MITRE Threat Group Tracker

**MITRE ATT\&CK Framework**

* **What It Is**: A knowledge base of adversarial tactics, techniques, and procedures (TTPs) used by attackers.
* **Purpose**: Helps organizations move towards a threat-informed defense by understanding and mitigating attacker behaviors.
* **Components**:
  * **Tactics**: The "why" of an attack (e.g., initial access, execution).
  * **Techniques**: The "how" of an attack (e.g., phishing, malware).
  * **Common Knowledge**: Documented behaviors and methods used by attackers.

\
**Benefits of MITRE ATT\&CK**

* **Standardization**: Provides a common language for describing adversary behavior, making it easier to share and compare threat intelligence.
* **Visualization**: Allows organizations to map their defense systems and identify strengths and weaknesses.
* **Prioritization**: Helps determine which techniques to focus on for mitigation and detection based on their relevance to specific threats.

\
**MITRE Threat Group Tracker**

* **What It Is**: A framework for tracking related intrusion activities by a common name in the security community.
* **Purpose**: Helps analysts track clusters of activities and understand the behavior of different threat groups.
* **Components**:
  * **Threat Groups**: Sets of related intrusion activities tracked by a common name.
  * **Activity Groups**: Clusters of activities using various analytic methodologies.
  * **Campaigns**: Specific intrusion sets or threat actors.

\
**Practical Use Case**

* **Example**: Comparing techniques used by APT3 (China-based) and APT29 (Russia-based).
  * **Color Coding**: Techniques unique to APT3 are blue, unique to APT29 are yellow, and common techniques are green.
  * **Prioritization**: Techniques in green (common to both groups) are high priority for mitigation and detection.

\
**How to Use MITRE ATT\&CK**

* **Start Small**: Begin with a single threat group and analyze their behaviors using the ATT\&CK framework.
* **Leverage Tools**: Use products and tools that map to ATT\&CK to enhance your analysis.
* **Collaborate**: Work with other analysts and defenders to compare and contrast threat groups and improve your defense strategies.\

## Threat Intelligence Naming Conventions

**What Are Naming Conventions?**

* **Definition**: A set of rules for choosing names to identify threat actors, APTs (Advanced Persistent Threats), campaigns, or operations.
* **Purpose**: Helps in organizing and cataloging threat patterns, making it easier to track and analyze them.

\
**Why Different Names for the Same Threat Actor?**

*   **Human Reasons**:

    * **Operation Name Used as Threat Actor Name**: Sometimes, the name of an operation is mistakenly used as the name of the threat actor.
    * **Malware Name Used as Threat Actor Name**: Similarly, malware names can be confused with threat actor names.
    * **Vendor Miscommunication**: Different vendors might misinterpret each other's research.
    * **Journalistic Errors**: Journalists may not always correct wrong mappings in public articles.


*   **Technical Reasons**:

    * **Partial Visibility**: Vendors see different parts of the full picture (e.g., different TTPs, IOC clusters).
    * **Group Dynamics**: Threat actors might join forces or split up, sharing tools and infrastructure.


* **Operational Reasons**:
  * **Vendor Independence**: Vendors prefer to maintain their own naming conventions for flexibility and reputation.
  * **Research Credibility**: Using another vendor's name might imply that their research is more complete.

\
**Examples of Naming Conventions**

* **FireEye/Mandiant, Cisco Talos**: Use numbers like APT28 or APT34.
* **CrowdStrike, Kaspersky, Symantec**: Use descriptive names (e.g., Panda for China, Kitten for Iran).

\
**Recommendations for Naming Conventions**

* **Avoid Numbers**: Numbers can be confusing and hard to track over time.
* **Avoid Tool-Based Names**: Naming after tools can create confusion if multiple campaigns use the same tool.
* **Be Creative and Flexible**: Adding humor or unique elements can make names easier to remember.
* **Base Names on Incidents**: Create names based on incidents you are directly facing, not just what you read about.

\
**Key Takeaways**

* **No Standardization**: There is no way to standardize all threat actor names due to various human, technical, and operational reasons.
* **Importance of Flexibility**: Being creative and flexible in naming conventions can help in better tracking and analysis.\
