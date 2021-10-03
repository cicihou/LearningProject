class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res
