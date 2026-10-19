---
title: cis-docker
tags: [grc-frameworks, cis-benchmarks, type/reference, phase/hardening, platform/container, platform/linux, source/cis]
description: "CIS Docker Benchmark v1.8.0 checklist: host, daemon, files, images, runtime, swarm, with levels."
source_pdf: CIS_Docker_Benchmark_v1.8.0.pdf
---

# CIS Docker Benchmark v1.8.0 (07-24-2025)

## Overview

- **Product:** Docker Engine on Linux, plus Docker Swarm
- **Benchmark version:** v1.8.0 (2025-07-24)
- **Profiles:** Level 1 - Docker - Linux, Level 2 - Docker - Linux, and Level 1 - Docker Swarm. Items are Docker-Linux unless the suffix says Swarm.
- **Recommendations:** 118 total (23 Automated, 95 Manual)
- **Checklist legend:** level (L1/L2) and assessment status come from the benchmark; a suffix after the level (for example Server, Workstation, Master, Worker, Swarm, Web, LB) means the item only applies to that profile variant.

### Section outline

| Section | Recommendations |
|---|---|
| 1 Host Configuration | 20 |
| 2 Docker daemon configuration | 19 |
| 3 Docker daemon configuration files | 24 |
| 4 Container Images and Build File Configuration | 12 |
| 5 Container Runtime Configuration | 32 |
| 6 Docker Security Operations | 2 |
| 7 Docker Swarm Configuration | 9 |

## Lab relevance

- **Daemon exposure (2.8, 2.13, 3.x):** never expose the TCP socket without TLS client auth (2.8); check `/var/run/docker.sock` and `docker.service` ownership and permissions (section 3).
- **Docker socket (5.32, 1.1.2):** do not mount the socket into containers (relevant to CI runners, Gitea Actions runners and Caddy docker-proxy plugins) and limit who is in the `docker` group.
- **Privilege reduction (5.4, 5.5, 5.26, 2.15):** drop capabilities, no `--privileged`, `no-new-privileges` as a daemon default.
- **Host sharing (5.6, 5.10, 5.16-5.18, 5.20, 5.31):** no sensitive host mounts, no host network/PID/IPC/UTS namespaces, no shared mount propagation.
- **Resource and filesystem limits (5.11, 5.13, 5.29):** memory limits, read-only root filesystem and PIDs cgroup limit for Caddy, Gitea and PostgreSQL containers where practical.
- **Port binding (5.14, 5.9):** bind published ports to a specific host interface (for example PostgreSQL to 127.0.0.1 or an internal docker network) instead of 0.0.0.0.
- **Images and secrets (4.1, 4.2, 4.4, 4.10, 4.12):** non-root user, trusted base images, regular rescans and rebuilds, no secrets in Dockerfiles or image layers, validated signatures.
- **Logging and iptables (2.3, 2.4, 2.14):** keep Docker allowed to manage iptables (2.4) and plan central logging (2.14). 1.1.x audit rules need auditd on the host.

## Recommendation checklist

Titles only; see the official benchmark for rationale, audit and remediation steps.

### 1 Host Configuration

#### 1.1 Linux Hosts Specific Configuration

