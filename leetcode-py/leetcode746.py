'''
可以参考：https://www.youtube.com/watch?v=OoGswqFU-zs
但是我觉得他讲的没有特别清楚，主要还是参考 lc 70 的视频和解法
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        method 1 greedy（improved dp）
            f[i] = cost[i] + min(f[i+1], f[i+2])
            记忆化存储后，cost[len(cost)-1] 和 cost[len(cost)-2] 中有一个是最优解
        time O(n)
        space O(1)
        '''
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

        '''
        method 2 DP
        注意有一个 constraint 是 2 <= cost.length <= 1000
        time: O(n)
        space: O(n)
        '''
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        return dp[n]
