---
title: assembly01
tags: [ctfs, type/walkthrough]
---

# Assembly01

![[Pasted image 20260330181314.png]]

### 1. Setup the Socket Structure (`loc_1000244A`)

This section prepares the `sockaddr_in` structure required for network communication.

- **Port Conversion:** * It takes a string representation of a port number (located at `[ebp+var_44]`) and passes it to `atoi` to convert it into an integer.
    
    - It immediately takes that integer and passes it to `htons` (Host TO Network Short) to ensure the byte order is correct for network transmission.
        
    - The result is stored in `[ebp+var_22]`, which aligns with the `sin_port` field of a `sockaddr_in` struct.
        
- **Address Family:** * `mov [ebp+Dst], 2` sets a value to 2. In Windows and Linux networking, `2` corresponds to `AF_INET` (IPv4). This is the `sin_family` field.
    
- **Copying the IP Address:**
    
    - It extracts an IP address size (from `[esi+0Ah]`) and a source pointer (from `[esi+0Ch]`).
        
    - It uses `memcpy` to copy the IP address bytes into `[ebp+var_20]`, which acts as the `sin_addr` field.
        
    - `add esp, 0Ch` cleans up the stack after the `memcpy` call (3 arguments * 4 bytes each = 12 bytes, or `0xC` in hex).
        

### 2. Creating the Socket (`loc_1000247E`)

This block actually invokes the `socket` API.

- It pushes the arguments for the `socket()` function in reverse order (standard x86 `stdcall`/`cdecl` behavior):
    
    - `push ebx` (protocol, likely 0 or `IPPROTO_TCP`)
        
    - `push 1` (`SOCK_STREAM`, meaning it's a TCP socket)
        
    - `push 2` (`AF_INET`, meaning IPv4)
        
- It calls `socket()` and stores the returned socket handle in `esi` and `[ebp+s]`.
    
- It compares the result against `0FFFFFFFFh` (-1, which represents `INVALID_SOCKET`).
    
- `jnz short loc_100024AD`: If the socket is valid (not equal to -1), it jumps ahead to continue execution.
    

### 3. Error Handling (`loc_10002493`)

If the socket creation failed, execution falls through to this block.

- It loads a pointer to a format string: `"Socket error....\n"`.
    
- It writes an error code/status `190h` (400 in decimal) into a structure tracked by `[ebp+File]`.
    
- It calls `printf` to output the error message.
    
- It jumps away to a cleanup or exit routine (`loc_10002CB4`).
    

### 4. Socket Configuration (`loc_100024AD`)

This is the success path where execution resumes if the socket was created successfully.

- The code pushes `optval` and an `optlen` of 4 onto the stack. While cut off, this perfectly matches the setup for a `setsockopt` call, likely configuring something like `SO_REUSEADDR`, receive timeouts, or a similar socket behavior before binding or connecting.
    

### High-Level C Translation

For a reverse engineer, it is often easier to map this back to mental pseudo-C. The assembly above translates roughly to this logic:

```
struct sockaddr_in dest_addr;

// loc_1000244A
dest_addr.sin_family = AF_INET; // 2
dest_addr.sin_port = htons(atoi(port_string));
memcpy(&dest_addr.sin_addr, source_ip_ptr, ip_size);

// loc_1000247E
SOCKET s = socket(AF_INET, SOCK_STREAM, protocol);

if (s == INVALID_SOCKET) { // -1 / 0xFFFFFFFF
    // loc_10002493
    file_obj->status = 0x190;
    printf("Socket error....\n");
    goto cleanup; // jmp loc_10002CB4
}

// loc_100024AD
// Preparing for setsockopt(s, level, optname, &optval, 4);
```