- [ ] 1.1.1 Ensure a separate partition for containers has been created — L1 · Manual
- [ ] 1.1.2 Ensure only trusted users are allowed to control Docker daemon — L1 · Manual
- [ ] 1.1.3 Ensure auditing is configured for the Docker daemon — L1 · Automated
- [ ] 1.1.4 Ensure auditing is configured for Docker files and directories - /run/containerd — L1 · Manual
- [ ] 1.1.5 Ensure auditing is configured for Docker files and directories - /var/lib/docker — L1 · Manual
- [ ] 1.1.6 Ensure auditing is configured for Docker files and directories - /etc/docker — L1 · Automated
- [ ] 1.1.7 Ensure auditing is configured for Docker files and directories - docker.service — L2 · Automated
- [ ] 1.1.8 Ensure auditing is configured for Docker files and directories - containerd.sock — L2 · Automated
- [ ] 1.1.9 Ensure auditing is configured for Docker files and directories - docker.sock — L2 · Automated
- [ ] 1.1.10 Ensure auditing is configured for Docker files and directories - /etc/default/docker — L2 · Automated
- [ ] 1.1.11 Ensure auditing is configured for Docker files and directories - /etc/docker/daemon.json — L2 · Automated
- [ ] 1.1.12 Ensure auditing is configured for Docker files and directories /etc/containerd/config.toml — L2 · Automated
- [ ] 1.1.13 Ensure auditing is configured for Docker files and directories - /etc/sysconfig/docker — L2 · Automated
- [ ] 1.1.14 Ensure auditing is configured for Docker files and directories - /usr/bin/containerd — L2 · Automated
- [ ] 1.1.15 Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shim — L2 · Automated
- [ ] 1.1.16 Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shimrunc-v1 — L2 · Manual
- [ ] 1.1.17 Ensure auditing is configured for Docker files and directories - /usr/bin/containerd-shimrunc-v2 — L2 · Automated
- [ ] 1.1.18 Ensure auditing is configured for Docker files and directories - /usr/bin/runc — L2 · Automated

#### 1.2 General Configuration

- [ ] 1.2.1 Ensure the container host has been Hardened — L1 · Manual
- [ ] 1.2.2 Ensure that the version of Docker is up to date — L1 · Manual

### 2 Docker daemon configuration

- [ ] 2.1 Run the Docker daemon as a non-root user, if possible — L1 · Manual
- [ ] 2.2 Ensure network traffic is restricted between containers on the default bridge — L1 · Manual
- [ ] 2.3 Ensure the logging level is set to 'info' — L1 · Manual
- [ ] 2.4 Ensure Docker is allowed to make changes to iptables — L1 · Manual
- [ ] 2.5 Ensure insecure registries are not used — L1 · Manual
- [ ] 2.6 Ensure aufs storage driver is not used — L1 · Manual
- [ ] 2.7 Ensure devicemapper storage driver is not used — L1 · Manual
- [ ] 2.8 Ensure TLS authentication for Docker daemon is configured — L1 · Manual
- [ ] 2.9 Ensure the default ulimit is configured appropriately — L1 · Manual
- [ ] 2.10 Enable user namespace support — L2 · Manual
- [ ] 2.11 Ensure the default cgroup usage has been confirmed — L2 · Manual
- [ ] 2.12 Ensure base device size is not changed until needed — L2 · Manual
- [ ] 2.13 Ensure that authorization for Docker client commands is enabled — L2 · Manual
- [ ] 2.14 Ensure centralized and remote logging is configured — L2 · Manual
- [ ] 2.15 Ensure containers are restricted from acquiring new privileges — L1 · Manual
- [ ] 2.16 Ensure live restore is enabled — L1 · Manual
- [ ] 2.17 Ensure Userland Proxy is Disabled — L1 · Manual
- [ ] 2.18 Ensure that a daemon-wide custom seccomp profile is applied if appropriate — L2 · Manual
- [ ] 2.19 Ensure that experimental features are not implemented in production — L1 · Manual

### 3 Docker daemon configuration files

