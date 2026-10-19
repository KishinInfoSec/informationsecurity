---
title: cis-microsoft-365-foundations
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/m365, source/cis]
description: "CIS Microsoft 365 Foundations Benchmark v6.0.1 checklist: Entra ID, Exchange, SharePoint, Teams, OneDrive, with levels."
source_pdf: CIS_Microsoft_365_Foundations_Benchmark_v6.0.1.pdf
---

# CIS Microsoft 365 Foundations Benchmark v6.0.1 (02-26-2026)

## Overview

- **Product:** Microsoft 365 tenant foundations (Entra ID, Exchange Online, SharePoint/OneDrive, Teams, Purview, Intune, Fabric/Power BI)
- **Benchmark version:** v6.0.1, published 2026-02-26 (v6.0.0 released 2025-10-31)
- **Recommendations:** 140 total — 97 Level 1, 43 Level 2; 117 Automated, 23 Manual
- **Assessment:** via CIS-CAT Pro Assessor, certified third-party tooling, or manual audit procedures; both Automated and Manual recommendations are in scope for audits
- **CIS Controls mapping:** the benchmark as a whole addresses (v8) 4.1 "Establish and Maintain a Secure Configuration Process" and (v7) 5.1 "Establish Secure Configurations"; individual recommendations are not mapped to these safeguards

### Section outline

| Section | Recommendations |
|---|---|
| 1 Microsoft 365 admin center | 15 |
| 2 Microsoft 365 Defender | 20 |
| 3 Microsoft Purview | 4 |
| 4 Microsoft Intune admin center | 2 |
| 5 Microsoft Entra admin center | 45 |
| 6 Exchange admin center | 12 |
| 7 SharePoint admin center | 13 |
| 8 Microsoft Teams admin center | 17 |
| 9 Microsoft Fabric | 12 |

## Profiles

This benchmark defines four profiles, combining license tier (E3 vs E5) with hardening level:

- **E3 Level 1** — applies to M365 E3 deployments; items that are practical and prudent, provide a clear security benefit, and do not inhibit the utility of the technology beyond acceptable means.
- **E3 Level 2** — extends "E3 Level 1"; items intended for environments where security is paramount, act as defense in depth, and may negatively inhibit utility or performance. **Level 2 is never a standalone profile.**
- **E5 Level 1** — extends "E3 Level 1" for M365 E5 deployments with the same practical/prudent criteria (covers E5-only features such as Customer Lockbox, PIM, DLP for Teams).
- **E5 Level 2** — extends both "E3 Level 1" and "E5 Level 1", effectively including all E3 and E5 recommendations at both levels.

Each recommendation lists its Profile Applicability (e.g. "E3 Level 1, E5 Level 1"); E5-only items appear solely under E5 profiles.

## Recommendation checklist

Condensed, high-signal selections per section; titles and states are the benchmark's own. See the official benchmark for full rationale, audit, and remediation procedures.

### 1 Microsoft 365 admin center

#### 1.1 Users

- [ ] 1.1.1 (L1) Ensure Administrative accounts are cloud-only — admin accounts must not be On-premises sync enabled and should have no applications assigned (no email/Teams/SharePoint access). Audit: filter All users in entra.microsoft.com by "On-premises sync enabled = Yes" and verify no privileged-role users appear; or Graph script checking `OnPremisesSyncEnabled` for members of *Administrator* roles and Global Reader.
- [ ] 1.1.2 (L1) Ensure two emergency access accounts have been defined (Manual) — "break glass" accounts not assigned to a specific user, excluded from at least all Conditional Access rules, protected by password entropy/length or FIDO2 security keys.
- [ ] 1.1.3 (L1) Ensure that between two and four global admins are designated.
- [ ] 1.1.4 (L1) Ensure administrative accounts use licenses with a reduced application footprint.

#### 1.2 Teams & groups

- [ ] 1.2.1 (L2) Ensure that only organizationally managed/approved public groups exist.
- [ ] 1.2.2 (L1) Ensure sign-in to shared mailboxes is blocked.

#### 1.3 Settings

