class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        method1 (similar to) Brute Force

        :param nums:
        :param k:
        :return:
        '''
        nums.sort()
        cache = set()
        for i in range(len(nums)):
            if nums[i]+k in nums[i+1:]:
                cache.add((nums[i], nums[i]+1))
        return len(cache)

        ''' method 2
        
        由于遍历的顺序，其实只会取到 nums[i] - k 在不在seen，
        我们这个是排序过的数组(如果不排序就不行了)，并且 k >= 0，nums[i] + k 是不会在循环的时候就存在于 seen 中的（无后向性）
        if k <= 0，we need to have statement nums[i] - k in seen
        '''
        if k == 0:
            c = Counter(nums)
            return len([i for i in c if c[i] > 1])
        seen = {}
        nums = sorted(set(nums))
        res = 0

        for i in range(len(nums)):
            if nums[i] - k in seen:
                res += 1
            seen[nums[i]] = 1
        return res
