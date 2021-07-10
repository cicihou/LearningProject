"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        method 1 DFS
        :param root:
        :return:
        '''
        res = []

        def dfs(root):
            if root:
                res.append(root.val)
                for child in root.children:
                    dfs(child)

        dfs(root)
        return res

        '''
        method 2 BFS
        
        preorder 要求根左右
        BFS 要将N叉树的末尾放到栈的最底部，最后处理N叉树的尾
        '''
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                for child in root.children[::-1]:
                    stack.append(child)
        return res
