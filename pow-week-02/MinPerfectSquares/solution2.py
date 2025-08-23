# BFS approach
from collections import deque

def numSquares(n: int) -> int:
    q = deque([(n, 0)])
    visited = set([n])
    while q:
        remainder, steps = q.popleft()
        if remainder == 0:
            return steps
        j = 1
        while j * j <= remainder:
            nxt = remainder - j * j
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))
            j += 1
    return -1
