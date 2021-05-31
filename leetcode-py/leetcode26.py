class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        method 1
        '''
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] in nums[:i]:
        #         nums.pop(i)
        # return len(nums)

        '''
        method 2 slow-fast pointer
        跟 80 题思想完全一致，
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
