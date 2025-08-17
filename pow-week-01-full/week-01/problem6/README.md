# Problem 6 – GCD of N Numbers (Amazon)

Compute the **greatest common divisor** of N integers.

### Approach — `solution_1.py`
- Use Euclidean algorithm and reduce across the list: `gcd = gcd(gcd, x)`.
- **Time:** O(N log M) where M is the max value | **Space:** O(1).

### Difficulties Faced
- Handling zeros (gcd(a, 0) = |a|).
- Large input lists—iterative reduce avoids recursion depth issues.

### How to Run
```bash
python solution_1.py
```
