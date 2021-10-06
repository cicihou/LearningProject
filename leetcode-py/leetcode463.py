class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        time: O(m*n)
        space: O(1)
        '''
        m = len(grid)
        n = len(grid[0])
        res = 0
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 4
                    for x, y in direc:
                        nx, ny = i + x, j + y
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            count -= 1
                    res += count
        return res
