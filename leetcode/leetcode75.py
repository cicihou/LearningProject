class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        return sorted(Counter(nums).elements())


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0, 0, 2, 2]))