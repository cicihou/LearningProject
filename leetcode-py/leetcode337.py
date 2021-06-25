# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        '''
        recursion
            将 抢该层和 不抢该层 得到的结果计算或返回，进行比较，取较大值
            本题无需 dp 即可完成
        '''
        def dfs(root):
            if not root:
                return (0, 0)
            left = dfs(root.left)
            right = dfs(root.right)

            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            return [rob, not_rob]

        return max(dfs(root))