- [ ] 3.1 Ensure that the docker.service file ownership is set to root:root — L1 · Automated
- [ ] 3.2 Ensure that docker.service file permissions are appropriately set — L1 · Automated
- [ ] 3.3 Ensure that docker.socket file ownership is set to root:root — L1 · Automated
- [ ] 3.4 Ensure that docker.socket file permissions are set to 644 or more restrictive — L1 · Automated
- [ ] 3.5 Ensure that the /etc/docker directory ownership is set to root:root — L1 · Automated
- [ ] 3.6 Ensure that /etc/docker directory permissions are set to 755 or more restrictively — L1 · Automated
- [ ] 3.7 Ensure that registry certificate file ownership is set to root:root — L1 · Manual
- [ ] 3.8 Ensure that registry certificate file permissions are set to 444 or more restrictively — L1 · Manual
- [ ] 3.9 Ensure that TLS CA certificate file ownership is set to root:root — L1 · Manual
- [ ] 3.10 Ensure that TLS CA certificate file permissions are set to 444 or more restrictively — L1 · Manual
- [ ] 3.11 Ensure that Docker server certificate file ownership is set to root:root — L1 · Manual
- [ ] 3.12 Ensure that the Docker server certificate file permissions are set to 444 or more restrictively — L1 · Manual
- [ ] 3.13 Ensure that the Docker server certificate key file ownership is set to root:root — L1 · Manual
- [ ] 3.14 Ensure that the Docker server certificate key file permissions are set to 400 — L1 · Manual
- [ ] 3.15 Ensure that the Docker socket file ownership is set to root:docker — L1 · Automated
- [ ] 3.16 Ensure that the Docker socket file permissions are set to 660 or more restrictively — L1 · Automated
- [ ] 3.17 Ensure that the daemon.json file ownership is set to root:root — L2 · Manual
- [ ] 3.18 Ensure that daemon.json file permissions are set to 644 or more restrictive — L2 · Manual
- [ ] 3.19 Ensure that the /etc/default/docker file ownership is set to root:root — L2 · Manual
- [ ] 3.20 Ensure that the /etc/default/docker file permissions are set to 644 or more restrictively — L2 · Manual
- [ ] 3.21 Ensure that the /etc/sysconfig/docker file permissions are set to 644 or more restrictively — L2 · Manual
- [ ] 3.22 Ensure that the /etc/sysconfig/docker file ownership is set to root:root — L2 · Manual
- [ ] 3.23 Ensure that the Containerd socket file ownership is set to root:root — L1 · Automated
- [ ] 3.24 Ensure that the Containerd socket file permissions are set to 660 or more restrictively — L1 · Automated

### 4 Container Images and Build File Configuration

- [ ] 4.1 Ensure that a user for the container has been created — L1 · Manual
- [ ] 4.2 Ensure that containers use only trusted base images — L1 · Manual
- [ ] 4.3 Ensure that unnecessary packages are not installed in the container — L1 · Manual
- [ ] 4.4 Ensure images are scanned and rebuilt to include security patches — L1 · Manual
- [ ] 4.5 Ensure Content trust for Docker is Enabled — L2 · Manual
- [ ] 4.6 Ensure that HEALTHCHECK instructions have been added to container images — L1 · Manual
- [ ] 4.7 Ensure update instructions are not used alone in Dockerfiles — L1 · Manual
- [ ] 4.8 Ensure setuid and setgid permissions are removed — L2 · Manual
- [ ] 4.9 Ensure that COPY is used instead of ADD in Dockerfiles — L1 · Manual
- [ ] 4.10 Ensure secrets are not stored in Dockerfiles — L1 · Manual
- [ ] 4.11 Ensure only verified packages are installed — L2 · Manual
- [ ] 4.12 Ensure all signed artifacts are validated — L1 · Manual

### 5 Container Runtime Configuration

