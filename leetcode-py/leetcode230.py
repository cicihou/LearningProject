# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ''' 利用 BST 在中序遍历的特点
        DFS
        '''
        nodes = []
        def dfs(root):
            if root:
                dfs(root.left)
                nodes.append(root.val)
                dfs(root.right)
        dfs(root)
        return nodes[k-1]

        '''
        BFS
        '''
        stack = [(0, root)]
        res = []
        while stack:
            color, root = stack.pop()
            if color:
                res.append(root.val)
            else:
                if root:
                    stack.append((0, root.right))
                    stack.append((1, root))
                    stack.append((0, root.left))
        return res[k-1]
