class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    max_sum = float('-inf')

    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)

    helper(root)
    return max_sum
