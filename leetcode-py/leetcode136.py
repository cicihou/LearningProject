class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        time: O(n)
        space: O(n)
        这题比较简单，也有很多种写法，时间复杂度要求也不高
        '''
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return list(res)[0]
