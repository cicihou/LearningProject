class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        method 1
        time: O(n**2)
        space: O(n)

        判断数字是否在集合中，需要 O(n) complexity
        '''
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return list(res)[0]

        '''
        method 2
        用 hashtable 来判断就能将时间复杂度优化
        
        time: O(n)
        space: O(n)
        '''
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                cache.pop(num)
        return list(cache.keys())[0]

        '''
        method 3
        math
        
        time: O(n+n), O(n), we use sum
        space: O(n+n), O(n)
        '''
        return 2 * sum(set(nums)) - sum(nums)
