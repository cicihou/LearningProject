class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        time: O(N)
        space: O(N), in the worst case
        """
        zero = 0
        while 0 in nums:
            nums.remove(0)
            zero += 1
        nums += [0] * zero

        '''
        method 2
        two-pointer
        
        time: O(n)
        space: O(1)
        '''
        i = j = 0
        n = len(nums)
        while j < n:
            while j < n - 1 and nums[j] == 0:
                j += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
