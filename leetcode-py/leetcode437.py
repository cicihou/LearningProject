# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        '''
        BF 解法
        题解：https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

        一个不错的 path sum 类型题的总结：https://leetcode-cn.com/problems/path-sum-iii/solution/yi-pian-wen-zhang-jie-jue-suo-you-er-cha-smch/
        '''
        self.res = 0

        def dfs(root, target):
            '''
            以 树 中的每个节点作为根节点，扫一遍以节点为根部，向下对应的 pathSum
            '''
            if not root:
                return
            helper(root, target)
            dfs(root.left, target)
            dfs(root.right, target)

        def helper(root, target):
            '''
            这个函数计算每个节点向下的路径和，如果碰到相等的，就 res += 1
            注意即使相等也并不需要提前退出，因为可能下面对应的子路径还有

            if root.val == target:
            注意这个判断的写法，如果写成 target == 0，就会漏掉叶子节点所在的路径
            （因为我们走到了叶子节点后，不会再进入这个递归的判断）
            '''
            if not root:
                return
            if root.val == target:
                self.res += 1

            helper(root.left, target - root.val)
            helper(root.right, target - root.val)

        dfs(root, targetSum)
        return self.res
