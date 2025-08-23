# Problem 1: Minimum Number of Perfect Squares to Sum to N

## Problem
You are given a positive integer `n`. Find the minimum number of perfect square numbers that sum exactly to `n`.

---

## Approach 1: Dynamic Programming
- dp[i] = minimum number of squares to sum to i.
- Transition: dp[i] = min(dp[i - j*j] + 1) for all j*j ≤ i.

**Time Complexity:** O(n * sqrt(n))  
**Space Complexity:** O(n)

---

## Approach 2: BFS
- Model problem as shortest path search.
- Subtract squares until reaching 0.

**Time Complexity:** O(n * sqrt(n))  
**Space Complexity:** O(n)
