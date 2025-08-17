class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    mp = {}
    cur = head
    while cur:
        mp[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        clone = mp[cur]
        clone.next = mp.get(cur.next)
        clone.random = mp.get(cur.random)
        cur = cur.next
    return mp[head]

if __name__ == "__main__":
    a = Node(7); b = Node(13); c = Node(11); d = Node(10); e = Node(1)
    a.next=b; b.next=c; c.next=d; d.next=e
    b.random=a; c.random=e; d.random=c; e.random=a
    cloned = copy_random_list(a)
    cur = cloned
    out = []
    while cur:
        out.append((cur.val, cur.random.val if cur.random else None))
        cur = cur.next
    print(out)
