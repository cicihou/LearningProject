# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        cache = {}
        self.res = False

        def dfs(root):
            if root:
                if root.val in cache:
                    self.res = True
                if self.res: return
                cache[k - root.val] = None
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return self.res
