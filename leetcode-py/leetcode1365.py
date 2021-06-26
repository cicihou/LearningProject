class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ''' 简单版的 315[hard] '''
        s = sorted(nums)
        res = []
        for num in nums:
            res.append(s.index(num))
        return res
