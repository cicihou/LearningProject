class Solution:
    def solve(self, nums, p: int) -> int:
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
