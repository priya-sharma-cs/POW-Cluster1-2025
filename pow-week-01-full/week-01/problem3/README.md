# Problem 3 – Equal Sum Partition (Facebook)

Determine if the array can be split into **two subsets with equal sum**.

### Approach (DP, 1D boolean) — `solution_1.py`
- If total sum is odd → immediately False.
- Target = sum/2. Use boolean DP of size `target+1`.
- For each number `num`, update from `target` down to `num`: `dp[j] |= dp[j-num]`.
- Answer is `dp[target]`.
- **Time:** O(N×target) | **Space:** O(target).

### Difficulties Faced
- Backward iteration in inner loop is crucial to avoid reusing the same element twice.
- Large target values can be slow; could optimize via bitset in Python (`int` bit tricks).

### How to Run
```bash
python solution_1.py
```