- [ ] 1.3.1 (L1) Ensure the 'Password expiration policy' is set to 'Set passwords to never expire (recommended)'.
- [ ] 1.3.2 (L2) Ensure 'Idle session timeout' is set to '3 hours (or less)' for unmanaged devices.
- [ ] 1.3.4–1.3.5 (L1) User owned apps/services restricted; internal phishing protection for Forms enabled.
- [ ] 1.3.6 (L2) Ensure the customer lockbox feature is enabled (E5) — requires approval for all Microsoft support data-access requests; audit via admin.microsoft.com > Settings > Org settings > Security & privacy > Customer lockbox, or Secure Score portal.
- [ ] 1.3.7 (L2) Ensure 'third-party storage services' are restricted in 'Microsoft 365 on the web'.
- [ ] 1.3.9 (L1) Ensure shared bookings pages are restricted to select users.

### 2 Microsoft 365 Defender

#### 2.1 Email & collaboration

- [ ] 2.1.1 (L2) Ensure Safe Links for Office Applications is Enabled.
- [ ] 2.1.2 (L1) Ensure the Common Attachment Types Filter is enabled — block known/custom malicious file types on the anti-malware (Default) policy. Audit: `Get-MalwareFilterPolicy -Identity Default | Select-Object EnableFileFilter` → `True`.
- [ ] 2.1.4–2.1.5 (L2) Safe Attachments policy enabled, including for SharePoint, OneDrive, and Microsoft Teams.
- [ ] 2.1.6 (L1) Ensure Exchange Online Spam Policies are set to notify administrators.
- [ ] 2.1.7 (L2) Ensure that an anti-phishing policy has been created.
- [ ] 2.1.8 (L1) Ensure that SPF records are published for all Exchange Domains.
- [ ] 2.1.9 (L1) Ensure that DKIM is enabled for all Exchange Online Domains — "Sign messages for this domain with DKIM signatures" Enabled, Status "Signing DKIM signatures" (Defender > Email & collaboration > Policies & rules > Threat policies > Email authentication settings > DKIM).
- [ ] 2.1.10 (L1) Ensure DMARC Records for all Exchange Online domains are published — per domain, `Resolve-DnsName _dmarc.[domain] txt` must return at minimum `v=DMARC1; (p=quarantine OR p=reject), pct=100, rua=mailto:<reporting address> and ruf=mailto:<reporting address>`; leaving `p=none` risks failed action against spear phishing.
- [ ] 2.1.11 (L2) Ensure comprehensive attachment filtering is applied.
- [ ] 2.1.12–2.1.14 (L1) Connection filter: IP allow list not used, safe list off; inbound anti-spam policies contain no allowed domains.
- [ ] 2.1.15 (L1) Ensure outbound anti-spam message limits are in place.

#### 2.2 Cloud apps / 2.4 System

(2.3 Audit is intentionally blank, kept only for structural consistency.)

- [ ] 2.2.1 (L1) Ensure emergency access account activity is monitored (Manual).
- [ ] 2.4.1 (L1) Ensure Priority account protection is enabled and configured.
- [ ] 2.4.2 (L1) Ensure Priority accounts have 'Strict protection' presets applied.
- [ ] 2.4.3 (L2) Ensure Microsoft Defender for Cloud Apps is enabled and configured (Manual).
- [ ] 2.4.4 (L1) Ensure Zero-hour auto purge for Microsoft Teams is on.

### 3 Microsoft Purview

- [ ] 3.1.1 (L1) Ensure Microsoft 365 audit log search is Enabled — unified audit log records user/admin activity, retained 180 days by default. Audit: `Get-AdminAuditLogConfig | Select-Object UnifiedAuditLogIngestionEnabled` → `True` (note: import Security & Compliance module before Exchange Online PowerShell or the value always displays False). Remediate: `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`.
- [ ] 3.2.1 (L1) Ensure DLP policies are enabled — create a Purview DLP policy specific to the data types the organization protects.
- [ ] 3.2.2 (L1) Ensure DLP policies are enabled for Microsoft Teams (E5) — default Teams DLP rule auto-applied to all conversations/channels; by default checks the pre-defined Credit Card Number sensitive info type.
- [ ] 3.3.1 (L1) Ensure Information Protection sensitivity label policies are published.

### 4 Microsoft Intune admin center

