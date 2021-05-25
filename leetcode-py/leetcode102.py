# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        method 1 层序遍历，bfs
        '''
        # if not root: return []
        #
        # queue = [root]
        # res = []
        # while queue:
        #     tmp = []
        #     size = len(queue)
        #     for i in range(size):
        #         root = queue.pop(0)
        #         tmp.append(root)
        #         if root.left:
        #             queue.append(root.left)
        #         if root.right:
        #             queue.append(root.right)
        #     res.append(tmp)
        # return res

        '''
        method 2 dfs
        用 dfs 做需要稍加理解，这里有一张很好的图
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/die-dai-di-gui-duo-tu-yan-shi-102er-cha-shu-de-cen/
        
        递归时，会先遍历完左边的子树，再遍历右边的子树
        若   3
            / \
           5   7
          /   / \
         9   4   6
        这样一棵树，res 是先把左树遍历完毕，生成 形如 [[3], [5], [9]] 的结构
        再 遍历右树，append 右树的节点 [[3], [5,7], [9,4,6]]
        而 if len(res) < level: res.append([]) 这一步通常是在左树完成的
        '''
        if not root:
            return []

        res = []

        def dfs(level, root):
            # level 表示层
            if len(res) < level:
                res.append([])
            res[level - 1].append(root.val)
            if root.left:
                dfs(level + 1, root.left)
            if root.right:
                dfs(level + 1, root.right)

        dfs(1, root)
        return res
