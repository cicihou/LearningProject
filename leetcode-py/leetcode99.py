# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        还有更加节约的方法
        可参考题解：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/san-chong-jie-fa-xiang-xi-tu-jie-99-hui-fu-er-cha-/

        time: O(n)
        space: O(n)
        """
        nodes = []
        def dfs(root):
            if root:
                dfs(root.left)
                nodes.append(root)
                dfs(root.right)
        dfs(root)

        err1 = err2 = None
        for i in range(1, len(nodes)):
            # 这里有点微妙，需要想一想，先用 err2 记录第一个错误（必然是更大的那个数，会落在 i-1 上）
            # 再用 err1 记录第二个错误（更小的那个数，会落在 i 上）
            if nodes[i-1].val > nodes[i].val:
                err1 = nodes[i]
                if not err2:
                    err2 = nodes[i-1]
        if err1 and err2:
            err1.val, err2.val = err2.val, err1.val
