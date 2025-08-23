import solution1, solution2

def test():
    root = solution1.TreeNode(-10)
    root.left = solution1.TreeNode(9)
    root.right = solution1.TreeNode(20)
    root.right.left = solution1.TreeNode(15)
    root.right.right = solution1.TreeNode(7)
    assert solution1.maxPathSum(root) == 42

    root2 = solution2.TreeNode(-10)
    root2.left = solution2.TreeNode(9)
    root2.right = solution2.TreeNode(20)
    root2.right.left = solution2.TreeNode(15)
    root2.right.right = solution2.TreeNode(7)
    assert solution2.maxPathSum(root2) == 42

    print("All tests passed.")

if __name__ == "__main__":
    test()
