# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ''' method 1
        BFS Solution
        由于 stack FILO
        先往 stack 里面压需要后处理的 root.right
        再往 stack 里面压需要先处理的 root.left
        '''
        # if not root:
        #     return []
        # stack = [root]
        # res = []
        # while stack:
        #     root = stack.pop()
        #     if root:
        #         res.append(root.val)
        #         stack.append(root.right)
        #         stack.append(root.left)
        # return res


        '''
        method 2
        recursion
        '''
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        # 这里需要特别注意，lc 的 input 显式的输入了 None 值
        # 但其实 那些 null 是空节点，既没有值，也没有引用，只是为了在二叉树占位表示树的结构
        # dfs + recursion
        if root:
            self.res.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)
