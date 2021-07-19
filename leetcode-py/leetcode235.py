# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        method 1 跟 LC 236 一模一样
        '''
        self.ans = root

        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)

            mid = root == p or root == q
            if mid + left + right >= 2:
                self.ans = root

            return mid or left or right

        dfs(root)
        return self.ans

        '''
        method 2 利用 BST 的特性，节约查找
            当 p 和 q 的 val 都 大于 root.val 时，查找 root.right
            当 p 和 q 的 val 都 小于 root.val 时，查找 root.left
            否则，表明 root 就是 p 和 q 的根节点
        '''
        def dfs(root):
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
        return dfs(root)
