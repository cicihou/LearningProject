"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

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
            if level:
                if len(level) > 1:
                    for i in range(1, len(level)):
                        level[i-1].next = level[i]
        return cur

        '''
        method 2 BFS
        '''
        if not root:
            return root
        q = deque([root])
        cur = root
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                root = q.popleft()
                level.append(root)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            for i in range(1, len(level)):
                level[i-1].next = level[i]
        return cur
