class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        time: O(n)
        space: O(n)
        '''
        dic = {}
        for num in nums:
            if num > 0:
                dic[num] = None
        for i in range(1, len(nums) + 2):
            if i not in dic:
                return i

        '''
        method 2
        题目要求空间复杂度为 O(1)
        '''
        # TODO
