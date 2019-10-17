# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''try'''
        # if not root:
        #     return 0
        # data = []
        # def preorder(root):
        #     if root == None:
        #         return
        #     data.append(root.val)
        #     preorder(root.left) if root.left else preorder(root.right)
        # data += ''.join(data)

        '''method1 '''
        # 递归，用每一个高位的书乘10，再和下一层的节点相加，每次都计算左右。结果累加
    #     self.res = 0
    #     self.dfs(root, 0)
    #     return self.res
    #
    # def dfs(self, root, value):
    #     if root:
    #         self.dfs(root.left, value*10 + root.val)
    #         self.dfs(root.right, value*10 + root.val)
    #         if not root.left and not root.right:
    #             self.res += value*10 +root.val

        '''method2'''
        # 思想都是累加，当一个节点为叶子节点的时候，res+= value。非叶子节点的时候，不断向下找叶子节点
        # if not root:
        #     return 0
        # stack = [(root, root.val)]
        # res = 0
        # while stack:
        #     root, s=stack.pop()
        #     if not root.left and not root.right:
        #         res += s
        #     if root.left:
        #         stack.append((root.left, s*10+root.left.val))
        #     if root.right:
        #         stack.append((root.right, s*10+root.right.val))
        # return res

        '''method3'''
        # java改的
        return 0 if not root else self.sum_nums(root, 0)

    def sum_nums(self, root, n):
        if not root.left and not root.right:
            return 10 * n + root.val
        res = 0
        if root.left:
            res += self.sum_nums(root.left, 10*n + root.val)
        if root.right:
            res += self.sum_nums(root.right, 10*n + root.val)
        return res



s = Solution()
s.sumNumbers([1,2,3])
s.sumNumbers([4,9,0,5,1])
