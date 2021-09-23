# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        '''method1
        dfs，用每一个高位的数乘10，再和下一层的节点相加，每次都计算左右。结果累加

        time: O(N), since one has to visit each node
        space: O(H), up to O(H) to keep the stack, H is tree height
        '''
        def dfs(root, val):
            if not root:
                return 0
            if not root.left and not root.right:
                return val * 10 + root.val
            left = dfs(root.left, val*10+root.val)
            right = dfs(root.right, val*10+root.val)
            return left + right

        return dfs(root, 0)

        '''method2
        BFS solution
        思想都是累加，当一个节点为叶子节点的时候，res+= value。
        非叶子节点的时候，不断向下找叶子节点
        
        time: O(N)
        space: O(H)
        '''
        if not root:
            return 0
        stack = [(root, root.val)]
        res = 0
        while stack:
            root, s=stack.pop()
            if not root.left and not root.right:
                res += s
            if root.left:
                stack.append((root.left, s*10+root.left.val))
            if root.right:
                stack.append((root.right, s*10+root.right.val))
        return res
