# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []

        while level:
            depth += 1
            queue = []
            for l in level:
                if l.left:
                    queue.append(l.left)
                if l.right:
                    queue.append(l.right)
            level = queue

        return depth