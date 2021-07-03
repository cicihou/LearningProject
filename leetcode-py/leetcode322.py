'''

视频：https://www.youtube.com/watch?v=Y0ZqKpToTic

        if j >= coins[i]:
            dp[i][j] = min(dp[i-1][j], 1 + T[i][j-coins[i]]
        else:
            dp[i][j] = dp[i-1][j]


代码：从递归 -> 记忆化 memoize -> dp
https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        method 1 recursion
        TLE
        '''
        global res
        res = float('inf')

        def dfs(coins, target, count):
            if target < 0:
                return
            if target == 0:
                global res
                res = min(res, count)
            for i in range(len(coins)):
                dfs(coins, target-coins[i], count+1)

        dfs(coins, amount, 0)
        if res == float('inf'):
            return -1
        return res

        '''
        method 2 
        memoize + recursion
        '''
        # TODO

        '''
        method 3 dp
        
        视频：https://www.youtube.com/watch?v=jgiZlGzXMBw
        
        time: O(N * amount), N is len(coins)
        space: O(amount)
        '''
        dp = [amount + 1] * (amount + 1)
        dp [0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] == amount + 1 else dp[amount]


s = Solution()
s.coinChange([1,2,5],11)
