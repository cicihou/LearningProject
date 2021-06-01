class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        跟 200 的思路一样，只是需要注意如何在 dfs 中进行适当的返回
        :param grid:
        :return:
        '''
        def dfs(i, j):
            count = 0
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 2
                count += 1
                return count + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            else:
                return 0

        m, n = len(grid), len(grid[0])
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    max_count = max(count, max_count)
        return max_count
