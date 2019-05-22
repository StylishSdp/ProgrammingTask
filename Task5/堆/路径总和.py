# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):

        def func(node, sum):
            if not node:
                return False
            if node.left is None and node.right is None and node.val == sum:
                return True
            sum = sum - node.val
            return func(node.left, sum) or func(node.right, sum)

        return func(root, sum)