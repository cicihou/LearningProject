from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        参考 62/63，顺便使用滚动数组，节约空间
        :param grid:
        :return:
        '''
        m = len(grid)
        n = len(grid[0])

        dp = grid

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] += dp[i][j-1]
                if j == 0:
                    dp[i][j] += dp[i-1][j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


s = Solution()
s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
