# Problem 2: Misère Nim (3 Heaps)

## Problem
Misère Nim game: player who takes the last stone loses. Given 3 heaps [a, b, c], determine if the first player has a forced win.

---

## Approach 1
- If all heaps are size 1 → First wins if heap count is even.  
- Else → use XOR rule.

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

---

## Approach 2
Generalized misère Nim function that works for n heaps.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)
