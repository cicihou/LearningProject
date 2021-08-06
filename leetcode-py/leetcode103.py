# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        method 1 DFS
        :param root:
        :return:
        '''
        res = []
        def dfs(root, level):
            if root:
                if len(res) < level:
                    res.append([])
                res[level-1].append(root.val)
                dfs(root.left, level+1)
                dfs(root.right, level+1)
        dfs(root, 1)
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res

        '''
        method 2 BFS
        '''
        res = []
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                root = q.pop(0)
                if root:
                    level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            if level:
                res.append(level)
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res
