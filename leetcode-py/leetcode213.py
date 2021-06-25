class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        从 198 修改而来，跟 198 唯一的不同就是，head/tail 房子不能同时打劫
        因此我们分成两次循环分别计算，得到两次打劫成果的 max
        '''
        n = len(nums)
        if n < 3:
            return max(nums)

        def dp(nums):
            dp = [0] * (n+1)
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
            return dp[-1]

        return max(dp(nums[1:]), dp(nums[:-1]))
