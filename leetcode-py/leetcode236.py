# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        当前的树是否包含 p 或 q 子节点
        如果包含，返回 True，如果不包含返回 False
            如果当前的 root/左子树/右子树 包含超过 p 和 q（True 的数量超过 2 个）
            将 ans 更新为当前的根，因为当前的根必定是 lowestCommonAncestor
        '''
        self.ans = root

        def lca(root):
            if not root:
                return False
            left = lca(root.left)
            right = lca(root.right)

            mid = root == p or root == q

            if mid + left + right >= 2:
                self.ans = root

            return mid or left or right

        lca(root)
        return self.ans
