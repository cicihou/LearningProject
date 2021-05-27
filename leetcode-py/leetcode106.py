# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
跟 105 相同的思想

中序遍历：左根右
后序遍历：左右根


其实目前使用的这种方法效率并不好
比较理想的方式是传递节点位置，recursion 的时候不带列表，只带 index 参数
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/758662/Python-O(n)-recursion-explained-with-diagram

或者将 index 记录在 dict 中
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.

# TODO
method 2 只传递 index 的写法

'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
