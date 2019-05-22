# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
    def maxDepth1(self, root):
        if not root:
            return 0

        left = self.maxDepth1(root.left)
        right = self.maxDepth1(root.right)

        return max(left, right) + 1

    #层序遍历，记录层数
    def maxDepth2(self, root):
        depth = 0
        if not root:
            return depth

        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            depth  += 1
        return depth