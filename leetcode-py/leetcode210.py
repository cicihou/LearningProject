import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        DFS + Topological Sort

        视频：https://www.youtube.com/watch?v=qe_pQCh09yU

        若存在环，返回 []；若不存在环，返回拓扑排序中的任意一种排列结果

        对于图中任意一个节点，在搜索过程中有且只有三种状态：
            a. 未搜索：我们还没有搜索到这个节点
            b. 搜索中：我们搜索过这个节点，但还没有回溯到该节点，i.e. 该节点还有相邻的节点没有搜索完成，因此还没有入栈
            c. 已完成：我们搜索并回溯过这个节点，即该节点已经入栈（并且所有该节点的相邻节点都出现在了栈中更底部的位置）

        解题步骤
        1. 将有向图遍历并存储 每门前课 对应了 哪些课程
        2. 将所有节点默认为没有搜索过，并建空栈
        3. 遍历每门课，如果当前无环，且节点没有被访问过，则访问节点
            3.1 将当前的节点标记成搜索中，并且遍历当前节点的全部前置课程
            3.2 若前置课程未访问过，则访问前置课程；并判断前置课程中是否有环，有的话直接返回
            3.3 若前置课程处于搜索中的状态，就说明成环了（不然前置课程如果有通向一条无环的路径，搜索会标记成已完成；）
            3.4 将前置课程的循环走完之后，当前节点标记为「已完成」，并添加进栈
        4. 判断图是否还有效，无环就可以返回stack[::-1]；存在环返回[]

        :param numCourses:
        :param prerequisites:
        :return:
        '''

        edges = collections.defaultdict(list)  # 存储有向图
        visited = [0] * numCourses  # 判断该节点有没有搜索过，0未搜索，1搜索中，2已完成
        res = list()  # stack

        self.valid = True

        for cur, pre in prerequisites:
            edges[pre].append(cur)  # key 是前置课程， value 是该前置课程对应了哪些课（哪些课需要上这门前置课才能上）

        def dfs(u: int):
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not self.valid:
                        return
                elif visited[v] == 1:  # 前置课已经搜索过，但又没有完成搜索，说明成环了
                    self.valid = False
                    return
            visited[u] = 2
            res.append(u)

        for i in range(numCourses):
            if self.valid and not visited[i]:
                dfs(i)

        return res[::-1] if self.valid else []

        '''
        method 2 BFS
        视频：https://www.youtube.com/watch?v=tggiFvaxjrY
        '''
