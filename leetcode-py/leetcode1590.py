class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ''' method 1 前缀和 + 同余定理
        '''
        # TODO
        tar = sum(nums) % p
        dic = {0: -1}
        prefix = 0
        res = len(nums)
        for i in range(len(nums)):
            prefix += nums[i]
            dic[prefix % p] = i
            modd = (prefix - tar) % p
            if modd in dic:
                res = min(res, i - dic[modd])
        return -1 if res == len(nums) else res
