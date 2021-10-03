class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        维护一个 sliding window，最多只能有一个 0 在我们的window 中
        如果我们的 window 有了两个 0，就需要 contract out window
        '''
        res = 0
        zero_count = 0
        n = len(nums)
        l = r = 0
        while r < n:
            if nums[r] == 0:
                zero_count += 1

            while zero_count == 2:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res
