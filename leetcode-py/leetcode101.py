# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        跟 lc 100 一模一样，稍作修改

        DFS

        time: O(n), we traverse the entire input tree once
        space: O(n), The number of recursive calls is bound by the height of the tree.
                     In the worst case, the tree is linear and the height is in O(n).
        '''
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root, root)

        '''
        method 2 BFS
        本题用 BFS 简直是多此一举
        '''

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val

        queue = [(root, root)]

        while queue:
            p, q = queue.pop(0)
            if not isSameTree(p, q):
                return False
            if p:
                queue.append((p.left, q.right))
                queue.append((p.right, q.left))
        return True
