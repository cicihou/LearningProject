# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''

        method 1
        用了 backtrack 的思想，跟 113 一模一样
        不过我们只要得到了有效的 path，就可以提前进行返回了
        '''
        res = []
        path = []
        def backtrack(path, root, targetSum):
            if res:
                return True
            if root:
                targetSum -= root.val
                path.append(root.val)
                if not root.left and not root.right and targetSum==0:
                    res.append(path[:])
                backtrack(path, root.left, targetSum)
                backtrack(path, root.right, targetSum)
                path.pop()
        backtrack(path, root, targetSum)
        return len(res) > 0

        '''
        method 2
        dfs，no need to backtrack
        '''
        def dfs(root, target):
            if root:
                target -= root.val
                if not root.left and not root.right:
                    return target == 0
                return dfs(root.left, target) or dfs(root.right, target)
        return dfs(root, targetSum)
