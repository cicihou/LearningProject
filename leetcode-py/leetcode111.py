# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        跟 lc 104 高度相似，改一改
        注意：当 min(l, r) 为 0 时，说明根的左子树或右子树没有叶子结点，与题意要求的不符，不能直接返回根的层级
        还有个要注意的点就是运算符优先级，min(l, r) or max(l, r) 是我们优先级最高的判断，必须用括号括起来以免曲解意思
        '''
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + (min(l, r) or max(l, r))
