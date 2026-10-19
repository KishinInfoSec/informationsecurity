---
title: ask-nicely
tags: [ctfs, type/walkthrough]
---

# Ask-Nicely

![[mining.asm]]
### Analysis of the `check` Function

The function performs several checks on the input buffer:

1. **Prefix and Suffix Logic:**
    
    - The program uses three global pointers: `monkey`, `gold`, and `meatball`. Based on their names and the logic, these likely point to the strings `"monkey"`, `"gold"`, and `"meatball"`.
        
    - **Index 0:** Compared against `monkey[5]` ('y'). Result: **`y`**.
        
    - **Suffix:** The last 4 characters of the input are compared against the string pointed to by `gold`. Result: **`gold`**.
        
2. **Hardcoded Character Checks:**
    
    - **Index 2:** Must be `'u'`.
        
    - **Index 4:** Must be `'s'`.
        
    - **Index 7:** Must be `'u'`.
        
    - **Index 10:** Must be `'_'`.
        
3. **Relational Checks:**
    
    - **Index 3 == Index 10:** Since index 10 is `'_'`, index 3 must be **`_`**.
        
    - **Index 1 == Index 12:** Index 12 is the 'o' from the "gold" suffix. Thus, index 1 must be **`o`**.
        
    - **Index 5 == meatball[3]:** 'meatball'[3] is 't'. Result: **`t`**.
        
    - **Index 9 == monkey[3]:** 'monkey'[3] is 'k'. Result: **`k`**.
        
    - **Index 7 - Index 8 == 0x12 (18):** Index 7 is 'u' (ASCII 117). 117−18=99, which is the ASCII value for **`c`**. So index 8 is **`c`**.
|**Index**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Char**|y|o|u|_|s|t|?|u|c|k|_|g|o|l|d|