# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        method 1 DFS + recursion
        '''
        if not root:
            return True
        if abs(self.dfs(root.right) - self.dfs(root.left)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return 1 + max(l, r)
