class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, 1 + n):
            if i not in nums:
                res.append(i)
        return res

        '''
        method 2, usually hashmap would be faster
        '''
        n = len(nums)
        hashmap = {num:None for num in nums}
        res = []
        for i in range(1, n+1):
            if i not in hashmap:
                res.append(i)
        return res
