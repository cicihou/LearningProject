'''
LCS 算法视频讲解：
    7min 讲解 dp: https://www.youtube.com/watch?v=NnD96abizww
    从递归到 memoize 再到 dp: https://www.youtube.com/watch?v=sSno9rV8Rhg
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        recursion + memo
        '''
        memo = {}
        def LCS(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(text1) or j >= len(text2):
                res = 0
            elif text1[i] == text2[j]:
                res = 1 + LCS(i+1, j+1)
            else:
                res = max(LCS(i+1, j), LCS(i, j+1))
            memo[(i, j)] = res
            return res
        return LCS(0, 0)

        '''
        DP 看看视频
        公式就是，如果match 上了，就是左上角那格 + 1，dp[i][j] = 1 + dp[i-1][j-1]
        如果match 不上，就是max(左格子，上格子)，dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        Time O(m*n)
        Space O(m*n)
        '''
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
