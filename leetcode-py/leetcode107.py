# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        '''
        lc 102 的逆序输出和打印

        method 1 BFS
        :param root:
        :return:
        '''
        q = [root]
        res = []
        while q:
            tmp = []
            size = len(q)
            for i in range(size):
                root = q.pop(0)
                if root:
                    tmp.append(root.val)
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
            if tmp:
                res.append(tmp)
        return res[::-1]


        '''
        method 2 DFS
        '''
        if not root:
            return []
        res = []

        def dfs(root, level):
            if len(res) < level:
                res.append([])
            if not root:
                return
            res[level - 1].append(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 1)
        return res[::-1]
