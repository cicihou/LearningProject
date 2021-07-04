'''
视频：https://www.youtube.com/watch?v=_fgjrs570YE

if j >= coins[i]:
    T[i][j] = T[i-1][j] + T[i][j - coins[i]]
else:
    T[i][j] = T[i-1][j]


'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        2-D DP
        视频：https://www.youtube.com/watch?v=DJ4a7cmjZY0
        代码：https://leetcode.com/problems/coin-change-2/discuss/675186/Python3-DP-Solution-O(mn)-Time-and-Space

        row 是 len(coins) + 1，col 是 amount
        第一列，amount/target 为 0，表示有一种硬币方案（i.e. 什么硬币都不要），因此 col 为 0 时默认置 1

        遍历：i in (1, len(coins) + 1)
                j in (1, amount + 1)
                    if j >= coins[i-1]
                        dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]  # 取 本列上一行 和本行前进 coins[i-1] 格的值 之和
                    else:
                        dp[i][j] = dp[i-1][j]  # 直接取本列的上一行

        time: O(amount*n)
        space: P(amount*n)
        '''
        dp = [[0] * (amount+1) for _ in range(len(coins) + 1)]

        # 第一列全部标 1
        for j in range(len(coins)):
            dp[0][j] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


        '''
        用滚动数组优化
        
        动态规划的边界是 dp[0] = 1。只有当不选取任何硬币时，金额之和才为 0，因此只有 1 种硬币组合。
        对于面额为 coin 的硬币，
            当 coin ≤ i ≤ amount 时，如果存在一种硬币组合的金额之和等于 i−coin，则在该硬币组合中增加一个面额为 coin 的硬币，即可得到一种金额之和等于 i 的硬币组合。
            因此需要遍历 coins，对于其中的每一种面额的硬币，更新数组 dp 中的每个大于或等于该面额的元素的值。

        time: O(amount * n)
        space: O(amount)
        非常快
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
