# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        '''
        method 1 dfs inorder traversal + toBST
        :param root:
        :return:
        '''
        res = []

        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)

        dfs(root)

        def toBST(nums):
            if not nums:
                return
            mid = len(nums) // 2

            root = TreeNode(nums[mid])
            root.left = toBST(nums[:mid])
            root.right = toBST(nums[mid+1:])

            return root

        return toBST(res)
