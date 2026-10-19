---
title: cis-aws-foundations
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/aws, source/cis]
description: "CIS AWS Foundations Benchmark v6.0.0 checklist: IAM, storage, logging, monitoring, networking, with levels."
source_pdf: CIS_Amazon_Web_Services_Foundations_Benchmark_v6.0.0.pdf
---

# CIS Amazon Web Services Foundations Benchmark v6.0.0 (09-23-2025)

## Overview

- **Product:** Amazon Web Services account foundations
- **Benchmark version:** v6.0.0 (2025-09-23)
- **Profiles:** Level 1 and Level 2.
- **Recommendations:** 63 total (35 Automated, 28 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Introduction | 0 |
| 2 Identity and Access Management | 21 |
| 3 Storage | 9 |
| 4 Logging | 9 |
| 5 Monitoring | 16 |
| 6 Networking | 8 |

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 2 Identity and Access Management

- [ ] 2.1 Maintain current contact details — L1 · Manual
- [ ] 2.2 Ensure security contact information is registered — L1 · Manual
- [ ] 2.3 Ensure no 'root' user account access key exists — L1 · Automated
- [ ] 2.4 Ensure MFA is enabled for the 'root' user account — L1 · Automated
- [ ] 2.5 Ensure hardware MFA is enabled for the 'root' user account — L2 · Manual
- [ ] 2.6 Eliminate use of the 'root' user for administrative and daily tasks — L1 · Manual
- [ ] 2.7 Ensure IAM password policy requires minimum length of 14 or greater — L1 · Automated
- [ ] 2.8 Ensure IAM password policy prevents password reuse — L1 · Automated
- [ ] 2.9 Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password — L1 · Automated
- [ ] 2.10 Do not create access keys during initial setup for IAM users with a console password — L1 · Manual
- [ ] 2.11 Ensure credentials unused for 45 days or more are disabled — L1 · Automated
- [ ] 2.12 Ensure there is only one active access key for any single IAM user — L1 · Automated
- [ ] 2.13 Ensure access keys are rotated every 90 days or less — L1 · Automated
- [ ] 2.14 Ensure IAM users receive permissions only through groups — L1 · Automated
- [ ] 2.15 Ensure IAM policies that allow full "*:*" administrative privileges are not attached — L1 · Automated
- [ ] 2.16 Ensure a support role has been created to manage incidents with AWS Support — L1 · Automated
- [ ] 2.17 Ensure IAM instance roles are used for AWS resource access from instances — L2 · Automated
- [ ] 2.18 Ensure that all expired SSL/TLS certificates stored in AWS IAM are removed — L1 · Automated
- [ ] 2.19 Ensure that IAM External Access Analyzer is enabled for all regions — L1 · Automated
- [ ] 2.20 Ensure IAM users are managed centrally via identity federation or AWS Organizations for multi-account environments — L2 · Manual
- [ ] 2.21 Ensure access to AWSCloudShellFullAccess is restricted — L1 · Manual

### 3 Storage

#### 3.1 Simple Storage Service (S3)

- [ ] 3.1.1 Ensure S3 Bucket Policy is set to deny HTTP requests — L2 · Automated
- [ ] 3.1.2 Ensure MFA Delete is enabled on S3 buckets — L2 · Manual
- [ ] 3.1.3 Ensure all data in Amazon S3 has been discovered, classified, and secured when necessary — L2 · Manual
- [ ] 3.1.4 Ensure that S3 is configured with 'Block Public Access' enabled — L1 · Automated

#### 3.2 Relational Database Service (RDS)

- [ ] 3.2.1 Ensure that encryption-at-rest is enabled for RDS instances — L1 · Automated
- [ ] 3.2.2 Ensure the Auto Minor Version Upgrade feature is enabled for RDS instances — L1 · Automated
- [ ] 3.2.3 Ensure that RDS instances are not publicly accessible — L1 · Automated
- [ ] 3.2.4 Ensure Multi-AZ deployments are used for enhanced availability in Amazon RDS — L1 · Manual

#### 3.3 Elastic File System (EFS)

- [ ] 3.3.1 Ensure that encryption is enabled for EFS file systems — L1 · Automated

### 4 Logging

- [ ] 4.1 Ensure CloudTrail is enabled in all regions — L1 · Manual
- [ ] 4.2 Ensure CloudTrail log file validation is enabled — L2 · Automated
- [ ] 4.3 Ensure AWS Config is enabled in all regions — L2 · Automated
- [ ] 4.4 Ensure that server access logging is enabled on the CloudTrail S3 bucket — L1 · Manual
- [ ] 4.5 Ensure CloudTrail logs are encrypted at rest using KMS CMKs — L2 · Automated
- [ ] 4.6 Ensure rotation for customer-created symmetric CMKs is enabled — L2 · Automated
- [ ] 4.7 Ensure VPC flow logging is enabled in all VPCs — L2 · Automated
- [ ] 4.8 Ensure that object-level logging for write events is enabled for S3 buckets — L2 · Automated
- [ ] 4.9 Ensure that object-level logging for read events is enabled for S3 buckets — L2 · Automated

### 5 Monitoring

- [ ] 5.1 Ensure unauthorized API calls are monitored — L2 · Manual
- [ ] 5.2 Ensure management console sign-in without MFA is monitored — L1 · Manual
- [ ] 5.3 Ensure usage of the 'root' account is monitored — L1 · Manual
- [ ] 5.4 Ensure IAM policy changes are monitored — L1 · Manual
- [ ] 5.5 Ensure CloudTrail configuration changes are monitored — L1 · Manual
- [ ] 5.6 Ensure AWS Management Console authentication failures are monitored — L2 · Manual
- [ ] 5.7 Ensure disabling or scheduled deletion of customer created CMKs is monitored — L2 · Manual
- [ ] 5.8 Ensure S3 bucket policy changes are monitored — L1 · Manual
- [ ] 5.9 Ensure AWS Config configuration changes are monitored — L2 · Manual
- [ ] 5.10 Ensure security group changes are monitored — L2 · Manual
- [ ] 5.11 Ensure Network Access Control List (NACL) changes are monitored — L2 · Manual
- [ ] 5.12 Ensure changes to network gateways are monitored — L1 · Manual
- [ ] 5.13 Ensure route table changes are monitored — L1 · Manual
- [ ] 5.14 Ensure VPC changes are monitored — L1 · Manual
- [ ] 5.15 Ensure AWS Organizations changes are monitored — L1 · Manual
- [ ] 5.16 Ensure AWS Security Hub is enabled — L2 · Automated

### 6 Networking

#### 6.1 Elastic Compute Cloud (EC2)

- [ ] 6.1.1 Ensure EBS volume encryption is enabled in all regions — L1 · Automated
- [ ] 6.1.2 Ensure CIFS access is restricted to trusted networks to prevent unauthorized access — L1 · Automated
- [ ] 6.2 Ensure no Network ACLs allow ingress from 0.0.0.0/0 to remote server administration ports — L1 · Automated
- [ ] 6.3 Ensure no security groups allow ingress from 0.0.0.0/0 to remote server administration ports — L1 · Automated
- [ ] 6.4 Ensure no security groups allow ingress from ::/0 to remote server administration ports — L1 · Automated
- [ ] 6.5 Ensure the default security group of every VPC restricts all traffic — L2 · Automated
- [ ] 6.6 Ensure routing tables for VPC peering are "least access" — L2 · Manual
- [ ] 6.7 Ensure that the EC2 Metadata Service only allows IMDSv2 — L1 · Automated

## Source

CIS Amazon Web Services Foundations Benchmark v6.0.0 (09-23-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[cloud-pentesting/aws-pentesting/attacks-and-methodology/aws-pentest-methodology]]
- [[cloud-pentesting/aws-pentesting/tools/prowler]]
- [[cloud-pentesting/aws-pentesting/tools/cloudsplaining]]
- [[cloud-pentesting/aws-pentesting/aws-environments/identity-and-access-management]]
- [[cloud-pentesting/aws-pentesting/s3-buckets/s3-bucket-misconfiguration]]
- [[cloud-pentesting/aws-pentesting/attacks-and-methodology/exploiting-aws-misconfigurations]]
