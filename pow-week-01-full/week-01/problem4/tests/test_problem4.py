from solution_1 import Node, copy_random_list
from solution_2 import Node as Node2, copy_random_list_interleaved

def build_sample():
    a = Node(7); b = Node(13); c = Node(11); d = Node(10); e = Node(1)
    a.next=b; b.next=c; c.next=d; d.next=e
    b.random=a; c.random=e; d.random=c; e.random=a
    return a

def test_clone_preserves_structure():
    head = build_sample()
    cloned = copy_random_list(head)
    cur1, cur2 = head, cloned
    for _ in range(5):
        assert cur1.val == cur2.val
        r1 = cur1.random.val if cur1.random else None
        r2 = cur2.random.val if cur2.random else None
        assert r1 == r2
        cur1 = cur1.next
        cur2 = cur2.next

def test_clone_o1_space_variant():
    from solution_2 import copy_random_list_interleaved as f
    head = build_sample()
    cloned = f(head)
    cur = cloned
    vals = []
    while cur:
        vals.append(cur.val)
        cur = cur.next
    assert vals == [7,13,11,10,1]
