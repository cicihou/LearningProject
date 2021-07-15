# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
递归判断 root 节点中是否含有 1

如果节点不存在，返回 False
判断节点的左右节点是否存在 1
    如果左节点不存在，将左节点置空
    如果右节点不存在，将右节点置空
返回当前节点的值是否为 1 或者左右节点的值是否含 1

time: O(N), the number of nodes in the tree
space: O(H), the height of the tree, i.e. the size of the implicit call stack in our recursion
'''
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        '''
        method 1 recursion
        '''
        def containsOne(root):
            if not root:
                return False

            left = containsOne(root.left)
            right = containsOne(root.right)

            if not left:
                root.left = None
            if not right:
                root.right = None

            return root.val == 1 or left or right

        return root if containsOne(root) else None


        '''
        shorter method
        '''
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            root = None

        return root
