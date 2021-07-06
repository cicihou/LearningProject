class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        lc 45 + lc 1024
        :param nums:
        :return:
        '''
        n = len(nums)
        end = furthest = 0
        for i in range(n-1):
            furthest = max(furthest, nums[i] + i)
            if i == end:
                end = furthest
            if i == furthest:
                return False
        return True
