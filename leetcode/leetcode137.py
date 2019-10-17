class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(0, len(nums)):
        #     if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
        #         return nums[i]

        '''method2 '''
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num

        'm3'
        nums.sort()



s = Solution()
print(s.singleNumber([2, 2, 3, 2]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))