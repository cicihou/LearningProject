'''
任意给出一棵二叉树的两个结点，
路径指的是：分别从这两个结点向上走，找到 最近的公共祖先 结点而形成的路径。
只有这样的定义下，路径才是唯一确定的。

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

1. 递归计算左右节点的最大贡献值，只有在最大贡献值大于 0 时，才会选取对应的节点
2. 节点的最大路径和为 root.val + left + right
3. res = max(res, 节点最大路径和)
4. 返回节点的最大贡献值（由于这个节点能贡献的最大值，只能选择左右子树中的某一条路径，不能同时选择两个）
    root.val + max(left, right)

time: O(N)
space: O(N)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global res
        res = float('-inf')

        def dfs(root):
            if not root:
                return 0


            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            global res
            res = max(res, root.val+left+right)

            return root.val + max(left, right)

        dfs(root)
        return res
