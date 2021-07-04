class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        time: O(n)
        space: O(n)
        '''
        dic = {}
        for num in nums:
            dic[num] = None
        for i in range(len(nums)):
            if i not in dic:
                return i
        return len(nums)

        '''
        method 2
        time: O(n*logN), sort
        space: O(1)
        '''
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
