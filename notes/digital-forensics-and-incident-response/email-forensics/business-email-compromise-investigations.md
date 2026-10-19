---
title: business-email-compromise-investigations
tags: [digital-forensics-and-incident-response, email-forensics, type/methodology, phase/forensics, platform/m365]
---

# Business Email Investigations

## Investigating using Hawk

### Introduction

Hawk is a free, open-source PowerShell module that streamlines the collection of forensic data from Microsoft cloud environments. Designed primarily for security professionals, incident responders, and administrators, Hawk automates the gathering of critical log data across Microsoft services, with a focus on Microsoft 365 (M365) and Microsoft Entra ID.

#### Core Capabilities

* **Data Collection**: Efficiently gather forensic data with automated collection processes
* **Security Analysis**: Examine security configurations, audit logs, and user activities
* **Export & Report**: Generate both CSV reports and JSON data for SIEM integration

{% hint style="success" %}
#### What Hawk is and isn't

While Hawk includes basic analysis capabilities to flag potential items of interest (such as suspicious mail forwarding rules, over-privileged applications, or risky user activities), it is fundamentally a data collection tool rather than an automated threat detection system.

Hawk streamlines data collection compared to manually running individual queries through web interfaces, freeing up those resources for other administrative tasks. The tool's goal is to quickly get you the data needed to come to a conclusion; not to make the conclusion for you.

#### Investigation Types

Hawk offers two main investigation approaches:

##### Tenant Investigations

* Examines broader Microsoft Cloud tenant settings, audit logs, and security configurations
* Provides an excellent starting point for identifying suspicious patterns
* Use `Start-HawkTenantInvestigation` to begin a tenant-wide investigation

##### User Investigations

* Performs deep-dive analysis into individual user accounts
* Examines mailbox configurations, inbox rules, and login histories
* Use `Start-HawkUserInvestigation -UserPrincipleName <user@domain.com>` to investigate specific users

#### Understanding Output

Hawk organizes investigation results into a structured directory hierarchy:

```
 [Investigation Root]
  Tenant/
    AdminAuditLogConfig.csv
    OrgConfig.csv
    _Investigate_*.csv
    [other tenant files]
  [user1@domain.com]/
    Mailbox_Info.csv
    InboxRules.csv
    _Investigate_*.csv
    [other user files]
  [user2@domain.com]/
     [similar structure]
```

Files prefixed with `_Investigate_` contain potentially suspicious findings that warrant further review.

{% hint style="warning" %}
#### System Requirements

* Windows operating system with administrator access
* PowerShell 5.0 or above (PowerShell Core will be supported in future)
* Network connectivity to:
  * PowerShell Gallery
  * Graph API
  * Microsoft 365 services

***

### 1. Preparation and Initial Setup

**A. Gather Necessary Permissions**

Ensure you have appropriate administrative permissions in the Microsoft 365 environment. This typically includes Global Administrator rights or, at a minimum, roles that allow you to access audit logs, mailbox settings, and security configurations.​

**B. Install the Hawk PowerShell Module**

Install Hawk by launching PowerShell with administrative privileges and executing:​

```powershell
Install-Module -Name Hawk
```

If prompted about installing from an untrusted repository, confirm by typing 'Y' and pressing Enter. ​Practical 365

**c. Set Up an Output Directory**

Create a dedicated directory to store the data extracts from Hawk:​Practical 365

```powershell
New-Item -Path "C:\Temp\Hawk" -ItemType Directory
```

***

### 2. Conduct a Tenant-Wide Investigation

**A. Connect to Necessary Services**

Establish connections to Exchange Online and the Microsoft Online Service (MSOL):​Practical 365

```powershell
Connect-ExchangeOnline
Connect-MsolService
```

**B. Initiate the Tenant Investigation**

Execute the tenant investigation to collect broad data across the organization:​Practical 365+1Hawk Forensics+1

```powershell
Start-HawkTenantInvestigation -OutputDirectory "C:\Temp\Hawk" -Days 30
```

This command collects logs and configurations from the past 30 days. ​Practical 365

***

### 3. Perform a User-Specific Investigation

**A. Identify Compromised Accounts**

Review the tenant investigation results to pinpoint accounts exhibiting suspicious activity.​

**B. Investigate Specific User Accounts**

For each suspected account, run:​

```powershell
Start-HawkUserInvestigation -UserPrincipalName "user@example.com" -OutputDirectory "C:\Temp\Hawk" -Days 30
```

Replace "[user@example.com](mailto:user@example.com)" with the actual User Principal Name (UPN) of the account under investigation. ​

***

### 4. Analyze Collected Data

**A. Review Sign-In Logs**

Examine the sign-in logs for anomalies such as logins from unfamiliar locations or devices.​

**B. Inspect Inbox Rules and Forwarding Settings**

Check for unauthorized inbox rules or forwarding settings that could indicate malicious activity.​

**C. Assess Mailbox Permissions**

Verify that mailbox permissions have not been altered to grant unauthorized access.​

***

### 5. Implement Remediation Measures

**A. Reset Compromised Credentials**

Force password resets and revoke existing sessions for affected accounts.​

**B. Remove Malicious Configurations**

Delete any unauthorized inbox rules, forwarding settings, or application consents identified during the investigation.​

**C. Enhance Security Posture**

Implement measures such as enabling multi-factor authentication (MFA), disabling legacy protocols, and conducting security awareness training to prevent future incidents.

## Microsoft Defender Explorer

### Steps to Follow

1.  **Access Threat Explorer**:

    * Navigate to the Microsoft 365 Defender portal at  Learn
    * In the navigation pane, select **Email & collaboration**, then choose **Explorer**.​Microsoft Learn

2.  **Search for Specific Emails**:

    * Use the search and filter options to locate emails based on criteria such as sender, recipient, subject, or detected threats.​
    * For instance, to identify phishing attempts, select the **Phish** view.​Microsoft Learn

3. **Analyze Email Details**:
   *   Click on individual emails to view detailed information, including:​

       * **Sender and recipient details**
       * **Delivery and filtering information**
       * **Detected threats**
       * **URLs and attachments**

4.  **Remediate Threats**:

    * Select the emails you wish to act upon.​
    * Click on **Take action** and choose the desired remediation action, such as **Soft Delete** or **Hard Delete**.​Microsoft Learn
    * Provide necessary details in the side pane, including a name for the remediation, severity, and description.​Microsoft Learn
    * Submit the action for approval.​Microsoft Learn

5.  **Track Remediation Actions**:

    * After submission, monitor the status of your actions in the **Action center** under the **History** tab.​
    * Use filters like remediation name, approval ID, or status to locate specific actions.​Microsoft Learn

**Best Practices**:

* **Batch Processing**: For optimal performance, limit remediation actions to batches of 50,000 emails or fewer.​
* **Targeted Remediation**: Focus on emails in folders like Inbox, Junk, or Deleted Items to ensure effective remediation.​Microsoft Learn
* **Two-Step Approval**: Implement a two-step approval process for remediation actions to enhance security and oversight.

***

## REFERENCES

* 
* 
* 
