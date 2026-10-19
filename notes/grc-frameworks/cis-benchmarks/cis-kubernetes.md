---
title: cis-kubernetes
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/container, source/cis]
description: "CIS Kubernetes Benchmark v1.11.1 checklist: control plane, etcd, worker nodes and policies, with levels."
source_pdf: CIS Kubernetes Benchmark v1.11.1_PDF.pdf
---

# CIS Kubernetes Benchmark v1.11.1 (04-16-2025)

## Overview

- **Product:** Kubernetes (self-managed control plane and worker nodes)
- **Benchmark version:** v1.11.1 (2025-04-16)
- **Profiles:** Level 1 and Level 2, each split into Master Node and Worker Node profiles. Level 2 adds defence-in-depth items that may affect functionality.
- **Recommendations:** 134 total (65 Automated, 69 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Control Plane Components | 60 |
| 2 etcd | 8 |
| 3 Control Plane Configuration | 5 |
| 4 Worker Nodes | 26 |
| 5 Policies | 35 |

## Lab relevance

- **Applies to k3s only in spirit:** this benchmark assumes kubeadm-style components with separate flags and files. k3s bundles the API server, kubelet and sqlite/etcd into one process and writes config under `/var/lib/rancher/k3s` and `/etc/rancher/k3s`, so file-path items (1.1.x, 4.1.x) need mapping and many flag items are checked via the k3s config instead. Rancher publishes a k3s-specific hardening guide for this reason.
- **API server authN/Z (1.2.1, 1.2.6-1.2.8):** anonymous-auth false, authorization mode not AlwaysAllow and including Node and RBAC.
- **Audit logging (1.2.16-1.2.19, 3.2.1, 3.2.2):** audit log path and retention, plus a minimal audit policy that covers key security events.
- **Secrets at rest (1.2.27, 1.2.28):** encryption-provider config; k3s supports `--secrets-encryption`.
- **Kubelet (4.2.1-4.2.4, 4.2.6, 4.2.14):** anonymous-auth false, authorization not AlwaysAllow, client CA set, readOnlyPort 0, seccomp-default true.
- **RBAC hygiene (5.1.1-5.1.7):** limit cluster-admin, secret access and wildcard roles; stop using default service accounts and avoid mounting tokens unnecessarily.
- **Pod security (5.2.x):** block privileged, hostPID/hostIPC/hostNetwork, hostPath and allowPrivilegeEscalation pods (use Pod Security Admission labels on namespaces); 5.2.7 non-root is L2.
- **Network policy (5.3.1, 5.3.2):** k3s ships flannel, which does not enforce NetworkPolicy by default (k3s embeds a network policy controller you can leave enabled), so verify policies are actually enforced before relying on them.

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Control Plane Components

#### 1.1 Control Plane Node Configuration Files

- [ ] 1.1.1 Ensure that the API server pod specification file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.2 Ensure that the API server pod specification file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.3 Ensure that the controller manager pod specification file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.4 Ensure that the controller manager pod specification file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.5 Ensure that the scheduler pod specification file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.6 Ensure that the scheduler pod specification file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.7 Ensure that the etcd pod specification file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.8 Ensure that the etcd pod specification file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.9 Ensure that the Container Network Interface file permissions are set to 600 or more restrictive — L1 Master · Manual
- [ ] 1.1.10 Ensure that the Container Network Interface file ownership is set to root:root — L1 Master · Manual
- [ ] 1.1.11 Ensure that the etcd data directory permissions are set to 700 or more restrictive — L1 Master · Automated
- [ ] 1.1.12 Ensure that the etcd data directory ownership is set to etcd:etcd — L1 Master · Automated
- [ ] 1.1.13 Ensure that the default administrative credential file permissions are set to 600 — L1 Master · Automated
- [ ] 1.1.14 Ensure that the default administrative credential file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.15 Ensure that the scheduler.conf file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.16 Ensure that the scheduler.conf file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.17 Ensure that the controller-manager.conf file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 1.1.18 Ensure that the controller-manager.conf file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.19 Ensure that the Kubernetes PKI directory and file ownership is set to root:root — L1 Master · Automated
- [ ] 1.1.20 Ensure that the Kubernetes PKI certificate file permissions are set to 644 or more restrictive — L1 Master · Manual
- [ ] 1.1.21 Ensure that the Kubernetes PKI key file permissions are set to 600 — L1 Master · Manual

#### 1.2 API Server

- [ ] 1.2.1 Ensure that the --anonymous-auth argument is set to false — L1 Master · Manual
- [ ] 1.2.2 Ensure that the --token-auth-file parameter is not set — L1 Master · Automated
- [ ] 1.2.3 Ensure that the DenyServiceExternalIPs is set — L1 Master · Manual
- [ ] 1.2.4 Ensure that the --kubelet-client-certificate and --kubelet-client-key arguments are set as appropriate — L1 Master · Automated
- [ ] 1.2.5 Ensure that the --kubelet-certificate-authority argument is set as appropriate — L1 Master · Automated
- [ ] 1.2.6 Ensure that the --authorization-mode argument is not set to AlwaysAllow — L1 Master · Automated
- [ ] 1.2.7 Ensure that the --authorization-mode argument includes Node — L1 Master · Automated
- [ ] 1.2.8 Ensure that the --authorization-mode argument includes RBAC — L1 Master · Automated
- [ ] 1.2.9 Ensure that the admission control plugin EventRateLimit is set — L1 Master · Manual
- [ ] 1.2.10 Ensure that the admission control plugin AlwaysAdmit is not set — L1 Master · Automated
- [ ] 1.2.11 Ensure that the admission control plugin AlwaysPullImages is set — L1 Master · Manual
- [ ] 1.2.12 Ensure that the admission control plugin ServiceAccount is set — L2 Master · Automated
- [ ] 1.2.13 Ensure that the admission control plugin NamespaceLifecycle is set — L2 Master · Automated
- [ ] 1.2.14 Ensure that the admission control plugin NodeRestriction is set — L2 Master · Automated
- [ ] 1.2.15 Ensure that the --profiling argument is set to false — L1 Master · Automated
- [ ] 1.2.16 Ensure that the --audit-log-path argument is set — L1 Master · Automated
- [ ] 1.2.17 Ensure that the --audit-log-maxage argument is set to 30 or as appropriate — L1 Master · Automated
- [ ] 1.2.18 Ensure that the --audit-log-maxbackup argument is set to 10 or as appropriate — L1 Master · Automated
- [ ] 1.2.19 Ensure that the --audit-log-maxsize argument is set to 100 or as appropriate — L1 Master · Automated
- [ ] 1.2.20 Ensure that the --request-timeout argument is set as appropriate — L1 Master · Manual
- [ ] 1.2.21 Ensure that the --service-account-lookup argument is set to true — L1 Master · Automated
- [ ] 1.2.22 Ensure that the --service-account-key-file argument is set as appropriate — L1 Master · Automated
- [ ] 1.2.23 Ensure that the --etcd-certfile and --etcd-keyfile arguments are set as appropriate — L1 Master · Automated
- [ ] 1.2.24 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate — L1 Master · Automated
- [ ] 1.2.25 Ensure that the --client-ca-file argument is set as appropriate — L1 Master · Automated
- [ ] 1.2.26 Ensure that the --etcd-cafile argument is set as appropriate — L1 Master · Automated
- [ ] 1.2.27 Ensure that the --encryption-provider-config argument is set as appropriate — L1 Master · Manual
- [ ] 1.2.28 Ensure that encryption providers are appropriately configured — L1 Master · Manual
- [ ] 1.2.29 Ensure that the API Server only makes use of Strong Cryptographic Ciphers — L1 Master · Manual
- [ ] 1.2.30 Ensure that the --service-account-extend-token-expiration parameter is set to false — L1 Master · Automated

#### 1.3 Controller Manager

- [ ] 1.3.1 Ensure that the --terminated-pod-gc-threshold argument is set as appropriate — L1 Master · Manual
- [ ] 1.3.2 Ensure that the --profiling argument is set to false — L1 Master · Automated
- [ ] 1.3.3 Ensure that the --use-service-account-credentials argument is set to true — L1 Master · Automated
- [ ] 1.3.4 Ensure that the --service-account-private-key-file argument is set as appropriate — L1 Master · Automated
- [ ] 1.3.5 Ensure that the --root-ca-file argument is set as appropriate — L1 Master · Automated
- [ ] 1.3.6 Ensure that the RotateKubeletServerCertificate argument is set to true — L1 Master · Automated
- [ ] 1.3.7 Ensure that the --bind-address argument is set to 127.0.0.1 — L1 Master · Automated

#### 1.4 Scheduler

- [ ] 1.4.1 Ensure that the --profiling argument is set to false — L1 Master · Automated
- [ ] 1.4.2 Ensure that the --bind-address argument is set to 127.0.0.1 — L1 Master · Automated

### 2 etcd

- [ ] 2.1 Ensure that the --cert-file and --key-file arguments are set as appropriate — L1 Master · Automated
- [ ] 2.2 Ensure that the --cert-file and --key-file arguments are set as appropriate — L1 Master · Automated
- [ ] 2.3 Ensure that the --client-cert-auth argument is set to true — L1 Master · Automated
- [ ] 2.4 Ensure that the --auto-tls argument is not set to true — L1 Master · Automated
- [ ] 2.5 Ensure that the --peer-cert-file and --peer-key-file arguments are set as appropriate — L1 Master · Automated
- [ ] 2.6 Ensure that the --peer-client-cert-auth argument is set to true — L1 Master · Automated
- [ ] 2.7 Ensure that the --peer-auto-tls argument is not set to true — L1 Master · Automated
- [ ] 2.8 Ensure that a unique Certificate Authority is used for etcd — L2 Master · Manual

### 3 Control Plane Configuration

#### 3.1 Authentication and Authorization

- [ ] 3.1.1 Client certificate authentication should not be used for users — L1 Master · Manual
- [ ] 3.1.2 Service account token authentication should not be used for users — L1 Master · Manual
- [ ] 3.1.3 Bootstrap token authentication should not be used for users — L1 Master · Manual

#### 3.2 Logging

- [ ] 3.2.1 Ensure that a minimal audit policy is created — L1 Master · Manual
- [ ] 3.2.2 Ensure that the audit policy covers key security concerns — L2 Master · Manual

### 4 Worker Nodes

#### 4.1 Worker Node Configuration Files

- [ ] 4.1.1 Ensure that the kubelet service file permissions are set to 600 or more restrictive — L1 Master · Automated
- [ ] 4.1.2 Ensure that the kubelet service file ownership is set to root:root — L1 Worker · Automated
- [ ] 4.1.3 If proxy kubeconfig file exists ensure permissions are set to 600 or more restrictive — L1 Worker · Manual
- [ ] 4.1.4 If proxy kubeconfig file exists ensure ownership is set to root:root — L1 Worker · Manual
- [ ] 4.1.5 Ensure that the --kubeconfig kubelet.conf file permissions are set to 600 or more restrictive — L1 Worker · Automated
- [ ] 4.1.6 Ensure that the --kubeconfig kubelet.conf file ownership is set to root:root — L1 Worker · Automated
- [ ] 4.1.7 Ensure that the certificate authorities file permissions are set to 644 or more restrictive — L1 Worker · Manual
- [ ] 4.1.8 Ensure that the client certificate authorities file ownership is set to root:root — L1 Worker · Manual
- [ ] 4.1.9 If the kubelet config.yaml configuration file is being used validate permissions set to 600 or more restrictive — L1 Worker · Automated
- [ ] 4.1.10 If the kubelet config.yaml configuration file is being used validate file ownership is set to root:root — L1 Worker · Automated

#### 4.2 Kubelet

- [ ] 4.2.1 Ensure that the --anonymous-auth argument is set to false — L1 Worker · Automated
- [ ] 4.2.2 Ensure that the --authorization-mode argument is not set to AlwaysAllow — L1 Worker · Automated
- [ ] 4.2.3 Ensure that the --client-ca-file argument is set as appropriate — L1 Worker · Automated
- [ ] 4.2.4 Verify that if defined, readOnlyPort is set to 0 — L1 Worker · Manual
- [ ] 4.2.5 Ensure that the --streaming-connection-idle-timeout argument is not set to 0 — L1 Worker · Manual
- [ ] 4.2.6 Ensure that the --make-iptables-util-chains argument is set to true — L1 Worker · Automated
- [ ] 4.2.7 Ensure that the --hostname-override argument is not set — L1 Worker · Manual
- [ ] 4.2.8 Ensure that the eventRecordQPS argument is set to a level which ensures appropriate event capture — L2 Worker · Manual
- [ ] 4.2.9 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate — L1 Worker · Manual
- [ ] 4.2.10 Ensure that the --rotate-certificates argument is not set to false — L1 Worker · Automated
- [ ] 4.2.11 Verify that the RotateKubeletServerCertificate argument is set to true — L1 Worker · Manual
- [ ] 4.2.12 Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers — L1 Worker · Manual
- [ ] 4.2.13 Ensure that a limit is set on pod PIDs — L1 Worker · Manual
- [ ] 4.2.14 Ensure that the --seccomp-default parameter is set to true — L1 Worker · Manual
- [ ] 4.2.15 Ensure that the --IPAddressDeny is set to any — L2 Worker · Manual

#### 4.3 kube-proxy

- [ ] 4.3.1 Ensure that the kube-proxy metrics service is bound to localhost — L1 Worker · Manual

### 5 Policies

#### 5.1 RBAC and Service Accounts

- [ ] 5.1.1 Ensure that the cluster-admin role is only used where required — L1 Master · Manual
- [ ] 5.1.2 Minimize access to secrets — L1 Master · Manual
- [ ] 5.1.3 Minimize wildcard use in Roles and ClusterRoles — L1 Worker · Manual
- [ ] 5.1.4 Minimize access to create pods — L1 Master · Manual
- [ ] 5.1.5 Ensure that default service accounts are not actively used. — L1 Master · Manual
- [ ] 5.1.6 Ensure that Service Account Tokens are only mounted where necessary — L1 Master · Manual
- [ ] 5.1.7 Avoid use of system:masters group — L1 Master · Manual
- [ ] 5.1.8 Limit use of the Bind, Impersonate and Escalate permissions in the Kubernetes cluster — L1 Master · Manual
- [ ] 5.1.9 Minimize access to create persistent volumes — L1 Master · Manual
- [ ] 5.1.10 Minimize access to the proxy sub-resource of nodes — L1 Master · Manual
- [ ] 5.1.11 Minimize access to the approval sub-resource of certificatesigningrequests objects — L1 Master · Manual
- [ ] 5.1.12 Minimize access to webhook configuration objects — L1 Master · Manual
- [ ] 5.1.13 Minimize access to the service account token creation — L1 Master · Manual

#### 5.2 Pod Security Standards

- [ ] 5.2.1 Ensure that the cluster has at least one active policy control mechanism in place — L1 Master · Manual
- [ ] 5.2.2 Minimize the admission of privileged containers — L1 Master · Manual
- [ ] 5.2.3 Minimize the admission of containers wishing to share the host process ID namespace — L1 Master · Manual
- [ ] 5.2.4 Minimize the admission of containers wishing to share the host IPC namespace — L1 Master · Manual
- [ ] 5.2.5 Minimize the admission of containers wishing to share the host network namespace — L1 Master · Manual
- [ ] 5.2.6 Minimize the admission of containers with allowPrivilegeEscalation — L1 Master · Manual
- [ ] 5.2.7 Minimize the admission of root containers — L2 Master · Manual
- [ ] 5.2.8 Minimize the admission of containers with the NET_RAW capability — L1 Master · Manual
- [ ] 5.2.9 Minimize the admission of containers with added capabilities — L1 Master · Manual
- [ ] 5.2.10 Minimize the admission of containers with capabilities assigned — L2 Master · Manual
- [ ] 5.2.11 Minimize the admission of Windows HostProcess Containers — L1 Master · Manual
- [ ] 5.2.12 Minimize the admission of HostPath volumes — L1 Master · Manual
- [ ] 5.2.13 Minimize the admission of containers which use HostPorts — L1 Master · Manual

#### 5.3 Network Policies and CNI

- [ ] 5.3.1 Ensure that the CNI in use supports Network Policies — L1 Master · Manual
- [ ] 5.3.2 Ensure that all Namespaces have Network Policies defined — L2 Master · Manual

#### 5.4 Secrets Management

- [ ] 5.4.1 Prefer using secrets as files over secrets as environment variables — L2 Master · Manual
- [ ] 5.4.2 Consider external secret storage — L2 Master · Manual

#### 5.5 Extensible Admission Control

- [ ] 5.5.1 Configure Image Provenance using ImagePolicyWebhook admission controller — L2 Master · Manual

#### 5.6 General Policies

- [ ] 5.6.1 Create administrative boundaries between resources using namespaces — L1 Master · Manual
- [ ] 5.6.2 Ensure that the seccomp profile is set to docker/default in your pod definitions — L2 Master · Manual
- [ ] 5.6.3 Apply Security Context to Your Pods and Containers — L2 Master · Manual
- [ ] 5.6.4 The default namespace should not be used — L2 Master · Manual

## Source

CIS Kubernetes Benchmark v1.11.1 (04-16-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[container-security/kubernetes/basic-commands]]
- [[container-security/docker/docker-container]]
- [[container-security/docker/expose-docker-remotely]]
- [[enumeration/protocols-and-ports/2375-docker]]
- [[grc-frameworks/cis-benchmarks/cis-docker]]
- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
