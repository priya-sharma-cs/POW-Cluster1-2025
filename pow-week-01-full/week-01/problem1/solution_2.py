class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_all_equal(node, target):
    if node is None:
        return True
    if node.val != target:
        return False
    return is_all_equal(node.left, target) and is_all_equal(node.right)

def count_unival_subtrees_naive(root):
    def traverse(node):
        if node is None:
            return 0
        here = 1 if is_all_equal(node, node.val) else 0
        return here + traverse(node.left) + traverse(node.right)
    return traverse(root)

def build_sample_tree():
    return Node(0,
                Node(1),
                Node(0,
                     Node(1, Node(1), Node(1)),
                     Node(0)))

if __name__ == "__main__":
    root = build_sample_tree()
    print(count_unival_subtrees_naive(root))  # 5
