class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ''' method 1'''
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

        ''' method 2'''
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

        ''' method3 
         simplify 1 && 2 
         time O(n), space O(1)
         '''
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        else:
            return len(nums)

        ''' method 4 binary search
        time O(logN)
        space O(1)
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
