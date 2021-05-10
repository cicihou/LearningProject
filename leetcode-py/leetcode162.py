class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return nums.index(max(nums))
        else:
            return 0

