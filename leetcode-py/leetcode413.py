class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        这题其实稍微想想还是挺好理解的，最少要三个连续的数，才是一个等差数列

        视频：https://www.youtube.com/watch?v=rKrLUXfzRQ4

        :param nums:
        :return:
        '''
        if len(nums) < 3:
            return 0
        n = len(nums)
        dp = [0] * n

        diff = nums[1] - nums[0]

        for i in range(2, n):
            if nums[i] - nums[i-1] == diff:
                dp[i] = dp[i-1] + 1
            else:
                diff = nums[i] - nums[i-1]
        return sum(dp)
