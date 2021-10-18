'''
解析：https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/shi-pin-jie-shi-di-gui-dai-ma-de-yun-xing-guo-chen/

一条路径(path)的长度为该路径经过的节点数减一，
所以求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一。

而任意一条路径均可以被看作由某个节点为起点，从其左儿子和右儿子向下遍历的路径拼接得到。

Note：
dfs 求 root 所对应的子树的最多节点数( 1 + max(l, r)，1 表示当前节点本身的节点数)
实质上一条路径所对应的节点数 - 1 就是这条路径的边长
最长的路径等于当前 root 左边的节点数量 + 右边的节点数量（左边和右边都会统计到 root 这个节点）
因此 l + r 相当于统计了两次 root，无需额外 -1 就是我们所需的路径边长

time: O(n), This is because in our recursion function longestPath, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.
space: O(n), The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(logN).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            self.res = max(self.res, l+r)
            return 1 + max(l, r)

        dfs(root)
        return self.res
