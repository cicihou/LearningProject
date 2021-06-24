class Solution:
    def tribonacci(self, n: int) -> int:
        ''' 同 lc 70/509 fibonacci 问题
        这题用递归会 TLE，直接 memoize 就好
        Tn+3 = Tn + Tn+1 + Tn+2 '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0, 1, 1]
        for i in range(3, n+1):
            nums.append(nums[i-1]+nums[i-2]+nums[i-3])
        return nums[-1]
