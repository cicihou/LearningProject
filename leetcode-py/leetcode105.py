# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
前序遍历的特性，根、左、右
中序遍历的特性，左、根、右
因此可以根据 根root 所在的位置，判断出整个二叉树一共有多少个左节点和右节点
这样将一个大问题就分成两个子问题了
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
