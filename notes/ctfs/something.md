---
title: something
tags: [ctfs, type/walkthrough]
---

# Something()

```
something:

push rbp

mov rbp, rsp

mov DWORD PTR [rbp-0x14], edi

mov DWORD PTR [rbp-0x4], 0x0

mov DWORD PTR [rbp-0x8], 0x0

jmp label_2

  

label_1:

mov eax, DWORD PTR [rbp-0x8]

add DWORD PTR [rbp-0x4], eax

add DWORD PTR [rbp-0x8], 0x1

  

label_2:

mov eax, DWORD PTR [rbp-0x8]

cmp eax, DWORD PTR [rbp-0x14]

jl label_1

mov eax, DWORD PTR [rbp-0x4]

pop rbp

ret
```

### Code Breakdown

The function uses the stack to store local variables and the input argument. Here is the mapping:

- **`[rbp-0x14]`**: The input argument ($n = 10$).
    
- **`[rbp-0x4]`**: A variable we'll call `total` (initialized to $0$).
    
- **`[rbp-0x8]`**: A loop counter we'll call `i` (initialized to $0$).
    

The logic follows a standard `while` loop structure:

1. **Initialization**: `total = 0`, `i = 0`.
    
2. **Comparison (`label_2`)**: Compare `i` to the input $n$ ($10$). If `i < 10`, jump to `label_1`.
    
3. **Loop Body (`label_1`)**:
    
    - Add the current value of `i` to `total`.
        
    - Increment `i` by $1$.
        
    - Continue to the comparison in `label_2`.
        
4. **Return**: Once `i` reaches $10$, the condition `jl` (jump if less than) fails. The function moves the final `total` into the `eax` register and returns.
    

---

### Step-by-Step Execution

Since the loop adds the value of `i` to the total and then increments `i`, the function is calculating the sum of all integers from $0$ up to (but not including) $10$.

|**Iteration**|**i**|**total (before addition)**|**total (after addition)**|
|---|---|---|---|
|1|0|0|0|
|2|1|0|1|
|3|2|1|3|
|4|3|3|6|
|5|4|6|10|
|6|5|10|15|
|7|6|15|21|
|8|7|21|28|
|9|8|28|36|
|10|9|36|**45**|
|11|10|_Loop terminates (10 is not < 10)_||

The sum of $0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45$.

The value returned from `something(10)` is **45**.