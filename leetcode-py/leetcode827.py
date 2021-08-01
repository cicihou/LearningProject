class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        method 1
        DFS 根据 695 来写，会超时 TLE

        time: O(N^4)
        space: O(N^2)

        :param grid:
        :return:
        '''
        n = len(grid)
        visited = set()

        def dfs(x, y):
            count = 0
            if 0 <= x < n and 0 <= y < n:
                if grid[x][y] == 1 and (x, y) not in visited:
                    visited.add((x, y))
                    count += 1
                    return count + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
            return 0

        res = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    visited = set()
                    res = max(res, dfs(x, y))
                    grid[x][y] = 0
        return n * n if res == 0 else res

        '''
        method 2 
        根据 method 1，以连通块来记录每个坐标的大小
            1. 先遍历矩阵，计算每个连通块(area of island)的大小
            2. 再遍历矩阵每个为 0 的点，假设其标为1，有多少的连通块可以被连接，最大的岛屿面积因此是多少

        代码：https://leetcode-cn.com/problems/making-a-large-island/solution/
        视频：https://www.youtube.com/watch?v=_426VVOB8Vo
        '''

        n = len(grid)

        def valid_neighbors(x, y):
            ''' 返回有效的四周坐标 '''
            res = []
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n:
                    res.append((i, j))
            return res

        def dfs(x, y, index):
            count = 1  # 能进入 dfs 的 x, y 本身就代表的一个岛
            grid[x][y] = index
            for i, j in valid_neighbors(x, y):
                if grid[i][j] == 1:
                    count += dfs(i, j, index)
            return count

        res = 0

        index = 2
        hashmap = {}

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    count = dfs(x, y, index)
                    res = max(res, count)
                    hashmap[index] = count
                    index += 1

        if res in [n ** 2, n ** 2 - 1]:
            return n ** 2
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    seen = {grid[i][j] for (i, j) in valid_neighbors(x, y) if
                            grid[i][j] > 1}  # 将 0 四周所有在 grid 内的岛所对应的 index 找出来
                    res = max(res, sum(hashmap[i] for i in seen) + 1)  # 计算将 0 变成 1 后，max(被连通的所有岛的面积, 目前取得的最大面积)
        return res
