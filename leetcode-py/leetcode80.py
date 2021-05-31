class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        fast slow pointer
        '''
        if len(nums) < 3:
            return len(nums)
        slow = fast = 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