- [ ] 4.1 (L2) Ensure devices without a compliance policy are marked 'not compliant'.
- [ ] 4.2 (L2) Ensure device enrollment for personally owned devices is blocked by default.

### 5 Microsoft Entra admin center

#### 5.1 Entra ID

- [ ] 5.1.2.1 (L1) Ensure 'Per-user MFA' is disabled (superseded by Conditional Access).
- [ ] 5.1.2.2 (L2) Ensure third party integrated applications are not allowed.
- [ ] 5.1.2.3 (L1) Ensure 'Restrict non-admin users from creating tenants' is set to 'Yes'.
- [ ] 5.1.2.4 (L1) Ensure access to the Entra admin center is restricted (Manual).
- [ ] 5.1.3.1–5.1.3.2 (L1) Dynamic group for guest users created; users cannot create security groups.
- [ ] 5.1.4.2–5.1.4.5 Entra join hardening: max devices per user limited (L1); GA role not added as local administrator (L1); local administrator assignment limited (L1); Local Administrator Password Solution enabled (L1).
- [ ] 5.1.4.6 (L2) Ensure users are restricted from recovering BitLocker keys.
- [ ] 5.1.5.1 (L2) Ensure user consent to apps accessing company data on their behalf is not allowed.
- [ ] 5.1.5.2 (L1) Ensure the admin consent workflow is enabled — "Users can request admin consent to apps they are unable to consent to" = Yes. Audit: `Get-MgPolicyAdminConsentRequestPolicy | fl IsEnabled,NotifyReviewers,RemindersEnabled` → `IsEnabled` = `True`. Reviewers must hold Global Admin, Cloud Application Admin, or Application Admin.
- [ ] 5.1.6.1 (L2) Ensure that collaboration invitations are sent to allowed domains only.
- [ ] 5.1.6.2 (L1) Ensure that guest user access is restricted.
- [ ] 5.1.6.3 (L2) Ensure guest user invitations are limited to the Guest Inviter role.
- [ ] 5.1.8.1 (L1) Ensure that password hash sync is enabled for hybrid deployments (Manual).

#### 5.2 ID Protection

- [ ] 5.2.2.1 (L1) Ensure multifactor authentication is enabled for all users in administrative roles — Conditional Access policy targeting Directory roles, All resources, Grant Access requiring MFA/authentication strength; Enable policy = On. Break-glass accounts excluded from all CA policies with documented annual reviews. Minimum roles include Application, Authentication, Billing, Cloud application, Conditional Access administrators.
- [ ] 5.2.2.2 (L1) Ensure multifactor authentication is enabled for all users.
- [ ] 5.2.2.3 (L1) Enable Conditional Access policies to block legacy authentication — legacy protocols (Authenticated SMTP, Autodiscover, EAS, EWS, IMAP4, MAPI/HTTP, OAB, Outlook Anywhere, POP3, and others) do not support MFA and are commonly abused; block them via Conditional Access.
- [ ] 5.2.2.4 (L1) Ensure Sign-in frequency is enabled and browser sessions are not persistent for Administrative users.
- [ ] 5.2.2.5 (L2) Ensure 'Phishing-resistant MFA strength' is required for Administrators.
- [ ] 5.2.2.6–5.2.2.8 Identity Protection risk policies: user risk and sign-in risk policies enabled (L1); medium/high sign-in risk blocked (L2).
- [ ] 5.2.2.9–5.2.2.12 Managed device required for authentication and security-info registration (L1); Intune Enrollment sign-in frequency 'Every time' (L1); device code sign-in flow blocked (L1).
- [ ] 5.2.3.1 (L1) Ensure Microsoft Authenticator is configured to protect against MFA fatigue (number matching).
- [ ] 5.2.3.2–5.2.3.3 (L1) Custom banned passwords lists used; password protection enabled for on-prem Active Directory.
- [ ] 5.2.3.4–5.2.3.6 (L1) All member users 'MFA capable'; weak authentication methods disabled; system-preferred MFA enabled.
- [ ] 5.2.3.7 (L2) Ensure the email OTP authentication method is disabled.
- [ ] 5.2.4.1 (L1) Ensure 'Self service password reset enabled' is set to 'All' (Manual).

#### 5.3 ID Governance

