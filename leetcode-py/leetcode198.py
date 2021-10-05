class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        对于 第 [i] 个房子，抢还是不抢（判断总价值哪个更大）
            i - 1 不能抢，否则会触发警铃
                抢: 当前房子的价值 + dp[i-2]
                不抢: dp[i-1]
            当前房子的价值就是上面对应的抢或者不抢中间的那个较大的值

        dp[i] = max(dp[i-1], dp[i-2] + nums[i-2)
            由于 dp[0] 和 dp[1] 会初始化为 0，所以 dp[i] 对应的是 nums[i-2]

        complexity
            Time O(n)
            Space O(n)

        系列题： House Robber 198/213/337
        '''
        n = len(nums)
        if n < 3:
            return max(nums)
        dp = [0] * (n+2)
        for i in range(2, n+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        return dp[-1]


        '''
        method 2 memoize
        
        状态分解: 
            抢当前房子; func(i+2) + nums[i]
            抢下一个房子; func(i+1)
        
        time: O(n)
        space: O(n)
        '''
        memo = {}

        def memoize(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            res = max(memoize(i+1), memoize(i+2) + nums[i])
            memo[i] = res
            return res

        return memoize(0)
