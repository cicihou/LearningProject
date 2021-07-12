# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        '''
        method 1 BFS
        :param root:
        :return:
        '''
        q = [root]
        uni = root.val
        while q:
            root = q.pop(0)

            if root.val != uni:
                return False
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        return True

        '''
        method 2 DFS
        '''
        res = set()
        def dfs(root):
            if root:
                res.add(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return len(res) == 1
