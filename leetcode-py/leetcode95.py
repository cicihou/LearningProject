# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        跟 lc 96 相似，不过这里要利用回溯生成具体的树

        生成一棵符合 BST 的树
            1. 当前的节点是 i，当前节点的左子树生成对应 (start, i-1)，当前节点的右子树生成对应 (i+1, end)
            2. 遍历左子树和右子树（两层循环），将其赋值到当前 node 的左右
            3. 将当前节点添加到 res 中
        :param n:
        :return:
        '''
        def generateTree(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                ls = generateTree(start, i-1)
                rs = generateTree(i+1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res

        return generateTree(1, n)
