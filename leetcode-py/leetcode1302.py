# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        '''
        method 1 BFS
        :param root:
        :return:
        '''
        if not root:
            return []

        q = deque([root])

        while q:
            res = []
            size = len(q)

            for i in range(size):
                root = q.popleft()
                res.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return sum(res)

        '''
        method 2 DFS
        '''
        res = []

        def dfs(level, root):
            if len(res) < level:
                res.append([])
            if not root:
                return
            res[level - 1].append(root.val)
            if root.left:
                dfs(level + 1, root.left)
            if root.right:
                dfs(level + 1, root.right)

        dfs(1, root)
        return sum(res[-1])
