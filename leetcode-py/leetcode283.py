class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        while 1:
            if 0 in nums:
                nums.remove(0)
                zero += 1
            else:
                break
        nums += [0] * zero

        '''
        method 2
        two-pointer
        '''
        j = 0
        n = len(nums)
        for i in range(n):
            if j >= n:
                break
            while j < n - 1 and nums[j] == 0:
                j += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
