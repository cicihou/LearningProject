# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        '''
        If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

        very concise and brilliant answer:
        https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/496700/Python3-a-concise-recursive-solution

        为防止结果过大，题目要求进行 10^9 +7 的 module
        '''
        res = []
        def dfs(root):
            if not root:
                return 0
            ans = root.val + dfs(root.left) + dfs(root.right)
            res.append(ans)
            return ans

        total = dfs(root)
        return max([(total-x)*x for x in res]) % (10**9+7)
