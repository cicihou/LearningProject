class Solution(object):
    def longestConsecutive(self, nums):
        """
        method 1

        time: O(nlogn)， sort
        space: O(1)
        """
        if not nums:
            return 0
        res = tmp = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1
        return res

        '''
        method 2
        
        time: O(n)
        space: O(n)
        
        理论上说用 hash 是更节约时间复杂度了，不过两种算法的核心其实差不多
        '''
        if len(nums) == 0:
            return 0
        cache = {num:None for num in nums}
        res = tmp = 1
        last = None
        for k in sorted(cache):
            if last is not None:
                if k - last == 1:
                    tmp += 1
                    res = max(res, tmp)
                else:
                    tmp = 1
            last = k
        return res


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
print(s.longestConsecutive([1,2,3,0,0]), 4)
print(s.longestConsecutive([1,2,43,44,56,45, 1, 3, 2]),3)
print(s.longestConsecutive([0,0,0]),1)
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]),7)
