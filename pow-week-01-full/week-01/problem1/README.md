# Problem 1 – Count Unival Subtrees (Google)

**Goal:** Count the number of subtrees where **all nodes share the same value**. A single node is unival.

### Approach 1 (Optimal, Post-order DFS) — `solution_1.py`
- Recurse on left and right first.
- A node is unival if both children are unival **and** their values (when present) match the node.
- Maintain a counter for every node that qualifies.
- **Time:** O(N) | **Space:** O(H) (recursion stack).

### Approach 2 (Naive, Educational) — `solution_2.py`
- For each node, check if its entire subtree has the same value.
- **Time:** O(N^2) worst case | **Space:** O(H).

### Difficulties Faced
- Ensuring **post-order** processing; otherwise parent decision is premature.
- Treating **None** as unival; forgetting this breaks counts.
- Carefully comparing child values to parent's value.

### How to Run
```bash
python solution_1.py
python solution_2.py   # optional
```

### Expected (Sample)
Sample tree in the file prints **5**.
