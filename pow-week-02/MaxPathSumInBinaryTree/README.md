# Problem 3: Maximum Path Sum in Binary Tree

## Problem
Given a binary tree, find the maximum path sum between any two nodes. Path does not need to pass through the root.

---

## Approach 1
Recursive DFS with global variable.  
At each node:
- Compute max path including one child.
- Update global maximum with node + left + right.

**Time Complexity:** O(N)  
**Space Complexity:** O(H)

---

## Approach 2
Same logic, cleaner implementation using a result list.

**Time Complexity:** O(N)  
**Space Complexity:** O(H)
