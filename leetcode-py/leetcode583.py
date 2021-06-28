class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        跟 1143 LCS 一模一样
        method 1 Recursion + Memoize
        '''
        memo = {}
        def LCS(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1) or j >= len(word2):
                res = 0
            elif word1[i] == word2[j]:
                res = LCS(i+1, j+1) + 1
            else:
                res = max(LCS(i+1,j), LCS(i,j+1))
            memo[(i, j)] = res
            return res
        return len(word1) + len(word2) - 2 * LCS(0, 0)

        '''
        method 2 DP
        '''
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m + n - dp[-1][-1] * 2
