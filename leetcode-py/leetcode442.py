class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        time: O(n)
        space: O(n)
        '''
        cache = {}
        res = []
        for num in nums:
            if num in cache:
                res.append(num)
            else:
                cache[num] = 1
        return res
