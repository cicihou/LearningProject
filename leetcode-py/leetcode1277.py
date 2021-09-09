class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        本题跟 lc 221 一模一样
        :param matrix:
        :return:
        '''
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    res += dp[i][j]
        return res
