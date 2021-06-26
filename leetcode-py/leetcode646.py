class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        DP
        跟 lc 300 相似，跟 lc 435 一模一样！
        跟 435 method 1 一致，不过这题数据量小，不会超时
        '''
        n = len(pairs)
        dp = [1] * n
        pairs.sort()
        for i in range(n):
            for j in range(i+1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        '''
        method 2
        跟 435 method 2 一致，加上了 prune
        '''
        n = len(pairs)
        dp = [1] * n
        pairs.sort()
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
        return max(dp)
