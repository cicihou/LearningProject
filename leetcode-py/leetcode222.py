# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        time O(n)
        :param root:
        :return:
        '''
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return 0

        '''
        binary search
        # TODO https://leetcode.com/problems/count-complete-tree-nodes/discuss/126600/Python-O(N)-and-O(log(n)-2)-solution-with-explanation
        '''
