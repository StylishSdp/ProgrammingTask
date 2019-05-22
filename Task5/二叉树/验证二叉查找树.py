# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):

        def valid(root, min_val, max_val):
            if not root:
                return True

            if min_val is not None and root.val <= min_val:
                return False
            if max_val is not None and root.val >= max_val:
                return False

            return valid(root.left, min_val, root.val) and valid(root.right, root.val, max_val)

        return valid(root, None, None)