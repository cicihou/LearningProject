class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        DFS
        https://www.youtube.com/watch?v=EgI5nU9etnU

        其实就找一个长度为 n 的 无环路径，找到就是 True，找不到就是 False

        :param numCourses:
        :param prerequisites:
        :return:
        '''
        preMap = {i: [] for i in range(numCourses)}
        prerequisites.sort()
        for course, pre in prerequisites:
            preMap.setdefault(course, []).append(pre)

        # all courses along the cur DFS path
        visited = set()

        def dfs(course):
            '''
            是否 无环，若是，返回 True，若否，返回 False
            :param course:
            :return:

            关于为什么要额外写一个 preMap[course] = []
            比如我上一把 premap {1: [2,3], 2: [3,4] ...}
            已经计算过 2 是不不会产生环的点，那就将 2 直接标记成 []，不然 走到 1 时，它又会把 2 对应的点又算一遍
            '''
            if course in visited:
                return False
            if preMap.get(course, []) == []:
                return True
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            # 这里如果不加这一行就会 TLE, 这里相当于把可以无环的点变成入度为 0 了
            # 不加这行代码，就需要记录一下每个点是否能够无环这样的信息，否则时间复杂度就是平方
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        '''
        method 2 BFS 
        BFS 思考起来 跟 DFS 完全相反
        '''
        # TODO
