# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
这一题跟 105/106 相似

pre 前序遍历：根左右
post 后序遍历：左右根

构建二叉树，实质上就是要确定左子树和右子树

pre[0] 和 post[-1] 就是二叉树的根
pre[1] 是左二叉树的根，pre[1] 在 post 的位置，就是左右二叉树的分界

由于这种解法要求访问 pre 的第二个节点，pre[1]
因此在 pre 长度为 1 的时候，需要直接将节点返回，避免 index out of range
'''


class Solution:
    def constructFromPrePost(self, pre: list[int], post: list[int]) -> TreeNode:
        if not (pre and post):
            return

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:i+2], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+2:], post[i+1:-1])
        return root
