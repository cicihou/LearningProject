'''
题目地址（Shortest-Cycle-Containing-Target-Node）

https://binarysearch.com/problems/Shortest-Cycle-Containing-Target-Node
题目描述

You are given a two-dimensional list of integers graph representing a directed graph as an adjacency list. You are also given an integer target.
Return the length of a shortest cycle that contains target. If a solution does not exist, return -1.
Constraints
n, m ≤ 250 where n and m are the number of rows and columns in graph


答案：https://leetcode-solution.cn/solutionDetail?type=3&id=44&max_id=2

本题有一个隐含的条件 target < len(graph)

题目：返回存在 target 的最短的环

逆向一下，就是从 target 开始搜索，检测到的第一个环（最近的环）
'''
from collections import deque


class Solution:
    def solve(self, graph, target):
        '''
        返回存在 target 的最短的环
            逆向一下，就是从 target 开始搜索，检测到的第一个环（最近的环）
            我们把环先加入队列，然后开始遍历图
            层次遍历，每走完一层，level += 1，等 for loop 结束，target 还没找到，return -1
        '''
        q = deque([target])
        visited = set()
        steps = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        q.append(neighbor)
                    elif neighbor == target:
                        return steps + 1
            steps += 1
        return -1
