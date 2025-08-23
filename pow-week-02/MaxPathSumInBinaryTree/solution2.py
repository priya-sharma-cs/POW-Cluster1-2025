class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    res = [float('-inf')]

    def dfs(node):
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        res[0] = max(res[0], node.val + left + right)
        return node.val + max(left, right)

    dfs(root)
    return res[0]
