'''
good video：https://www.youtube.com/watch?v=5o-kdjv7FD0
本题方法还有很多，详见：https://leetcode.com/problems/climbing-stairs/solution/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        method 1 TLE 直接递归

        这个没有压缩状态空间，会重复计算已知结果

        time: O(2**n), size of recursion tree 指数倍增
        space: O(n)，depth of recursion tree can go up to n
        '''
        if n in [0, 1]:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        '''
        method 2 recursion + memoization
        time: O(n)，size of recursion tree 不会重复计算
        space: O(n)，the depth of recursion tree
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
        method 3 dp
        问题近似于 Fibonacci(lc 509, Fibonacci Number)，但如果直接递归会 TLE
        必须用一些类似 memoize 的手段
        
        这个写法就类似 dp 了，如果使用 dp 滚动数组可以将 space 优化到 O(1)
        
        time: O(n)
        space: O(n)
        '''
        if n in [0,1]:
            return 1
        # 实质上是 nums[0] = 1, nums[0] = 1
        nums = [1,1]
        for i in range(2, n+1):
            nums.append(nums[i-1]+nums[i-2])
        return nums[-1]

        '''
        method 4
        用 lru_cache 来实现 recursion + memoize，跟 method 2 实质上是一样的
        
        time: O(n)
        space: O(n)
        '''
        @lru_cache
        def memoize(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 3
            return memoize(n - 1) + memoize(n - 2)

        return memoize(n)
