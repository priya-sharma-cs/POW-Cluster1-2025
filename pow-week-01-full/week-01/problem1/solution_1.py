class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    count = 0
    def is_unival(node):
        nonlocal count
        if node is None:
            return True
        left_ok = is_unival(node.left)
        right_ok = is_unival(node.right)
        if not (left_ok and right_ok):
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        count += 1
        return True
    is_unival(root)
    return count

def build_sample_tree():
    #       0
    #      / \\
    #     1   0
    #        / \\
    #       1   0
    #      / \\
    #     1   1
    return Node(0,
                Node(1),
                Node(0,
                     Node(1, Node(1), Node(1)),
                     Node(0)))

if __name__ == "__main__":
    root = build_sample_tree()
    print(count_unival_subtrees(root))  # 5
