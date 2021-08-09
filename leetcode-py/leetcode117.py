"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        method 1 DFS
        :param root:
        :return:
        '''
        res = []
        def dfs(root, level):
            if len(res) < level:
                res.append([])
            if root:
                res[level-1].append(root)
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        cur = root
        dfs(root, 1)
        for level in res:
            for i in range(1, len(level)):
                level[i-1].next = level[i]
        return cur

        '''
        method 2 BFS
        :param root: 
        :return: 
        '''
        q = deque([root])
        cur = root
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                root = q.popleft()
                if root:
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
                    if level:
                        last = level.pop()
                        last.next = root
                    level.append(root)
        return cur
