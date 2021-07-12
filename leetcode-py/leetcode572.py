# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        '''
        method 1 由 lc101 改写，先遍历 root 所有节点，再判断 subRoot 是否和 root 中的某个节点相同
        :param root:
        :param subRoot:
        :return:
        '''
        res = {}

        def dfs(root):
            if not root:
                return
            res[root] = None
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        for tree in res:
            if isSameTree(tree, subRoot):
                return True
        return False

        '''
        method 2 
        由 method 1 简化而来，不再进行显式的遍历
        只是代码简化了，速度上没有提升，因为递归的层数没有减少
        
        only the code is simplified, the time complexity is not decreased
        '''

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        if not root:
            return False

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