- [ ] 5.1 Ensure swarm mode is not Enabled, if not needed — L1 · Manual
- [ ] 5.2 Ensure that, if applicable, an AppArmor Profile is enabled — L1 · Manual
- [ ] 5.3 Ensure that, if applicable, SELinux security options are set — L2 · Manual
- [ ] 5.4 Ensure that Linux kernel capabilities are restricted within containers — L1 · Manual
- [ ] 5.5 Ensure that privileged containers are not used — L1 · Manual
- [ ] 5.6 Ensure sensitive host system directories are not mounted on containers — L1 · Manual
- [ ] 5.7 Ensure sshd is not run within containers — L1 · Manual
- [ ] 5.8 Ensure privileged ports are not mapped within containers — L1 · Manual
- [ ] 5.9 Ensure that only needed ports are open on the container — L1 · Manual
- [ ] 5.10 Ensure that the host's network namespace is not shared — L1 · Manual
- [ ] 5.11 Ensure that the memory usage for containers is limited — L1 · Manual
- [ ] 5.12 Ensure that CPU priority is set appropriately on containers — L1 · Manual
- [ ] 5.13 Ensure that the container's root filesystem is mounted as read only — L1 · Manual
- [ ] 5.14 Ensure that incoming container traffic is bound to a specific host interface — L1 · Manual
- [ ] 5.15 Ensure that the 'on-failure' container restart policy is set to '5' — L1 · Manual
- [ ] 5.16 Ensure that the host's process namespace is not shared — L1 · Manual
- [ ] 5.17 Ensure that the host's IPC namespace is not shared — L1 · Manual
- [ ] 5.18 Ensure that host devices are not directly exposed to containers — L1 · Manual
- [ ] 5.19 Ensure that the default ulimit is overwritten at runtime if needed — L1 · Manual
- [ ] 5.20 Ensure mount propagation mode is not set to shared — L1 · Manual
- [ ] 5.21 Ensure that the host's UTS namespace is not shared — L1 · Manual
- [ ] 5.22 Ensure the default seccomp profile is not Disabled — L1 · Manual
- [ ] 5.23 Ensure that docker exec commands are not used with the privileged option — L2 · Manual
- [ ] 5.24 Ensure that docker exec commands are not used with the user=root option — L2 · Manual
- [ ] 5.25 Ensure that cgroup usage is confirmed — L1 · Manual
- [ ] 5.26 Ensure that the container is restricted from acquiring additional privileges — L1 · Manual
- [ ] 5.27 Ensure that container health is checked at runtime — L1 · Manual
- [ ] 5.28 Ensure that Docker commands always make use of the latest version of their image — L1 · Manual
- [ ] 5.29 Ensure that the PIDs cgroup limit is used — L1 · Manual
- [ ] 5.30 Ensure that Docker's default bridge "docker0" is not used — L2 · Manual
- [ ] 5.31 Ensure that the host's user namespaces are not shared — L1 · Manual
- [ ] 5.32 Ensure that the Docker socket is not mounted inside any containers — L1 · Manual

### 6 Docker Security Operations

- [ ] 6.1 Ensure that image sprawl is avoided — L1 · Manual
- [ ] 6.2 Ensure that container sprawl is avoided — L1 · Manual

### 7 Docker Swarm Configuration

- [ ] 7.1 Ensure that the minimum number of manager nodes have been created in a swarm — L1 Swarm · Manual
- [ ] 7.2 Ensure that swarm services are bound to a specific host interface — L1 Swarm · Manual
- [ ] 7.3 Ensure that all Docker swarm overlay networks are encrypted — L1 Swarm · Manual
- [ ] 7.4 Ensure that Docker's secret management commands are used for managing secrets in a swarm cluster — L1 Swarm · Manual
- [ ] 7.5 Ensure that swarm manager is run in auto-lock mode — L1 Swarm · Manual
- [ ] 7.6 Ensure that the swarm manager auto-lock key is rotated periodically — L1 Swarm · Manual
- [ ] 7.7 Ensure that node certificates are rotated as appropriate — L1 Swarm · Manual
- [ ] 7.8 Ensure that CA certificates are rotated as appropriate — L1 Swarm · Manual
- [ ] 7.9 Ensure that management plane traffic is separated from data plane traffic — L1 Swarm · Manual

## Source

CIS Docker Benchmark v1.8.0 (07-24-2025), Center for Internet Security. Used under CC BY-NC-SA 4.0.

## Related

- [[container-security/docker/docker-container]]
- [[container-security/docker/expose-docker-remotely]]
- [[enumeration/protocols-and-ports/2375-docker]]
- [[container-security/kubernetes/basic-commands]]
- [[grc-frameworks/cis-benchmarks/cis-kubernetes]]
- [[grc-frameworks/cis-benchmarks/cis-ubuntu-24-04]]
