---
title: cis-github
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/web, source/cis]
description: "CIS GitHub Benchmark v1.2.0 checklist: source code, build pipelines, dependencies, artifacts, with levels."
source_pdf: CIS_GitHub_Benchmark_v1.2.0_PDF.pdf
---

# CIS GitHub Benchmark v1.2.0 (02-18-2026)

## Overview

- **Product:** GitHub (organizations and repositories; software supply chain)
- **Benchmark version:** v1.2.0 (2026-02-18)
- **Profiles:** Level 1 (essential supply-chain hygiene) and Level 2 (stricter controls for higher-risk environments).
- **Recommendations:** 120 total (2 Automated, 118 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Source Code | 50 |
| 2 Build Pipelines | 33 |
| 3 Dependencies | 12 |
| 4 Artifacts | 14 |
| 5 Deployment | 11 |

## Lab relevance

- **Branch protection (1.1.3, 1.1.14, 1.1.16, 1.1.17, 1.1.20):** required reviews, enforce for administrators, deny force pushes and branch deletion, protect the default branch. Mirror the same rules in Gitea branch protection.
- **Signed commits and checks (1.1.9, 1.1.12):** require passing checks before merge and signed commits (L2); ties in with local GPG/SSH signing keys.
- **MFA and membership (1.3.4, 1.3.5, 1.3.1, 1.3.3):** require MFA for the organisation and contributors, prune inactive users, keep the administrator count minimal.
- **Secret scanning (1.5.1, 5.1.3, 2.1.7):** scanners for sensitive data in code and deployment config, and minimal-scope build secrets (GitHub push protection and secret scanning cover this).
- **Third-party apps and webhooks (1.4.1-1.4.4):** admin approval and least privilege for GitHub Apps/OAuth apps, review stale apps, use webhook secrets.
- **Dependencies and CI (1.5.2-1.5.5, 2.1.x, 2.2.x):** Dependabot/code scanning for vulnerable packages and pipeline files, single-use ephemeral runners, limited build-environment access.
- **Repository hygiene (1.2.1-1.2.7):** SECURITY.md on public repos, limit repo creation and deletion, review forks, visibility changes and inactive repos.

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Source Code

#### 1.1 Code Changes

- [ ] 1.1.1 Ensure any changes to code are tracked in a version control platform — L1 · Manual
- [ ] 1.1.2 Ensure any change to code can be traced back to its associated task — L1 · Manual
- [ ] 1.1.3 Ensure any change to code receives approval of two strongly authenticated users — L1 · Automated
- [ ] 1.1.4 Ensure previous approvals are dismissed when updates are introduced to a code change proposal — L1 · Manual
- [ ] 1.1.5 Ensure there are restrictions on who can dismiss code change reviews — L1 · Manual
- [ ] 1.1.6 Ensure code owners are set for extra sensitive code or configuration — L1 · Manual
- [ ] 1.1.7 Ensure code owner's review is required when a change affects owned code — L1 · Manual
- [ ] 1.1.8 Ensure inactive branches are periodically reviewed and removed — L1 · Manual
- [ ] 1.1.9 Ensure all checks have passed before merging new code — L1 · Manual
- [ ] 1.1.10 Ensure open Git branches are up to date before they can be merged into code base — L1 · Manual
- [ ] 1.1.11 Ensure all open comments are resolved before allowing code change merging — L2 · Manual
- [ ] 1.1.12 Ensure verification of signed commits for new changes before merging — L2 · Manual
- [ ] 1.1.13 Ensure linear history is required — L2 · Manual
- [ ] 1.1.14 Ensure branch protection rules are enforced for administrators — L1 · Manual
- [ ] 1.1.15 Ensure pushing or merging of new code is restricted to specific individuals or teams — L2 · Manual
- [ ] 1.1.16 Ensure force push code to branches is denied — L1 · Manual
- [ ] 1.1.17 Ensure branch deletions are denied — L1 · Manual
- [ ] 1.1.18 Ensure any merging of code is automatically scanned for risks — L1 · Manual
- [ ] 1.1.19 Ensure any changes to branch protection rules are audited — L1 · Manual
- [ ] 1.1.20 Ensure branch protection is enforced on the default branch — L1 · Manual

#### 1.2 Repository Management

- [ ] 1.2.1 Ensure all public repositories contain a SECURITY.md file — L1 · Manual
- [ ] 1.2.2 Ensure repository creation is limited to specific members — L1 · Manual
- [ ] 1.2.3 Ensure repository deletion is limited to specific users — L1 · Manual
- [ ] 1.2.4 Ensure issue deletion is limited to specific users — L1 · Manual
- [ ] 1.2.5 Ensure all copies (forks) of code are tracked and accounted for — L1 · Manual
- [ ] 1.2.6 Ensure all code projects are tracked for changes in visibility status — L1 · Manual
- [ ] 1.2.7 Ensure inactive repositories are reviewed and archived periodically — L1 · Manual

#### 1.3 Contribution Access

- [ ] 1.3.1 Ensure inactive users are reviewed and removed periodically — L2 · Manual
- [ ] 1.3.2 Ensure team creation is limited to specific members — L1 · Manual
- [ ] 1.3.3 Ensure minimum number of administrators are set for the organization — L1 · Manual
- [ ] 1.3.4 Ensure Multi-Factor Authentication (MFA) is required for contributors of new code — L2 · Manual
- [ ] 1.3.5 Ensure the organization is requiring members to use Multi-Factor Authentication (MFA) — L2 · Manual
- [ ] 1.3.6 Ensure new members are required to be invited using company-approved email — L2 · Manual
- [ ] 1.3.7 Ensure two administrators are set for each repository — L2 · Manual
- [ ] 1.3.8 Ensure strict base permissions are set for repositories — L1 · Manual
- [ ] 1.3.9 Ensure an organization’s identity is confirmed with a “Verified” badge — L2 · Manual
- [ ] 1.3.10 Ensure Source Code Management (SCM) email notifications are restricted to verified domains — L2 · Manual
- [ ] 1.3.11 Ensure an organization provides SSH certificates — L2 · Manual
- [ ] 1.3.12 Ensure Git access is limited based on IP addresses — L2 · Manual
- [ ] 1.3.13 Ensure anomalous code behavior is tracked — L1 · Manual

#### 1.4 Third-Party

- [ ] 1.4.1 Ensure administrator approval is required for every installed application — L1 · Manual
- [ ] 1.4.2 Ensure stale applications are reviewed and inactive ones are removed — L1 · Manual
- [ ] 1.4.3 Ensure the access granted to each installed application is limited to the least privilege needed — L1 · Manual
- [ ] 1.4.4 Ensure only secured webhooks are used — L1 · Manual

#### 1.5 Code Risks

- [ ] 1.5.1 Ensure scanners are in place to identify and prevent sensitive data in code — L2 · Manual
- [ ] 1.5.2 Ensure scanners are in place to secure Continuous Integration (CI) pipeline instructions — L2 · Manual
- [ ] 1.5.3 Ensure scanners are in place to secure Infrastructure as Code (IaC) instructions — L2 · Manual
- [ ] 1.5.4 Ensure scanners are in place for code vulnerabilities — L2 · Manual
- [ ] 1.5.5 Ensure scanners are in place for open-source vulnerabilities in used packages — L2 · Manual
- [ ] 1.5.6 Ensure scanners are in place for open-source license issues in used packages — L2 · Manual

### 2 Build Pipelines

#### 2.1 Build Environment

- [ ] 2.1.1 Ensure each pipeline has a single responsibility — L2 · Manual
- [ ] 2.1.2 Ensure all aspects of the pipeline infrastructure and configuration are immutable — L1 · Manual
- [ ] 2.1.3 Ensure the build environment is logged — L1 · Manual
- [ ] 2.1.4 Ensure the creation of the build environment is automated — L1 · Manual
- [ ] 2.1.5 Ensure access to build environments is limited — L1 · Manual
- [ ] 2.1.6 Ensure users must authenticate to access the build environment — L1 · Manual
- [ ] 2.1.7 Ensure build secrets are limited to the minimal necessary scope — L2 · Manual
- [ ] 2.1.8 Ensure the build infrastructure is automatically scanned for vulnerabilities — L1 · Manual
- [ ] 2.1.9 Ensure default passwords are not used — L1 · Manual
- [ ] 2.1.10 Ensure webhooks of the build environment are secured — L1 · Manual
- [ ] 2.1.11 Ensure minimum number of administrators are set for the build environment — L1 · Manual

#### 2.2 Build Worker

- [ ] 2.2.1 Ensure build workers are single-used — L1 · Manual
- [ ] 2.2.2 Ensure build worker environments and commands are passed and not pulled — L1 · Manual
- [ ] 2.2.3 Ensure the duties of each build worker are segregated — L1 · Manual
- [ ] 2.2.4 Ensure build workers have minimal network connectivity — L1 · Manual
- [ ] 2.2.5 Ensure run-time security is enforced for build workers — L1 · Manual
- [ ] 2.2.6 Ensure build workers are automatically scanned for vulnerabilities — L1 · Manual
- [ ] 2.2.7 Ensure build workers' deployment configuration is stored in a version control platform — L1 · Manual
- [ ] 2.2.8 Ensure resource consumption of build workers is monitored — L1 · Manual

#### 2.3 Pipeline Instructions

- [ ] 2.3.1 Ensure all build steps are defined as code — L1 · Manual
- [ ] 2.3.2 Ensure steps have clearly defined build stage input and output — L1 · Manual
- [ ] 2.3.3 Ensure output is written to a separate, secured storage repository — L1 · Manual
- [ ] 2.3.4 Ensure changes to pipeline files are tracked and reviewed — L1 · Manual
- [ ] 2.3.5 Ensure access to build process triggering is minimized — L1 · Manual
- [ ] 2.3.6 Ensure pipelines are automatically scanned for misconfigurations — L1 · Manual
- [ ] 2.3.7 Ensure pipelines are automatically scanned for vulnerabilities — L1 · Manual
- [ ] 2.3.8 Ensure scanners are in place to identify and prevent sensitive data in pipeline files — L2 · Automated

#### 2.4 Pipeline Integrity

- [ ] 2.4.1 Ensure all artifacts on all releases are signed — L1 · Manual
- [ ] 2.4.2 Ensure all external dependencies used in the build process are locked — L1 · Manual
- [ ] 2.4.3 Ensure dependencies are validated before being used — L1 · Manual
- [ ] 2.4.4 Ensure the build pipeline creates reproducible artifacts — L1 · Manual
- [ ] 2.4.5 Ensure pipeline steps produce a Software Bill of Materials (SBOM) — L1 · Manual
- [ ] 2.4.6 Ensure pipeline steps sign the Software Bill of Materials (SBOM) produced — L1 · Manual

### 3 Dependencies

#### 3.1 Third-Party Packages

- [ ] 3.1.1 Ensure third-party artifacts and open-source libraries are verified — L1 · Manual
- [ ] 3.1.2 Ensure Software Bill of Materials (SBOM) is required from all third-party suppliers — L1 · Manual
- [ ] 3.1.3 Ensure signed metadata of the build process is required and verified — L1 · Manual
- [ ] 3.1.4 Ensure dependencies are monitored between open-source components — L1 · Manual
- [ ] 3.1.5 Ensure trusted package managers and repositories are defined and prioritized — L1 · Manual
- [ ] 3.1.6 Ensure a signed Software Bill of Materials (SBOM) of the code is supplied — L1 · Manual
- [ ] 3.1.7 Ensure dependencies are pinned to a specific, verified version — L1 · Manual
- [ ] 3.1.8 Ensure all packages used are more than 60 days old — L2 · Manual

#### 3.2 Validate Packages

- [ ] 3.2.1 Ensure an organization-wide dependency usage policy is enforced — L1 · Manual
- [ ] 3.2.2 Ensure packages are automatically scanned for known vulnerabilities — L1 · Manual
- [ ] 3.2.3 Ensure packages are automatically scanned for license implications — L1 · Manual
- [ ] 3.2.4 Ensure packages are automatically scanned for ownership change — L1 · Manual

### 4 Artifacts

#### 4.1 Verification

- [ ] 4.1.1 Ensure all artifacts are signed by the build pipeline itself — L2 · Manual
- [ ] 4.1.2 Ensure artifacts are encrypted before distribution — L2 · Manual
- [ ] 4.1.3 Ensure only authorized platforms have decryption capabilities of artifacts — L2 · Manual

#### 4.2 Access to Artifacts

- [ ] 4.2.1 Ensure the authority to certify artifacts is limited — L1 · Manual
- [ ] 4.2.2 Ensure number of permitted users who may upload new artifacts is minimized — L1 · Manual
- [ ] 4.2.3 Ensure user access to the package registry utilizes Multi-Factor Authentication (MFA) — L2 · Manual
- [ ] 4.2.4 Ensure user management of the package registry is not local — L1 · Manual
- [ ] 4.2.5 Ensure anonymous access to artifacts is revoked — L1 · Manual
- [ ] 4.2.6 Ensure minimum number of administrators are set for the package registry — L1 · Manual

#### 4.3 Package Registries

- [ ] 4.3.1 Ensure all signed artifacts are validated upon uploading the package registry — L1 · Manual
- [ ] 4.3.2 Ensure all versions of an existing artifact have their signatures validated — L1 · Manual
- [ ] 4.3.3 Ensure changes in package registry configuration are audited — L1 · Manual
- [ ] 4.3.4 Ensure webhooks of the repository are secured — L1 · Manual

#### 4.4 Origin Traceability

- [ ] 4.4.1 Ensure artifacts contain information about their origin — L1 · Manual

### 5 Deployment

#### 5.1 Deployment Configuration

- [ ] 5.1.1 Ensure deployment configuration files are separated from source code — L2 · Manual
- [ ] 5.1.2 Ensure changes in deployment configuration are audited — L1 · Manual
- [ ] 5.1.3 Ensure scanners are in place to identify and prevent sensitive data in deployment configuration — L1 · Manual
- [ ] 5.1.4 Limit access to deployment configurations — L1 · Manual
- [ ] 5.1.5 Scan Infrastructure as Code (IaC) — L2 · Manual
- [ ] 5.1.6 Ensure deployment configuration manifests are verified — L1 · Manual
- [ ] 5.1.7 Ensure deployment configuration manifests are pinned to a specific, verified version — L1 · Manual

#### 5.2 Deployment Environment

- [ ] 5.2.1 Ensure deployments are automated — L1 · Manual
- [ ] 5.2.2 Ensure the deployment environment is reproducible — L1 · Manual
- [ ] 5.2.3 Ensure access to production environment is limited — L1 · Manual
- [ ] 5.2.4 Ensure default passwords are not used — L1 · Manual

## Source

CIS GitHub Benchmark v1.2.0 (02-18-2026), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[cloud-pentesting/aws-pentesting/initial-access/leaked-secrets]]
- [[vulnerability-research/code-review]]
- [[owasp-top-10/web/a06-2021-vulnerable-and-outdated-components]]
- [[owasp-top-10/web/a08-2021-software-and-data-integrity-failures]]
- [[miscellaneous/gpg]]
- [[miscellaneous/ssh-commands]]
