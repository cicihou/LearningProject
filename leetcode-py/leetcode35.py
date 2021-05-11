''' Solution 1 '''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            for i in range(1, len(nums)):
                if target > nums[i-1] and target < nums[i]:
                    return i


''' Solution 2 '''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            nums.append(target)
            nums.sort()
            return nums.index(target)
