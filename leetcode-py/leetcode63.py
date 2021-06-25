class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        根据 62 method 2 修改而来
        recursion + memoize
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        memo = {}
        def countPath(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m - 1 and j == n-1:
                res = 1
            elif i>= m or j >= n or obstacleGrid[i][j] == 1:
                res = 0
            else:
                res = countPath(i+1, j) + countPath(i, j+1)
            memo[(i, j)] = res
            return res
        return countPath(0, 0)

        '''
        DP
        细节：由于机器人只能向右向下，所以如果在边上碰到一个 obstacle，相当于整条边都被封死了
        也可以在 dp 数组中预处理完这两条边
        We'll also need to seed the initial starting position with a value of 1 to represent the single initial path.
        
        time O(m*n)
        space O(m*n)
        '''

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = int(obstacleGrid[0][0] == 0)

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
