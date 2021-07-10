"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''
        method 1 DFS
        :param root:
        :return:
        '''
        res = []
        def dfs(root):
            if root:
                for child in root.children:
                    dfs(child)
                res.append(root.val)
        dfs(root)
        return res

        '''
        method 2 BFS
        '''
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.extend(root.children)
        return res[::-1]
