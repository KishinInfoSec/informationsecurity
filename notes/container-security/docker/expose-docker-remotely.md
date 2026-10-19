---
title: expose-docker-remotely
tags: [container-security, docker, type/cheatsheet, platform/linux, platform/container]
---

# Expose Docker Remotely

## Theory

Exposing Docker remotely means allowing connections to the Docker daemon from machines other than the one it is running on. This can be useful for managing Docker containers on remote servers, or for exposing Dockerized applications to the public internet.

A remote Docker host is a machine, inside or outside our local network which is running a Docker Engine and has ports exposed for querying the Engine API. The sample application can be deployed on a remote host in several way



***

## Practical

  
Docker must be installed on your system.
   

### Check Docker Process

```
ps -ef | grep docker
```

          (206) 

### Edit docker.service File

```
vim /lib/systemd/system/docker.service

# add or modify the below line
ExecStart=/usr/bin/dockerd -H=fd:// -H=tcp://0.0.0.0:2375
```

          (207) 

### Reload and Restart

```
systemctl daemon-reload

sudo service docker restart
```

### Test

```
curl 
```

          (208) 



***

## REFERENCES

* 
* 

