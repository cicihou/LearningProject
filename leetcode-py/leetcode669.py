# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        '''
        这是一棵 BST(Binary Search Tree)
            当 node.val > R，那么修剪后的二叉树必定出现在节点的左边。(因为 node 右子树的值都会大于当前 node.va，所以没必要考虑右子树)
            类似地，当 node.val < L，那么修剪后的二叉树出现在节点的右边。(因为 node 左子树的值都会小于当前 node.va，所以没必要考虑左子树)
        否则，我们将会修剪树的两边。

        case [5,2,6,0,3,null,7,null,null,null,4], 3, 5 可以用了画图帮助理解

        time: O(N)
        space: O(N)
        '''

        def trim(root):
            if not root:
                return None
            elif root.val > high:
                return trim(root.left)
            elif root.val < low:
                return trim(root.right)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
                return root

        return trim(root)
