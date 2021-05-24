# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''method 1 recursion + dfs'''
    #     self.res = []
    #     self.dfs(root)
    #     return self.res
    #
    # def dfs(self, root):
    #     if root:
    #         self.dfs(root.left)
    #         self.res.append(root.val)
    #         self.dfs(root.right)

        ''' method 2 bfs
        跟 144 同理，由于 stack FILO
        先往 stack 里面压需要后处理的 root.right
        再往 stack 里面压需要先处理的 root.left
        '''
        if not root: return []
        res = []
        stack = [(0, root)]
        while stack:
            color, root = stack.pop()
            if not root:
                continue
            if not color:
                stack.append((0, root.right))
                stack.append((1, root))
                stack.append((0, root.left))
            else:
                res.append(root.val)
        return res
