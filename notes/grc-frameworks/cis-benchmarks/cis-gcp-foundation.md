---
title: cis-gcp-foundation
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/gcp, source/cis]
description: "CIS Google Cloud Platform Foundation Benchmark v4.0.0 checklist: IAM, logging, network, VMs, storage, SQL, with levels."
source_pdf: CIS_Google_Cloud_Platform_Foundation_Benchmark_v4.0.0.pdf
---

# CIS Google Cloud Platform Foundation Benchmark v4.0.0 (05-02-2025)

## Overview

- **Product:** Google Cloud Platform foundations
- **Benchmark version:** v4.0.0 (2025-05-02)
- **Profiles:** Level 1 and Level 2.
- **Recommendations:** 84 total (72 Automated, 12 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Identity and Access Management | 17 |
| 2 Logging and Monitoring | 16 |
| 3 Networking | 10 |
| 4 Virtual Machines | 12 |
| 5 Storage | 2 |
| 6 Cloud SQL Database Services | 22 |
| 7 BigQuery | 4 |
| 8 Dataproc | 1 |

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Identity and Access Management

- [ ] 1.1 Ensure that Corporate Login Credentials are Used — L1 · Manual
- [ ] 1.2 Ensure that Multi-Factor Authentication is 'Enabled' for All Non-Service Accounts — L1 · Manual
- [ ] 1.3 Ensure that Security Key Enforcement is Enabled for All Admin Accounts — L2 · Manual
- [ ] 1.4 Ensure That There Are Only GCP-Managed Service Account Keys for Each Service Account — L1 · Automated
- [ ] 1.5 Ensure That Service Account Has No Admin Privileges — L1 · Automated
- [ ] 1.6 Ensure That IAM Users Are Not Assigned the Service Account User or Service Account Token Creator Roles at Project Level — L1 · Automated
- [ ] 1.7 Ensure User-Managed/External Keys for Service Accounts Are Rotated Every 90 Days or Fewer — L1 · Automated
- [ ] 1.8 Ensure That Separation of Duties Is Enforced While Assigning Service Account Related Roles to Users — L2 · Automated
- [ ] 1.9 Ensure That Cloud KMS Cryptokeys Are Not Anonymously or Publicly Accessible — L1 · Automated
- [ ] 1.10 Ensure KMS Encryption Keys Are Rotated Within a Period of 90 Days — L1 · Automated
- [ ] 1.11 Ensure That Separation of Duties Is Enforced While Assigning KMS Related Roles to Users — L2 · Automated
- [ ] 1.12 Ensure API Keys Only Exist for Active Services — L2 · Automated
- [ ] 1.13 Ensure API Keys Are Restricted To Use by Only Specified Hosts and Apps — L2 · Manual
- [ ] 1.14 Ensure API Keys Are Restricted to Only APIs That Application Needs Access — L2 · Automated
- [ ] 1.15 Ensure API Keys Are Rotated Every 90 Days — L2 · Automated
- [ ] 1.16 Ensure Essential Contacts is Configured for Organization — L1 · Automated
- [ ] 1.17 Ensure Secrets are Not Stored in Cloud Functions Environment Variables by Using Secret Manager — L1 · Manual

### 2 Logging and Monitoring

- [ ] 2.1 Ensure That Cloud Audit Logging Is Configured Properly — L1 · Automated
- [ ] 2.2 Ensure That Sinks Are Configured for All Log Entries — L1 · Automated
- [ ] 2.3 Ensure That Retention Policies on Cloud Storage Buckets Used for Exporting Logs Are Configured Using Bucket Lock — L2 · Automated
- [ ] 2.4 Ensure Log Metric Filter and Alerts Exist for Project Ownership Assignments/Changes — L1 · Automated
- [ ] 2.5 Ensure That the Log Metric Filter and Alerts Exist for Audit Configuration Changes — L1 · Automated
- [ ] 2.6 Ensure That the Log Metric Filter and Alerts Exist for Custom Role Changes — L1 · Automated
- [ ] 2.7 Ensure That the Log Metric Filter and Alerts Exist for VPC Network Firewall Rule Changes — L2 · Automated
- [ ] 2.8 Ensure That the Log Metric Filter and Alerts Exist for VPC Network Route Changes — L2 · Automated
- [ ] 2.9 Ensure That the Log Metric Filter and Alerts Exist for VPC Network Changes — L2 · Automated
- [ ] 2.10 Ensure That the Log Metric Filter and Alerts Exist for Cloud Storage IAM Permission Changes — L2 · Automated
- [ ] 2.11 Ensure That the Log Metric Filter and Alerts Exist for SQL Instance Configuration Changes — L2 · Automated
- [ ] 2.12 Ensure That Cloud DNS Logging Is Enabled for All VPC Networks — L1 · Automated
- [ ] 2.13 Ensure Cloud Asset Inventory Is Enabled — L1 · Automated
- [ ] 2.14 Ensure 'Access Transparency' is 'Enabled' — L2 · Manual
- [ ] 2.15 Ensure 'Access Approval' is 'Enabled' — L2 · Automated
- [ ] 2.16 Ensure Logging is enabled for HTTP(S) Load Balancer — L2 · Automated

### 3 Networking

- [ ] 3.1 Ensure That the Default Network Does Not Exist in a Project — L2 · Automated
- [ ] 3.2 Ensure Legacy Networks Do Not Exist for Older Projects — L1 · Automated
- [ ] 3.3 Ensure That DNSSEC Is Enabled for Cloud DNS — L1 · Automated
- [ ] 3.4 Ensure That RSASHA1 Is Not Used for the Key-Signing Key in Cloud DNS DNSSEC — L1 · Automated
- [ ] 3.5 Ensure That RSASHA1 Is Not Used for the Zone-Signing Key in Cloud DNS DNSSEC — L1 · Automated
- [ ] 3.6 Ensure That SSH Access Is Restricted From the Internet — L2 · Automated
- [ ] 3.7 Ensure That RDP Access Is Restricted From the Internet — L2 · Automated
- [ ] 3.8 Ensure that VPC Flow Logs is Enabled for Every Subnet in a VPC Network — L2 · Automated
- [ ] 3.9 Ensure No HTTPS or SSL Proxy Load Balancers Permit SSL Policies With Weak Cipher Suites — L1 · Manual
- [ ] 3.10 Use Identity Aware Proxy (IAP) to Ensure Only Traffic From Google IP Addresses are 'Allowed' — L2 · Manual

### 4 Virtual Machines

- [ ] 4.1 Ensure That Instances Are Not Configured To Use the Default Service Account — L1 · Automated
- [ ] 4.2 Ensure That Instances Are Not Configured To Use the Default Service Account With Full Access to All Cloud APIs — L1 · Automated
- [ ] 4.3 Ensure “Block Project-Wide SSH Keys” Is Enabled for VM Instances — L1 · Automated
- [ ] 4.4 Ensure Oslogin Is Enabled for a Project — L1 · Automated
- [ ] 4.5 Ensure ‘Enable Connecting to Serial Ports’ Is Not Enabled for VM Instance — L1 · Automated
- [ ] 4.6 Ensure That IP Forwarding Is Not Enabled on Instances — L1 · Automated
- [ ] 4.7 Ensure VM Disks for Critical VMs Are Encrypted With Customer-Supplied Encryption Keys (CSEK) — L2 · Automated
- [ ] 4.8 Ensure Compute Instances Are Launched With Shielded VM Enabled — L2 · Automated
- [ ] 4.9 Ensure That Compute Instances Do Not Have Public IP Addresses — L2 · Automated
- [ ] 4.10 Ensure That App Engine Applications Enforce HTTPS Connections — L2 · Manual
- [ ] 4.11 Ensure That Compute Instances Have Confidential Computing Enabled — L2 · Automated
- [ ] 4.12 Ensure the Latest Operating System Updates Are Installed On Your Virtual Machines in All Projects — L2 · Manual

### 5 Storage

- [ ] 5.1 Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible — L1 · Automated
- [ ] 5.2 Ensure That Cloud Storage Buckets Have Uniform Bucket-Level Access Enabled — L2 · Automated

### 6 Cloud SQL Database Services

#### 6.1 MySQL Database

- [ ] 6.1.1 Ensure That a MySQL Instance Does Not Allow Anyone To Connect With Administrative Privileges — L1 · Manual
- [ ] 6.1.2 Ensure ‘Skip_show_database’ Database Flag for Cloud SQL MySQL Instance Is Set to ‘On’ — L1 · Automated
- [ ] 6.1.3 Ensure That the ‘Local_infile’ Database Flag for a Cloud SQL MySQL Instance Is Set to ‘Off’ — L1 · Automated

#### 6.2 PostgreSQL Database

- [ ] 6.2.1 Ensure ‘Log_error_verbosity’ Database Flag for Cloud SQL PostgreSQL Instance Is Set to ‘DEFAULT’ or Stricter — L2 · Automated
- [ ] 6.2.2 Ensure That the ‘Log_connections’ Database Flag for Cloud SQL PostgreSQL Instance Is Set to ‘On’ — L1 · Automated
- [ ] 6.2.3 Ensure That the ‘Log_disconnections’ Database Flag for Cloud SQL PostgreSQL Instance Is Set to ‘On’ — L1 · Automated
- [ ] 6.2.4 Ensure ‘Log_statement’ Database Flag for Cloud SQL PostgreSQL Instance Is Set Appropriately — L2 · Automated
- [ ] 6.2.5 Ensure that the ‘Log_min_messages’ Flag for a Cloud SQL PostgreSQL Instance is set at minimum to 'Warning' — L1 · Automated
- [ ] 6.2.6 Ensure ‘Log_min_error_statement’ Database Flag for Cloud SQL PostgreSQL Instance Is Set to ‘Error’ or Stricter — L1 · Automated
- [ ] 6.2.7 Ensure That the ‘Log_min_duration_statement’ Database Flag for Cloud SQL PostgreSQL Instance Is Set to '-1' (Disabled) — L1 · Automated
- [ ] 6.2.8 Ensure That 'cloudsql.enable_pgaudit' Database Flag for each Cloud Sql Postgresql Instance Is Set to 'on' For Centralized Logging — L1 · Automated

#### 6.3 SQL Server

- [ ] 6.3.1 Ensure 'external scripts enabled' Database Flag for Cloud SQL SQL Server Instance Is Set to 'off' — L1 · Automated
- [ ] 6.3.2 Ensure 'cross db ownership chaining' Database Flag for Cloud SQL SQL Server Instance Is Set to 'off' — L1 · Automated
- [ ] 6.3.3 Ensure 'user Connections' Database Flag for Cloud SQL SQL Server Instance Is Set to a Non-limiting Value — L1 · Automated
- [ ] 6.3.4 Ensure 'user options' Database Flag for Cloud SQL SQL Server Instance Is Not Configured — L1 · Automated
- [ ] 6.3.5 Ensure 'remote access' Database Flag for Cloud SQL SQL Server Instance Is Set to 'off' — L1 · Automated
- [ ] 6.3.6 Ensure '3625 (trace flag)' Database Flag for all Cloud SQL SQL Server Instances Is Set to 'on' — L1 · Automated
- [ ] 6.3.7 Ensure 'contained database authentication' Database Flag for Cloud SQL SQL Server Instance Is Set to 'off' — L1 · Automated
- [ ] 6.4 Ensure That the Cloud SQL Database Instance Requires All Incoming Connections To Use SSL — L1 · Automated
- [ ] 6.5 Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses — L1 · Automated
- [ ] 6.6 Ensure That Cloud SQL Database Instances Do Not Have Public IPs — L2 · Automated
- [ ] 6.7 Ensure That Cloud SQL Database Instances Are Configured With Automated Backups — L1 · Automated

### 7 BigQuery

- [ ] 7.1 Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible — L1 · Automated
- [ ] 7.2 Ensure That All BigQuery Tables Are Encrypted With Customer-Managed Encryption Key (CMEK) — L2 · Automated
- [ ] 7.3 Ensure That a Default Customer-Managed Encryption Key (CMEK) Is Specified for All BigQuery Data Sets — L2 · Automated
- [ ] 7.4 Ensure all data in BigQuery has been classified — L2 · Manual

### 8 Dataproc

- [ ] 8.1 Ensure that Dataproc Cluster is encrypted using Customer-Managed Encryption Key — L2 · Automated

## Source

CIS Google Cloud Platform Foundation Benchmark v4.0.0 (05-02-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[grc-frameworks/cis-benchmarks/cis-aws-foundations]]
- [[grc-frameworks/cis-benchmarks/cis-azure-foundations]]
- [[cloud-pentesting/aws-pentesting/attacks-and-methodology/aws-pentest-methodology]]
- [[cloud-pentesting/aws-pentesting/tools/prowler]]
- [[cloud-pentesting/aws-pentesting/initial-access/leaked-secrets]]
