class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res_count = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                count = 1
            res_count = max(res_count, count)
        return res_count


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
print(s.longestConsecutive([1,2,3,0,0]), 4)
print(s.longestConsecutive([1,2,43,44,56,45, 1, 3, 2]),3)
print(s.longestConsecutive([0,0,0]),1)
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]),7)
