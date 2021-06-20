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

        method 1 preorder traversal + update nodes
        """
        nodes = []
        def dfs(root):
            if root:
                nodes.append(root)
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        for i in range(1, len(nodes)):
            prev, cur = nodes[i-1], nodes[i]
            prev.left = None
            prev.right = cur


        '''
        method 2 preorder traversal and in-replace nodes at the same time
        '''
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
