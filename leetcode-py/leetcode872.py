# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        '''
        method 1
        lc 145 后序遍历修改而来

        post-order traverse tree
        左右根

        DFS
        '''
        res1 = []
        res2 = []

        def dfs(root, res):
            if root:
                dfs(root.left, res)
                dfs(root.right, res)
                if not root.left and not root.right:
                    res.append(root.val)

        dfs(root1, res1)
        dfs(root2, res2)

        if len(res1) != len(res2):
            return False
        for i, j in zip(res1, res2):
            if i != j:
                return False
        return True

        '''
        method 2
        BFS
        '''

        def bfs(root):
            res = []
            stack = [(0, root)]
            while stack:
                color, root = stack.pop()
                if root:
                    if color and not any([root.left, root.right]):
                        res.append(root.val)
                    elif not color:
                        stack.append((1, root))
                        stack.append((0, root.right))
                        stack.append((0, root.left))
            return res

        res1 = bfs(root1)
        res2 = bfs(root2)

        if len(res1) != len(res2):
            return False
        for i, j in zip(res1, res2):
            if i != j:
                return False
        return True
