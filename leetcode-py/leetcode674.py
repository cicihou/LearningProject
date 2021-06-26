class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ''' 300/673 的相似题，不过简单很多
        time O(n)
        space O(n)

        用 sliding window 会更简单，space 会优化到 O(1)
        '''
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)
