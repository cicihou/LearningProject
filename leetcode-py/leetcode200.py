class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
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

s = Solution()
s.numIslands([["1","1","1","1","0"]])
