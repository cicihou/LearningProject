# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        while root is not None:
            if root.left is None:
                root = root.right
                continue
            left = root.left
            while left.right is not None:
                left = left.right
            left.right = root.right
            root.right = root.left
            root.left = None
            root = root.right