# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        '''
        用了回溯的思想，先尝试暴力枚举所有答案，在结果不满足条件的时候取消前1或n步的计算

        其中 N 是树的节点数。
        time：O(N^2)，最坏情况下就是完全二叉树的每一条路径都符合要求。
        space: O(N)，空间复杂度主要取决于栈空间的开销，栈中的元素个数不会超过树的节点数。
        关于 time complexity 可参考：https://leetcode-cn.com/problems/path-sum-ii/solution/lu-jing-zong-he-ii-by-leetcode-solution/

        注意这道题是求 根节点到叶子结点的路径之和，当还未到达叶子节点的时候，即时得到了符合条件的 TargetSUM 也不能作为答案
        backtrack 中不需要判断 target 的大小，我们最终判断的是根到叶子结点的距离是否符合 targetSum
        回溯剪枝需要格外小心，提前return 可能会扰乱状态空间
        '''

        res = []
        path = []

        def backtrack(path, root, targetSum):
            if root:
                path.append(root.val)
                targetSum -= root.val
                if not root.left and not root.right and targetSum == 0:
                    res.append(path[:])
                backtrack(path, root.left, targetSum)
                backtrack(path, root.right, targetSum)
                path.pop()  # 回溯很重要的一个点：状态撤销
        backtrack(path, root, targetSum)
        return res
