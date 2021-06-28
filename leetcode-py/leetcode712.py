class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        跟 LC 1143/583 一样，唯一的区别是，前两题是为了算长度，因此 dp[i][j] = dp[i-1][j-1] + 1
        这一题是算字符的 ASCII 码，dp[i][j] = dp[i-1][j-1] + ord(str)

        The only thing different is that LC712 calculates the Maximum ASCII Sum of Common Subsequence while LC1143 needs to find out the length of LCS. The result will be ASCII Sum of S1 - Max ASCII Sum of CS + ASCII Sum of S2 - Max ASCII Sum of CS
        计算返回上跟 583 一样
        '''
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return sum(map(ord, s1+s2)) - 2 * dp[-1][-1]

        '''
        memoize + recursion
        这个慢于 DP
        '''
        memo = {}

        def LCS(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s1) or j >= len(s2):
                res = 0
            elif s1[i] == s2[j]:
                res = LCS(i + 1, j + 1) + ord(s1[i])
            else:
                res = max(LCS(i + 1, j), LCS(i, j + 1))
            memo[(i, j)] = res
            return res

        return sum(map(ord, s1 + s2)) - 2 * LCS(0, 0)
