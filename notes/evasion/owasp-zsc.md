---
title: owasp-zsc
tags: [evasion, type/cheatsheet, phase/evasion, platform/linux]
---

# OWASP-ZSC

## Help Menu

```
zsc> help
```

## Generate Shellcode

```
zsc> shellcode

zsc> generate
```

You can use tab compilation&#x20;
   
## Generate Linux Shellcode

```
zsc/shellcode/generate/> linux_x86
```

### Generate system("/bin/sh") payload with no encoders

```
zsc/shellcode/generate/linux_x86> system
```

```
zsc/shellcode/generate/linux_x86/system> command_to_execute
```

```
command_to_execute> /bin/sh
```

```
zsc/shellcode/generate/linux_x86/system/encode_type> 
```

```
zsc/shellcode/generate/linux_x86/system/encode_type> none
```

```
Output assembly code?(y or n)> y
```

```
Output shellcode to screen?(y or n)> y
```

```
Shellcode output to a .c file?(y or n)> n
```

### Generate system("/bin/sh") with xor\_random encoder

```
python3 zsc.py -p linux_x86/system/xor_random -i /bin/sh
```

Now, Copy the shellcode and paste into the PoC
   
## Search for Shell\_Storm Shell Code

```
python3 zsc.py --shell-storm search 'linux/x86 bind 1337'
```

          (82) 

### Download the shellcode

```
python3 zsc.py --shell-storm download 882
```

## Obsfucate the Exploit

```
zsc> help
```

```
zsc> obfuscate
```

```
zsc/obfuscate> python
```

```
filename> /home/l3mon/Desktop/hello.py
```

```
encode> simple_base64_rev
```

The original code will be at the top within comments.

Followed by the obfuscated code.
   
          (83) 
