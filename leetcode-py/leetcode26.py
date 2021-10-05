class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        method 1

        time: O(n^2)
        space: O(1)
        '''
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in nums[:i]:
                nums.pop(i)
        return len(nums)

        '''
        method 2 slow-fast pointer
        跟 80 题思想完全一致，
        
        time: O(n)
        space: O(1)
        '''
        slow = fast = 1
        if len(nums) <= fast:
            return len(nums)

        while fast < len(nums):
            if nums[slow - 1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        '''
        method 3 two-pointer
        
        time: O(n)
        space: O(1)
        '''
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
