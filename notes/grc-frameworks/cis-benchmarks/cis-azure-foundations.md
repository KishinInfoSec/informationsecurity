---
title: cis-azure-foundations
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/azure, source/cis]
description: "CIS Azure Foundations Benchmark v5.0.0 checklist: identity, logging, networking, storage, Defender, with levels."
source_pdf: CIS_Microsoft_Azure_Foundations_Benchmark_v5.0.0.pdf
---

# CIS Microsoft Azure Foundations Benchmark v5.0.0 (09-30-2025)

## Overview

- **Product:** Microsoft Azure subscription foundations (incl. Entra ID)
- **Benchmark version:** v5.0.0 (2025-09-30)
- **Profiles:** Level 1 and Level 2.
- **Recommendations:** 155 total (93 Automated, 62 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Introduction | 0 |
| 2 Analytics Services | 11 |
| 3 Compute Services | 1 |
| 4 Database Services (reference) | 0 |
| 5 Identity Services | 43 |
| 6 Management and Governance Services | 25 |
| 7 Networking Services | 16 |
| 8 Security Services | 38 |
| 9 Storage Services | 21 |

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 2 Analytics Services

#### 2.1 Azure Databricks

- [ ] 2.1.1 Ensure that Azure Databricks is deployed in a customer-managed virtual network (VNet) — L1 · Automated
- [ ] 2.1.2 Ensure that network security groups are configured for Databricks subnets — L1 · Automated
- [ ] 2.1.3 Ensure that traffic is encrypted between cluster worker nodes — L2 · Manual
- [ ] 2.1.4 Ensure that users and groups are synced from Microsoft Entra ID to Azure Databricks — L1 · Manual
- [ ] 2.1.5 Ensure that Unity Catalog is configured for Azure Databricks — L1 · Manual
- [ ] 2.1.6 Ensure that usage is restricted and expiry is enforced for Databricks personal access tokens — L1 · Manual
- [ ] 2.1.7 Ensure that diagnostic log delivery is configured for Azure Databricks — L1 · Automated
- [ ] 2.1.8 Ensure critical data in Azure Databricks is encrypted with customer-managed keys (CMK) — L2 · Manual
- [ ] 2.1.9 Ensure 'No Public IP' is set to 'Enabled' — L1 · Automated
- [ ] 2.1.10 Ensure 'Allow Public Network Access' is set to 'Disabled' — L1 · Automated
- [ ] 2.1.11 Ensure private endpoints are used to access Azure Databricks workspaces — L2 · Automated

### 3 Compute Services

#### 3.1 Virtual Machines

- [ ] 3.1.1 Ensure only MFA enabled identities can access privileged Virtual Machine — L2 · Manual

### 5 Identity Services

#### 5.1 Security Defaults (Per-User MFA)

- [ ] 5.1.1 Ensure that 'security defaults' is enabled in Microsoft Entra ID — L1 · Automated
- [ ] 5.1.2 Ensure that 'multifactor authentication' is 'enabled' for all users — L1 · Automated
- [ ] 5.1.3 Ensure that 'Allow users to remember multifactor authentication on devices they trust' is disabled — L1 · Manual

#### 5.2 Conditional Access

- [ ] 5.2.1 Ensure that 'trusted locations' are defined — L2 · Manual
- [ ] 5.2.2 Ensure that an exclusionary geographic Conditional Access policy is considered — L2 · Manual
- [ ] 5.2.3 Ensure that an exclusionary device code flow policy is considered — L2 · Manual
- [ ] 5.2.4 Ensure that a multifactor authentication policy exists for all users — L2 · Manual
- [ ] 5.2.5 Ensure that multifactor authentication is required for risky sign-ins — L2 · Manual
- [ ] 5.2.6 Ensure that multifactor authentication is required for Windows Azure Service Management API — L2 · Manual
- [ ] 5.2.7 Ensure that multifactor authentication is required to access Microsoft Admin Portals — L2 · Manual
- [ ] 5.2.8 Ensure a Token Protection Conditional Access policy is considered — L2 · Manual

#### 5.3 Periodic Identity Reviews

- [ ] 5.3.1 Ensure that Azure admin accounts are not used for daily operations — L1 · Manual
- [ ] 5.3.2 Ensure that guest users are reviewed on a regular basis — L1 · Manual
- [ ] 5.3.3 Ensure that use of the 'User Access Administrator' role is restricted — L1 · Automated
- [ ] 5.3.4 Ensure that all 'privileged' role assignments are periodically reviewed — L1 · Manual
- [ ] 5.3.5 Ensure disabled user accounts do not have read, write, or owner permissions — L1 · Manual
- [ ] 5.3.6 Ensure 'Tenant Creator' role assignments are periodically reviewed — L1 · Manual
- [ ] 5.3.7 Ensure all non-privileged role assignments are periodically reviewed — L1 · Manual
- [ ] 5.4 Ensure that 'Restrict non-admin users from creating tenants' is set to 'Yes' — L1 · Automated
- [ ] 5.5 Ensure that 'Number of methods required to reset' is set to '2' — L1 · Manual
- [ ] 5.6 Ensure that account 'Lockout threshold' is less than or equal to '10' — L1 · Manual
- [ ] 5.7 Ensure that account 'Lockout duration in seconds' is greater than or equal to '60' — L1 · Manual
- [ ] 5.8 Ensure that a 'Custom banned password list' is set to 'Enforce' — L1 · Manual
- [ ] 5.9 Ensure that 'Number of days before users are asked to re-confirm their authentication information' is not set to '0' — L1 · Manual
- [ ] 5.10 Ensure that 'Notify users on password resets?' is set to 'Yes' — L1 · Manual
- [ ] 5.11 Ensure that 'Notify all admins when other admins reset their password?' is set to 'Yes' — L1 · Manual
- [ ] 5.12 Ensure that 'User consent for applications' is set to 'Do not allow user consent' — L1 · Manual
- [ ] 5.13 Ensure that 'User consent for applications' is set to 'Allow user consent for apps from verified publishers, for selected permissions' — L2 · Manual
- [ ] 5.14 Ensure that 'Users can register applications' is set to 'No' — L1 · Automated
- [ ] 5.15 Ensure that 'Guest users access restrictions' is set to 'Guest user access is restricted to properties and memberships of their own directory objects' — L1 · Automated
- [ ] 5.16 Ensure that 'Guest invite restrictions' is set to 'Only users assigned to specific admin roles [...]' or 'No one [..]' — L2 · Automated
- [ ] 5.17 Ensure that 'Restrict access to Microsoft Entra admin center' is set to 'Yes' — L1 · Manual
- [ ] 5.18 Ensure that 'Restrict user ability to access groups features in My Groups' is set to 'Yes' — L2 · Manual
- [ ] 5.19 Ensure that 'Users can create security groups in Azure portals, API or PowerShell' is set to 'No' — L2 · Manual
- [ ] 5.20 Ensure that 'Owners can manage group membership requests in My Groups' is set to 'No' — L2 · Manual
- [ ] 5.21 Ensure that 'Users can create Microsoft 365 groups in Azure portals, API or PowerShell' is set to 'No' — L2 · Manual
- [ ] 5.22 Ensure that 'Require Multifactor Authentication to register or join devices with Microsoft Entra' is set to 'Yes' — L1 · Manual
- [ ] 5.23 Ensure that no custom subscription administrator roles exist — L1 · Automated
- [ ] 5.24 Ensure that a custom role is assigned permissions for administering resource locks — L2 · Manual
- [ ] 5.25 Ensure that 'Subscription leaving Microsoft Entra tenant' and 'Subscription entering Microsoft Entra tenant' is set to 'Permit no one' — L2 · Manual
- [ ] 5.26 Ensure fewer than 5 users have global administrator assignment — L1 · Manual
- [ ] 5.27 Ensure there are between 2 and 3 subscription owners — L1 · Automated
- [ ] 5.28 Ensure passwordless authentication methods are considered — L2 · Manual

### 6 Management and Governance Services

#### 6.1 Logging and Monitoring

**6.1.1 Configuring Diagnostic Settings**

- [ ] 6.1.1.1 Ensure that a 'Diagnostic Setting' exists for Subscription Activity Logs — L1 · Automated
- [ ] 6.1.1.2 Ensure Diagnostic Setting captures appropriate categories — L1 · Automated
- [ ] 6.1.1.3 Ensure the storage account containing the container with activity logs is encrypted with customer-managed key (CMK) — L2 · Manual
- [ ] 6.1.1.4 Ensure that logging for Azure Key Vault is 'Enabled' — L1 · Automated
- [ ] 6.1.1.5 Ensure that Network Security Group Flow logs are captured and sent to Log Analytics — L2 · Manual
- [ ] 6.1.1.6 Ensure that logging for Azure AppService 'HTTP logs' is enabled — L2 · Automated
- [ ] 6.1.1.7 Ensure that virtual network flow logs are captured and sent to Log Analytics — L2 · Manual
- [ ] 6.1.1.8 Ensure that a Microsoft Entra diagnostic setting exists to send Microsoft Graph activity logs to an appropriate destination — L2 · Manual
- [ ] 6.1.1.9 Ensure that a Microsoft Entra diagnostic setting exists to send Microsoft Entra activity logs to an appropriate destination — L2 · Manual
- [ ] 6.1.1.10 Ensure that Intune logs are captured and sent to Log Analytics — L2 · Manual

**6.1.2 Monitoring using Activity Log Alerts**

- [ ] 6.1.2.1 Ensure that Activity Log Alert exists for Create Policy Assignment — L1 · Automated
- [ ] 6.1.2.2 Ensure that Activity Log Alert exists for Delete Policy Assignment — L1 · Automated
- [ ] 6.1.2.3 Ensure that Activity Log Alert exists for Create or Update Network Security Group — L1 · Automated
- [ ] 6.1.2.4 Ensure that Activity Log Alert exists for Delete Network Security Group — L1 · Automated
- [ ] 6.1.2.5 Ensure that Activity Log Alert exists for Create or Update Security Solution — L1 · Automated
- [ ] 6.1.2.6 Ensure that Activity Log Alert exists for Delete Security Solution — L1 · Automated
- [ ] 6.1.2.7 Ensure that Activity Log Alert exists for Create or Update SQL Server Firewall Rule — L1 · Automated
- [ ] 6.1.2.8 Ensure that Activity Log Alert exists for Delete SQL Server Firewall Rule — L1 · Automated
- [ ] 6.1.2.9 Ensure that Activity Log Alert exists for Create or Update Public IP Address rule — L1 · Automated
- [ ] 6.1.2.10 Ensure that Activity Log Alert exists for Delete Public IP Address rule — L1 · Automated
- [ ] 6.1.2.11 Ensure that an Activity Log Alert exists for Service Health — L1 · Automated

**6.1.3 Configuring Application Insights**

- [ ] 6.1.3.1 Ensure Application Insights are Configured — L2 · Automated
- [ ] 6.1.4 Ensure that Azure Monitor Resource Logging is Enabled for All Services that Support it — L1 · Manual
- [ ] 6.1.5 Ensure that SKU Basic/Consumption is not used on artifacts that need to be monitored (Particularly for Production Workloads) — L2 · Manual
- [ ] 6.2 Ensure that Resource Locks are set for Mission-Critical Azure Resources — L2 · Manual

### 7 Networking Services

- [ ] 7.1 Ensure that RDP access from the Internet is evaluated and restricted — L1 · Automated
- [ ] 7.2 Ensure that SSH access from the Internet is evaluated and restricted — L1 · Automated
- [ ] 7.3 Ensure that UDP access from the Internet is evaluated and restricted — L1 · Automated
- [ ] 7.4 Ensure that HTTP(S) access from the Internet is evaluated and restricted — L1 · Automated
- [ ] 7.5 Ensure that network security group flow log retention days is set to greater than or equal to 90 — L2 · Automated
- [ ] 7.6 Ensure that Network Watcher is 'Enabled' for Azure Regions that are in use — L2 · Automated
- [ ] 7.7 Ensure that Public IP addresses are Evaluated on a Periodic Basis — L1 · Manual
- [ ] 7.8 Ensure that virtual network flow log retention days is set to greater than or equal to 90 — L2 · Automated
- [ ] 7.9 Ensure 'Authentication type' is set to 'Azure Active Directory' only for Azure VPN Gateway point-to-site configuration — L2 · Manual
- [ ] 7.10 Ensure Azure Web Application Firewall (WAF) is enabled on Azure Application Gateway — L2 · Automated
- [ ] 7.11 Ensure subnets are associated with network security groups — L1 · Automated
- [ ] 7.12 Ensure the SSL policy's 'Min protocol version' is set to 'TLSv1_2' or higher on Azure Application Gateway — L1 · Automated
- [ ] 7.13 Ensure 'HTTP2' is set to 'Enabled' on Azure Application Gateway — L1 · Automated
- [ ] 7.14 Ensure request body inspection is enabled in Azure Web Application Firewall policy on Azure Application Gateway — L2 · Automated
- [ ] 7.15 Ensure bot protection is enabled in Azure Web Application Firewall policy on Azure Application Gateway — L2 · Automated
- [ ] 7.16 Ensure Azure Network Security Perimeter is used to secure Azure platform-as-a-service resources — L2 · Manual

### 8 Security Services

#### 8.1 Microsoft Defender for Cloud

**8.1.1 Microsoft Cloud Security Posture Management (CSPM)**

- [ ] 8.1.1.1 Ensure Microsoft Defender CSPM is set to 'On' — L2 · Automated

**8.1.2 Defender Plan: APIs**

- [ ] 8.1.2.1 Ensure Microsoft Defender for APIs is set to 'On' — L2 · Automated

**8.1.3 Defender Plan: Servers**

- [ ] 8.1.3.1 Ensure that Defender for Servers is set to 'On' — L2 · Automated
- [ ] 8.1.3.2 Ensure that 'Vulnerability assessment for machines' component status is set to 'On' — L2 · Manual
- [ ] 8.1.3.3 Ensure that 'Endpoint protection' component status is set to 'On' — L2 · Automated
- [ ] 8.1.3.4 Ensure that 'Agentless scanning for machines' component status is set to 'On' — L2 · Manual
- [ ] 8.1.3.5 Ensure that 'File Integrity Monitoring' component status is set to 'On' — L2 · Manual

**8.1.4 Defender Plan: Containers**

- [ ] 8.1.4.1 Ensure That Microsoft Defender for Containers Is Set To 'On' — L2 · Automated

**8.1.5 Defender Plan: Storage**

- [ ] 8.1.5.1 Ensure That Microsoft Defender for Storage Is Set To 'On' — L2 · Automated
- [ ] 8.1.5.2 Ensure Advanced Threat Protection Alerts for Storage Accounts Are Monitored — L2 · Manual

**8.1.6 Defender Plan: App Service**

- [ ] 8.1.6.1 Ensure That Microsoft Defender for App Services Is Set To 'On' — L2 · Automated

**8.1.7 Defender Plan: Databases**

- [ ] 8.1.7.1 Ensure That Microsoft Defender for Azure Cosmos DB Is Set To 'On' — L2 · Automated
- [ ] 8.1.7.2 Ensure That Microsoft Defender for Open-Source Relational Databases Is Set To 'On' — L2 · Automated
- [ ] 8.1.7.3 Ensure That Microsoft Defender for (Managed Instance) Azure SQL Databases Is Set To 'On' — L2 · Automated
- [ ] 8.1.7.4 Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On' — L2 · Automated

**8.1.8 Defender Plan: Key Vault**

- [ ] 8.1.8.1 Ensure That Microsoft Defender for Key Vault Is Set To 'On' — L2 · Automated

**8.1.9 Defender Plan: Resource Manager**

- [ ] 8.1.9.1 Ensure That Microsoft Defender for Resource Manager Is Set To 'On' — L2 · Automated
- [ ] 8.1.10 Ensure that Microsoft Defender for Cloud is configured to check VM operating systems for updates — L1 · Automated
- [ ] 8.1.11 Ensure that Microsoft Cloud Security Benchmark policies are not set to 'Disabled' — L1 · Manual
- [ ] 8.1.12 Ensure That 'All users with the following roles' is set to 'Owner' — L1 · Automated
- [ ] 8.1.13 Ensure 'Additional email addresses' is Configured with a Security Contact Email — L1 · Automated
- [ ] 8.1.14 Ensure that 'Notify about alerts with the following severity (or higher)' is enabled — L1 · Automated
- [ ] 8.1.15 Ensure that 'Notify about attack paths with the following risk level (or higher)' is enabled — L1 · Automated
- [ ] 8.1.16 Ensure that Microsoft Defender External Attack Surface Monitoring (EASM) is enabled — L2 · Manual

#### 8.2 Microsoft Defender for IoT

- [ ] 8.2.1 Ensure That Microsoft Defender for IoT Hub Is Set To 'On' — L2 · Manual

#### 8.3 Key Vault

- [ ] 8.3.1 Ensure that the Expiration Date is set for all Keys in RBAC Key Vaults — L1 · Automated
- [ ] 8.3.2 Ensure that the Expiration Date is set for all Keys in Non-RBAC Key Vaults. — L1 · Automated
- [ ] 8.3.3 Ensure that the Expiration Date is set for all Secrets in RBAC Key Vaults — L1 · Automated
- [ ] 8.3.4 Ensure that the Expiration Date is set for all Secrets in Non-RBAC Key Vaults — L1 · Automated
- [ ] 8.3.5 Ensure 'Purge protection' is set to 'Enabled' — L1 · Automated
- [ ] 8.3.6 Ensure that Role Based Access Control for Azure Key Vault is enabled — L2 · Automated
- [ ] 8.3.7 Ensure Public Network Access is Disabled — L1 · Automated
- [ ] 8.3.8 Ensure Private Endpoints are used to access Azure Key Vault — L2 · Automated
- [ ] 8.3.9 Ensure automatic key rotation is enabled within Azure Key Vault — L2 · Automated
- [ ] 8.3.10 Ensure that Azure Key Vault Managed HSM is used when required — L2 · Manual
- [ ] 8.3.11 Ensure certificate 'Validity Period (in months)' is less than or equal to '12' — L1 · Automated

#### 8.4 Azure Bastion

- [ ] 8.4.1 Ensure an Azure Bastion Host Exists — L2 · Automated
- [ ] 8.5 Ensure Azure DDoS Network Protection is enabled on virtual networks — L2 · Automated

### 9 Storage Services

#### 9.1 Azure Files

- [ ] 9.1.1 Ensure soft delete for Azure File Shares is Enabled — L1 · Automated
- [ ] 9.1.2 Ensure 'SMB protocol version' is set to 'SMB 3.1.1' or higher for SMB file shares — L1 · Automated
- [ ] 9.1.3 Ensure 'SMB channel encryption' is set to 'AES-256-GCM' or higher for SMB file shares — L1 · Automated

#### 9.2 Azure Blob Storage

- [ ] 9.2.1 Ensure that soft delete for blobs on Azure Blob Storage storage accounts is Enabled — L1 · Automated
- [ ] 9.2.2 Ensure that soft delete for containers on Azure Blob Storage storage accounts is Enabled — L1 · Automated
- [ ] 9.2.3 Ensure 'Versioning' is set to 'Enabled' on Azure Blob Storage storage accounts — L2 · Automated

#### 9.3 Storage Accounts

**9.3.1 Secrets and Keys**

- [ ] 9.3.1.1 Ensure that 'Enable key rotation reminders' is enabled for each Storage Account — L1 · Automated
- [ ] 9.3.1.2 Ensure that Storage Account access keys are periodically regenerated — L1 · Automated
- [ ] 9.3.1.3 Ensure 'Allow storage account key access' for Azure Storage Accounts is 'Disabled' — L1 · Automated

**9.3.2 Networking**

- [ ] 9.3.2.1 Ensure Private Endpoints are used to access Storage Accounts — L2 · Automated
- [ ] 9.3.2.2 Ensure that 'Public Network Access' is 'Disabled' for storage accounts — L1 · Automated
- [ ] 9.3.2.3 Ensure default network access rule for storage accounts is set to deny — L1 · Automated

**9.3.3 Identity and Access Management**

- [ ] 9.3.3.1 Ensure that 'Default to Microsoft Entra authorization in the Azure portal' is set to 'Enabled' — L1 · Automated
- [ ] 9.3.4 Ensure that 'Secure transfer required' is set to 'Enabled' — L1 · Automated
- [ ] 9.3.5 Ensure 'Allow Azure services on the trusted services list to access this storage account' is Enabled for Storage Account Access — L2 · Automated
- [ ] 9.3.6 Ensure the 'Minimum TLS version' for storage accounts is set to 'Version 1.2' — L1 · Automated
- [ ] 9.3.7 Ensure 'Cross Tenant Replication' is not enabled — L1 · Automated
- [ ] 9.3.8 Ensure that 'Allow Blob Anonymous Access' is set to 'Disabled' — L1 · Automated
- [ ] 9.3.9 Ensure Azure Resource Manager Delete locks are applied to Azure Storage Accounts — L1 · Manual
- [ ] 9.3.10 Ensure Azure Resource Manager ReadOnly locks are considered for Azure Storage Accounts — L2 · Manual
- [ ] 9.3.11 Ensure Redundancy is set to 'geo-redundant storage (GRS)' on critical Azure Storage Accounts — L2 · Automated

## Source

CIS Microsoft Azure Foundations Benchmark v5.0.0 (09-30-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[cloud-pentesting/azure-pentesting]]
- [[cloud-pentesting/azure-pentesting/azure-attack-matrix]]
- [[cloud-pentesting/azure-pentesting/stealing-access-tokens]]
- [[cloud-pentesting/azure-pentesting/lateral-movement-skeleton-key-attack]]
- [[grc-frameworks/cis-benchmarks/cis-aws-foundations]]
- [[grc-frameworks/cis-benchmarks/cis-gcp-foundation]]
