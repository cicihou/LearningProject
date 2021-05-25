# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
注意 BST 有几个重要的性质：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

所以二叉搜索树的右子树所有的节点都会大于 root，左子树所有的节点都会小于 root
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        method 1
        BST Binary Search Tree 的 中序遍历 inorder traversal is ordered
        BST 的中序遍历如果是有序数组，则判断其是 BST，否则就不是
        :param root:
        :return:
        '''
    #     self.res = []
    #     self.dfs(root)
    #
    #     for i in range(1, len(self.res)):
    #         if self.res[i].val <= self.res[i - 1].val:
    #             return False
    #     return True
    #
    # def dfs(self, root):
    #     if root:
    #         self.dfs(root.left)
    #         self.res.append(root)
    #         self.dfs(root.right)


        '''
        method 2
        BFS + stack，中序遍历
        '''
        # stack = [(0, root)]
        # res = []
        # while stack:
        #     flag, root = stack.pop()
        #     if flag:
        #         res.append(root)
        #     else:
        #         if root.right:
        #             stack.append((0, root.right))
        #         stack.append((1, root))
        #         if root.left:
        #             stack.append((0, root.left))
        # for i in range(1, len(res)):
        #     if res[i].val <= res[i - 1].val:
        #         return False
        # return True


        '''
        method 3 
        只递归的比较值，不占用空间存储二叉树遍历的值
        https://leetcode.com/problems/validate-binary-search-tree/discuss/146601/Python3-100-using-easy-recursion
        https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution
        '''
        return self.check_bst(root, float('-inf'), float('inf'))

    def check_bst(self, root, left, right):
        if not root:
            return True

        if not left < root.val < right:
            return False

        return self.check_bst(root.left, left, root.val) and \
               self.check_bst(root.right, root.val, right)
