# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        '''
        method 1 bfs
        这道题是 102 的变种，
        用层序遍历做即可

        注意：这道题并不需要维护 res, 只维护 tmp ，留下的最后一个 tmp 就是我们要的最后一层
        代码这样写，是为了便于我们理解

        复杂度分析
        时间复杂度：O(N)，其中 N 为树的节点数。
        空间复杂度：O(Q)，其中 Q 为队列长度，最坏的情况是满二叉树，此时和 N 同阶，其中 N 为树的节点总数
        '''
        # queue = [root]
        # res = []
        # while queue:
        #     size = len(queue)
        #     tmp = []
        #     for i in range(size):
        #         root = queue.pop(0)
        #         tmp.append(root)
        #         if root.left:
        #             queue.append(root.left)
        #         if root.right:
        #             queue.append(root.right)
        #     res.append(tmp)
        # return res[-1][0].val


        '''
        method 2
        dfs + recursion
        这一题 跟 102 的 method 2 相似，
        由于 dfs 从左子树开始，因此第一个满足 level > max_level 的值，必然是最下面一层的左子树
        
        注意，这里的 root 的初始 level 设为 0 层 和设为 1 层都可以
        由于 level > self.max_level 的判断特性，都可以得到正确的值
        '''

        self.res = root.val
        self.max_level = 0

        def dfs(root, level):
            if not root:
                return

            if level > self.max_level:
                self.max_level = level
                self.res = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 1)
        return self.res
