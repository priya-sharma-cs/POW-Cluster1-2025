# Problem 4 – Deep Clone Linked List with Random Pointer (Snapchat)

Clone a linked list where each node has `next` and `random` pointers.

### Approach 1 (Hash Map) — `solution_1.py`
- First pass: create clone for each original node and store in a map.
- Second pass: wire `next` and `random` using the map.
- **Time:** O(N) | **Space:** O(N).

### Approach 2 (O(1) extra space, Interleaving) — `solution_2.py`
- Interleave cloned nodes in-between original nodes.
- Set random pointers, then detangle into two lists.
- **Time:** O(N) | **Space:** O(1) extra.

### Difficulties Faced
- Ensuring random pointers of clones point to **clone** of target, not original.
- Correctly separating interleaved list without breaking `next` chains.

### How to Run
```bash
python solution_1.py
python solution_2.py
```
