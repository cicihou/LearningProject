'''
good video：https://www.youtube.com/watch?v=5o-kdjv7FD0
本题方法还有很多，详见：https://leetcode.com/problems/climbing-stairs/solution/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        method 1 TLE 直接递归
        '''
        if n in [0, 1]:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        '''
        method 2 recursion + memoization
        '''
        memo = {}

        def func(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                res = n
            else:
                res = func(n-1) + func(n-2)
            memo[n] = res
            return res
        return func(n)

        '''
        method 3
        问题近似于 Fibonacci(lc 509, Fibonacci Number)，但如果直接递归会 TLE
        必须用一些类似 memoize 的手段
        '''
        if n in [0,1]:
            return 1
        # 实质上是 nums[0] = 1, nums[0] = 1
        nums = [1,1]
        for i in range(2, n+1):
            nums.append(nums[i-1]+nums[i-2])
        return nums[-1]
