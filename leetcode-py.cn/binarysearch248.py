'''
题目地址（Top-View-of-a-Tree）
https://binarysearch.com/problems/Top-View-of-a-Tree

题目描述
Given a binary tree root, return the top view of the tree, sorted left-to-right.

Constraints
n ≤ 100,000 where n is the number of nodes in root


这道题跟 leetcode 上的 987 计算思想相似：https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

本题记录 横坐标位置，如果横坐标位置已经在 seen 中，节点就不再添加进来
本题由于是自顶向下来看树的节点，需要且必须用层序遍历（见 leetcode 102），i.e. 当前层先添加，再添加下一层

总之就是 leetcode 102 + 987
'''
from collections import deque


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        '''
        method 1
        DFS 层序遍历
        '''
        seen = {}
        res = []

        def dfs(level, root, x):
            # 当前层不存在，或 当前节点的层 比seen 已存在的层数更小（更上层）的时候，替换节点
            if not x in seen or level < seen[x][1]:
                seen[x] = (root.val, level)
            if root.left:
                dfs(level + 1, root.left, x - 1)
            if root.right:
                dfs(level + 1, root.right, x + 1)

        dfs(1, root, 0)
        for k in sorted(seen):
            res.append(seen[k][0])
        return res


        '''
        method 2
        BFS 层序遍历
        时间复杂度：O（nlogn），注意这里的时间复杂度主要是落在 return 的那个排序上，python 中的 sorted 内置排序就是 O(nlogn)
        空间复杂度：O (n)
        '''
        q = deque([(root, 0)])
        seen = {}
        while q:
            root, x = q.popleft()
            if x not in seen:
                seen[x] = root.val
            if root.left:
                q.append((root.left, x - 1))
            if root.right:
                q.append((root.right, x + 1))
        return [seen[k] for k in sorted(seen)]
