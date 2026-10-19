---
title: cis-gke
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/gcp, platform/container, source/cis]
description: "CIS Google Kubernetes Engine (GKE) Benchmark v1.8.0 checklist: control plane, node config, policies, with levels."
source_pdf: "CIS_Google_Kubernetes_Engine_(GKE)_Benchmark_v1.8.0_PDF.pdf"
---
# CIS Google Kubernetes Engine (GKE) Benchmark v1.8.0 (2025-06-26)

## Overview
- Scope: GKE-specific hardening checklist (v1.8.0). Focus on end-user responsibilities (nodes, containers, Pods); GCP manages the control plane (API server, etcd, controllers).
- Profiles: **Level 1** (practical, clear security benefit, minimal utility impact); **Level 2** (extends Level 1, not standalone). Recommendations include profile applicability in the PDF.
- Format: control ID (e.g. 3.1.x, 4.1.x), title, level, automated/manual, audit, remediation. All commands/values quoted as in PDF where present.

## Control Plane Configuration (Section 2/3 context)
- **Control plane exposure**: Prefer private clusters / control plane authorized networks to restrict access to cluster API. Limit IPs that can reach control plane; enforce HTTPS; avoid broadly exposing API.
- **Authentication/authorization model (RBAC)**: GKE maps Google identity to Kubernetes auth. Default groups include `system:unauthenticated`, `system:authenticated`. Exercise caution when binding these to roles (see RBAC section).
- **Shared responsibility**: Google secures control plane; users secure nodes, containers, Pods. Use GKE-managed features (seccomp, COS/COS_CONTAINERD, PSP/PSS-aligned controls, Workload Identity) per PDF guidance.

## Worker Node Configuration (Section 3)
- **Node images**: Use **COS or COS_CONTAINERD** for worker nodes where feasible; hardened, GCP-maintained. Review image choices and lifecycle.
- **Kubelet configuration**: Harden kubelet flags/settings as applicable (e.g. limit anonymous access, protect kubeconfig, set appropriate TLS/authn/z settings). Verify node configs against PDF checklist items (3.x).
- **Node metadata/identity**: Use **Workload Identity** for GKE workloads (avoid legacy node/service account key patterns where possible). Restrict node service account scopes/permissions.
- **OS/boot**: Ensure nodes follow recommended secure configs; avoid running privileged/unsupported node images.

## Networking (Section 5)
- **Network policies**: Enforce Kubernetes NetworkPolicy to restrict intra-cluster traffic by namespace/pods as appropriate for workload segmentation.
- **Ingress/egress**: Restrict egress to required destinations; secure LoadBalancer/Ingress; use private IPs for internal endpoints. Validate cluster network config per PDF.
- **Authorized networks (control plane)**: Restrict which CIDRs can connect to control plane (`--enable-master-authorized-networks` / equivalent console setting).
- **Pod-to-Pod**: Default deny/allow rules by app tier; ensure no unrestricted cross-namespace traffic.

## RBAC & Service Accounts (Section 4.1)
- **Cluster-admin** (4.1.1, L1, Automated): Only use `cluster-admin` where strictly required. Audit bindings: `kubectl get clusterrolebindings -o json | jq ...` and inspect users/groups/SA bound to cluster-admin.
- **Minimize access to secrets** (4.1.2, L1, Automated): Grant `get/watch/list` on `secrets` only to principals needing it. Avoid broad RBAC on secrets.
- **Wildcard use** (4.1.3, L1, Automated): Minimize `*` in `verbs`, `resources`, `apiGroups` in Roles/ClusterRoles. Prefer least-privilege resource/verb sets.
- **Default service accounts** (4.1.4, L1, Automated): Do not actively use `default` SA in namespaces for workloads. Create/use dedicated SAs with minimal IAM and RBAC.
- **SA token mounting** (4.1.5, L1, Automated): Only mount SA tokens where necessary (`automountServiceAccountToken: false` on Pods/ServiceAccounts when not needed). Limit token exposure.
- **Avoid `system:masters`** (4.1.6, L1, Automated): `system:masters` is a superuser group; do not bind users/groups to it.
- **Bind/Impersonate/Escalate** (4.1.7, L1, Automated): Limit `bind`, `impersonate`, `escalate` permissions in cluster; audit roles granting these.
- **Avoid binding to `system:anonymous`** (4.1.8, L1, Automated): No non-default RoleBindings/ClusterRoleBindings to `system:anonymous`.
- **Avoid non-default bindings to `system:unauthenticated`** (4.1.9, L1, Automated): Only default allowed is `system:public-info-viewer` (ClusterRoleBinding). Check with:
  - `kubectl get clusterrolebindings -o json | jq -r ... | grep system:unauthenticated` (expect only default)
- **Avoid non-default bindings to `system:authenticated`** (4.1.10, L1, Automated): Only defaults: `system:basic-user`, `system:discovery`, `system:public-info-viewer`. Treat `system:authenticated` (includes Google/Gmail accounts) with same caution as unauthenticated for broad bindings.

## Pod Security Standards (Section 4.2)
- **Enforce PSS Baseline or stricter** (4.2.1, L1, Manual): Enforce Pod Security Standard **Baseline** profile or stricter for all namespaces (e.g. `kubectl label ns ... pod-security.kubernetes.io/enforce=baseline` or admission controller). Without enforcement, baseline is not guaranteed.
- **Seccomp profile** (4.6.2, L1): Set `seccompProfile.type: RuntimeDefault` in Pod definitions. Kubernetes disables seccomp by default; use `RuntimeDefault` unless a custom localhost profile is required.

## Workload Hardening (Section 4.3–4.6)
- **Non-root containers**: Run containers as non-root users; avoid root; drop unnecessary Linux capabilities; use `readOnlyRootFilesystem` where feasible, `allowPrivilegeEscalation: false`, `runAsNonRoot: true`.
- **Host namespaces/FS**: Avoid hostNetwork, hostPID, hostIPC where not required; do not mount sensitive host paths.
- **Images**: Use trusted, signed images; avoid `:latest`; scan images per org policy. Pull from approved registries.
- **Secrets**: Prefer external secret stores/Workload Identity; avoid embedding secrets in image/env; restrict secret RBAC (4.1.2).

## Logging & Monitoring (Section 4.7)
- **Enable logging/monitoring**: Enable GKE logging and monitoring (Cloud Logging/Monitoring) for control plane + nodes + workloads as applicable. Retain audit logs per policy.
- **Audit events**: Review Kubernetes audit logs for RBAC changes, privilege escalation, suspicious operations. Ensure logs are immutable/exported securely per compliance.

## Remediation Notes
- Prefer automated checks where marked Automated; Manual items require evidence. Use `gcloud`, `kubectl`, GCP Console as indicated in PDF.
- When removing non-default, unsafe bindings, verify they are not operationally required first.
- Follow least privilege and change control; document exceptions with rationale.

## References
- CIS Google Kubernetes Engine (GKE) Benchmark v1.8.0, 2025-06-26 (PDF: `Resources/cis-benchmarks/CIS_Google_Kubernetes_Engine_(GKE)_Benchmark_v1.8.0_PDF.pdf`)
- Related (optional cross-link): [[grc-frameworks/cis-benchmarks/cis-kubernetes]] (canonical Kubernetes benchmark reference where applicable)
