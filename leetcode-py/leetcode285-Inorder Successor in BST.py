# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = []

        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root)
                dfs(root.right)

        dfs(root)

        for i in range(1, len(res)):
            if p.val < res[i].val:
                return res[i]
