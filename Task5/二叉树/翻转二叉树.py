# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        # 直接交换节点
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root