"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        method 1
        N 叉树层序遍历，根据 102 改写
        :param root:
        :return:
        '''
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            tmp = []
            size = len(q)
            for i in range(size):
                root = q.popleft()
                tmp.append(root.val)
                if root.children:
                    for child in root.children:
                        q.append(child)
            res.append(tmp)
        return res

        '''
        method 2 DFS
        根据 lc 102 改写
        '''
        if not root:
            return []

        res = []

        def dfs(root, level):
            if len(res) < level:
                res.append([])
            res[level - 1].append(root.val)
            for child in root.children:
                dfs(child, level + 1)

        dfs(root, 1)
        return res
