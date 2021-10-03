class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        lc 45 + lc 1024
        判断能不能正好到达最后一个 index，当前步数并不是一定要用尽
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
