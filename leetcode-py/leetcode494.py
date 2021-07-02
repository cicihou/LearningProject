'''
代码：https://leetcode-solution.cn/solutionDetail?type=3&id=54&max_id=2
视频：https://www.youtube.com/watch?v=hqGa65Rp5LQ

题目规定数组元素非负，而我们最终选定是有正有负的
因此我们假设**最终选择的数组**中，全正子数组和是 positive，全负子数组和是 negative，数组元素绝对值总和是 total，目标数是 target

positive + negative = target
positive - negtive = total

则可推出 positive = (target + total) / 2

这题递归的写法相对好理解很多，也可以回溯，背包 DP 的写法我不太理解
'''
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        method 1 recursion + memoize
        '''

        @lru_cache(None)
        def f(i, cur_sum):
            if i == len(nums):
                if target == cur_sum:
                    return 1
                return 0
            return f(i+1, cur_sum + nums[i]) + f(i+1, cur_sum - nums[i])

        return f(0, 0)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        '''
        method 2 
        
        2D DP
        '''
        if (sum(nums) + target) % 2 == 1:
        # total 和 target 的两个数之和必然是偶数，因为 total + target = 2 positive
            return 0
        t = (sum(nums) + target) // 2
        dp = [[0] * (len(nums) + 1) for _ in range(t+1)]
        dp[0][0] = 1

        for i in range(t + 1):
            for j in range(1, len(nums) + 1):
                dp[i][j] = dp[i][j-1]
                if i - nums[j-1] >= 0:
                    dp[i][j] += dp[i-nums[j-1]][j-1]
        return dp[-1][-1]

    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        '''
        method 3 1D dp
        '''
        t = sum(nums) + target
        if t % 2:
            return 0
        t = t // 2

        dp = [0] * (t + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(t, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[-1]
