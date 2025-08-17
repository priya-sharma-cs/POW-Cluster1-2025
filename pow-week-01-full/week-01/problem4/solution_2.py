class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list_interleaved(head):
    if not head:
        return None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = Node(cur.val, nxt, None)
        cur = nxt
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur = head
    new_head = head.next
    while cur:
        clone = cur.next
        cur.next = clone.next
        clone.next = clone.next.next if clone.next else None
        cur = cur.next
    return new_head

if __name__ == "__main__":
    a = Node(7); b = Node(13); c = Node(11); d = Node(10); e = Node(1)
    a.next=b; b.next=c; c.next=d; d.next=e
    b.random=a; c.random=e; d.random=c; e.random=a
    cloned = copy_random_list_interleaved(a)
    cur = cloned
    out = []
    while cur:
        out.append((cur.val, cur.random.val if cur.random else None))
        cur = cur.next
    print(out)