- [ ] 5.3.1 (L2) Ensure 'Privileged Identity Management' is used to manage roles (E5).
- [ ] 5.3.2–5.3.3 (L1) 'Access reviews' configured for Guest Users and for privileged roles.
- [ ] 5.3.4 (L1) Ensure approval is required for Global Administrator role activation (E5) — PIM > Microsoft Entra Roles > Roles > Global Administrator > Role settings: "Require approval to activate" = Yes, with at least two approvers; break-glass account needed to avoid lockouts. Approvers need not hold the same role.
- [ ] 5.3.5 (L1) Ensure approval is required for Privileged Role Administrator activation (E5).

### 6 Exchange admin center

- [ ] 6.1.1 (L1) Ensure 'AuditDisabled' organizationally is set to 'False' — mailbox auditing on by default; with advanced auditing (E5) logs are limited to 90 days otherwise.
- [ ] 6.1.2–6.1.3 (L1) Mailbox audit actions configured; 'AuditBypassEnabled' not enabled on mailboxes.
- [ ] 6.2.1 (L1) Ensure all forms of mail forwarding are blocked and/or disabled — covers inbox-rule forwarding, OOF-rule forwarding, OWA ForwardingSmtpAddress, admin ForwardingAddress, and Power Automate/Flow forwarding. Two-step audit: (1) `Get-TransportRule | Where-Object {$_.RedirectMessageTo -ne $null} | ft Name,RedirectMessageTo` — no external domains; (2) Anti-spam outbound policy (default): Automatic forwarding = "Off - Forwarding is disabled".
- [ ] 6.2.2 (L1) Ensure mail transport rules do not whitelist specific domains.
- [ ] 6.2.3 (L1) Ensure email from external senders is identified.
- [ ] 6.3.1 (L2) Ensure users installing Outlook add-ins is not allowed.
- [ ] 6.5.1–6.5.3 Modern authentication for Exchange Online enabled (L1); MailTips enabled for end users (L1); additional storage providers restricted in Outlook on the web (L2).
- [ ] 6.5.4 (L1) Ensure SMTP AUTH is disabled — "Turn off SMTP AUTH protocol for your organization" (checked). Audit: `Get-TransportConfig | Format-List SmtpClientAuthenticationDisabled` → `True`. Supports least functionality and backstops Conditional Access legacy-auth blocks; per-mailbox overrides exist for special cases.
- [ ] 6.5.5 (L2) Ensure Direct Send submissions are rejected.

### 7 SharePoint admin center (incl. OneDrive)

- [ ] 7.2.1–7.2.2 (L1) Modern authentication for SharePoint applications required; SharePoint and OneDrive integration with Azure AD B2B enabled.
- [ ] 7.2.3 (L1) Ensure external content sharing is restricted — recommended state "New and existing guests" or less permissive; audit `Get-SPOTenant | fl SharingCapability` (compliant: ExternalUserSharingOnly or stricter). Guests get a directory identity that can be governed by groups and Conditional Access.
- [ ] 7.2.4–7.2.6 (L2) OneDrive content sharing restricted; SharePoint guest users cannot share items they don't own; SharePoint external sharing restricted.
- [ ] 7.2.7 (L1) Ensure link sharing is restricted in SharePoint and OneDrive — default link type: Specific people or Only people in your organization. Audit: `Get-SPOTenant | fl DefaultSharingLinkType` → `Direct` or `Internal` (more restrictive). Remediate: `Set-SPOTenant -DefaultSharingLinkType Direct` (or `Internal`).
- [ ] 7.2.8 (L2) Ensure external sharing is restricted by security group (Manual).
- [ ] 7.2.9–7.2.11 (L1) Guest access to a site or OneDrive expires automatically; reauthentication with verification code restricted; SharePoint default sharing link permission set.
- [ ] 7.3.1–7.3.2 (L2) SharePoint infected files disallowed for download; OneDrive sync restricted for unmanaged devices.

### 8 Microsoft Teams admin center

