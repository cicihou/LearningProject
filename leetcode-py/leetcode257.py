# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        '''
        lc 113 的变种题
        :param root:
        :return:
        '''
        res = []
        def backtrack(root, path):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    res.append(path[:])
                backtrack(root.left, path)
                backtrack(root.right, path)
                path.pop()
        backtrack(root, [])
        for i in range(len(res)):
            res[i] = '->'.join([str(integer) for integer in res[i]])
        return res
