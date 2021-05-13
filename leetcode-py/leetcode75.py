class Solution(object):
    def sortColors(self, nums):
        """
        method 1
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # from collections import Counter
        # return sorted(Counter(nums).elements())

        ''' method 2 bubble sort'''
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0, 0, 2, 2]))