- [ ] 8.1.1 (L2) Ensure external file sharing in Teams is enabled for only approved cloud storage services.
- [ ] 8.1.2 (L1) Ensure users can't send emails to a channel email address.
- [ ] 8.2.1 (L2) Ensure external domains are restricted in the Teams admin center.
- [ ] 8.2.2–8.2.4 (L1) Communication with unmanaged Teams users disabled; external Teams users cannot initiate conversations; no communication with accounts in trial Teams tenants.
- [ ] 8.4.1 (L1) Ensure app permission policies are configured (Manual).
- [ ] 8.5.1 (L2) Ensure anonymous users can't join a meeting — "Anonymous users can join a meeting unverified" = Off. Audit: `Get-CsTeamsMeetingPolicy -Identity Global | fl AllowAnonymousUsersToJoinMeeting` → `False`. Organizations not normally at Level 2 but handling sensitive information may still want this.
- [ ] 8.5.2 (L1) Ensure anonymous users and dial-in callers can't start a meeting.
- [ ] 8.5.3 (L1) Ensure only people in my org can bypass the lobby — recommended "People who were invited" or more restrictive (People in my org, Only organizers and co-organizers); everyone else, including dial-in users, waits in the lobby.
- [ ] 8.5.4–8.5.6 Lobby/presenters: dial-in users can't bypass the lobby (L1); meeting chat excludes anonymous users (L2); only organizers and co-organizers can present (L2).
- [ ] 8.5.7 (L1) Ensure external participants can't give or request control.
- [ ] 8.5.8 (L2) Ensure external meeting chat is off.
- [ ] 8.5.9 (L2) Ensure meeting recording is off by default.
- [ ] 8.6.1 (L1) Ensure users can report security concerns in Teams.

### 9 Microsoft Fabric (Power BI)

Tenant settings audited via the Fabric admin portal (app.powerbi.com/admin-portal) by Fabric Administrator or Global Administrator (Global Reader lacks sufficient permissions); v6.0.1 added an automation script and PowerShell audit procedures for all 9.1 settings (requires PowerShell 7.5 and Az.Accounts).

- [ ] 9.1.1–9.1.3 (L1) Guest/user external access and content restrictions in place.
- [ ] 9.1.4 (L1) Ensure 'Publish to web' is restricted.
- [ ] 9.1.5 (L2) Ensure 'Interact with and share R and Python' visuals is 'Disabled'.
- [ ] 9.1.6 (L1) Ensure 'Allow users to apply sensitivity labels for content' is 'Enabled'.
- [ ] 9.1.7–9.1.8 (L1) Shareable links restricted; enabling of external data sharing restricted.
- [ ] 9.1.9 (L1) Ensure 'Block ResourceKey Authentication' is 'Enabled'.
- [ ] 9.1.10–9.1.11 (L1) Service principal access to APIs restricted; service principals cannot create and use profiles.
- [ ] 9.1.12 (L1) Ensure service principals ability to create workspaces, connections and deployment pipelines is restricted — compliant states: Disabled, or Enabled with Specific security groups defined; prefer Disabled if the feature is unused (setting `ServicePrincipalAccessGlobalAPIs`).

## Audit / remediation conventions

- Console paths in the benchmark target entra.microsoft.com, security.microsoft.com, admin.exchange.microsoft.com, admin.microsoft.com/sharepoint, admin.teams.microsoft.com, purview.microsoft.com, and app.powerbi.com/admin-portal.
- PowerShell modules used across recommendations: Microsoft Graph (`Connect-MgGraph`), Exchange Online (`Connect-ExchangeOnline`), SharePoint Online (`Connect-SPOService`), Teams (`Connect-MicrosoftTeams`).
- CIS recommends running custom or custom-adjacent baselines in Report-only mode first, then enabling once the organization is ready (e.g. Conditional Access deployment pattern in 5.2.2.1).

## Change history (v6.x)

- **v6.0.1 (2026-02-26):** new CIS-CAT Pro Assessor automated content; Fabric 9.1 automation script and PowerShell audit procedures; 5.3.2 audit made backwards compatible with PowerShell 5; title fix for 1.3.9.
- **v6.0.0 (2025-10-31):** added 1.3.9, 2.1.15, 5.1.3.2, 5.1.4.1–5.1.4.6, 5.2.3.7, 6.5.5, 8.2.4, 9.1.12; removed 7.3.3 and 7.3.4 (custom script settings no longer available/automatically disabled by Microsoft).

## Related

- [[grc-frameworks/cis-benchmarks/cis-azure-foundations]]
