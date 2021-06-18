class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        time O(M*N)
        space O(M*N)
        注意入参是 str 不是 int: param grid: List[List[str]]

        dfs (i, j) 相邻的四个点为 (i - 1, j), (i + 1, j), (i, j -1), (i, j + 1)
        '''
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = 2
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        m = len(grid)  # 纵坐标（有几行）
        n = len(grid[0])  # 横坐标（有几列）
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


        '''
        BFS
        time O(M*N)
        space O(min(M, N))
        用队列来存储待处理的元素，当所有节点都有值的时候，最坏的空间复杂度就是队列的长度
        因为本质上 BFS 是在做逐层遍历，一般是要等到本层结束才会遍历下一层
        但是 BFS 最多会同时记录两层，所以其实准确是 O(2*min(M,N))
        省略常数，总体来说，会无限趋近于 O(min(M,N))
        '''
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    neighbor = collections.deque([(i,j)])
                    while neighbor:
                        x, y = neighbor.popleft()
                        for row, col in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                            if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                                grid[row][col] = 2
                                neighbor.append((row, col))
        return count


s = Solution()
s.numIslands([["1","1","1","1","0"]])
