# Problem 5 – Flood Fill Algorithm (Facebook)

Change the color of a starting pixel and all **4-directionally connected** pixels with the same original color.

### Approach (DFS) — `solution_1.py`
- If the starting pixel already has the new color → return image.
- DFS from (sr, sc) and recolor neighbors with the same original color.
- **Time:** O(R×C) | **Space:** O(R×C) worst-case recursion.

### Difficulties Faced
- Avoid infinite loops by only visiting cells that match the **original** color.
- Stay within bounds and use 4-neighborhood only (no diagonals).

### How to Run
```bash
python solution_1.py
```
