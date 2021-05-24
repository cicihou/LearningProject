# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ''' method 1 dfs + recursion'''
    #     self.res = []
    #     self.dfs(root)
    #     return self.res
    #
    # def dfs(self, root):
    #     if root:
    #         self.dfs(root.left)
    #         self.dfs(root.right)
    #         self.res.append(root.val)

        ''' method 2 bfs + stack'''
        if not root: return []
        res = []
        stack = [(0, root)]
        while stack:
            color, root = stack.pop()
            if not root:
                continue
            if not color:
                stack.append((1, root))
                stack.append((0, root.right))
                stack.append((0, root.left))
            else:
                res.append(root.val)
        return res
