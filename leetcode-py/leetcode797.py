'''
BFS
视频：https://www.youtube.com/watch?v=CYnvDzMprdc

本题题目中就已经要求了是 有 n 个结点的有向无环图

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1
'''

import collections


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        很经典的 回溯 问题
        graph 的结构就是 index - [index 对应的下个点]，i.e. index - graph[index] 就是 边
        路径只统计从开始走到结尾的路径（找到所有从 0 到 n-1 的路径并输出）
        本图无环
            1. 若 path 的最后一个点等于尾节点，输出一条有效的路径
            2. 当前 path 最后一个点不是尾节点，当前 path 最后一个点每一条边都需要创建一条新的路径添加进 queue

        :param graph:
        :return:
        '''
        res = []
        q = collections.deque([0])

        goal = len(graph) - 1

        while q:
            path = q.popleft()
            last_node = path[-1]

            if last_node == goal:
                res.append(path[:])
            else:
                cur = graph[last_node]
                for c in cur:
                    new_path = path[:]
                    new_path.append(c)
                    q.append(new_path)
        return res
