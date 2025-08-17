# Problem 2 – Word Search in 2D Matrix (Microsoft, Easy)

Check if a **word** exists either **left-to-right** in any row or **top-to-bottom** in any column.

### Approach — `solution_1.py`
- Join each row to a string and check substring.
- Build each column string and check substring.
- **Time:** O(M×N) | **Space:** O(1) extra (ignoring the joined strings).

### Difficulties Faced
- Handling uneven rows (we assume proper M×N grid).
- Ensuring only forward directions (no diagonal/backward).

### How to Run
```bash
python solution_1.py
```
