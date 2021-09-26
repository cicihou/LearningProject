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

        '''
        method 2
        递归 + memoize 就不会超时了
        '''
        cache = {0: 0, 1: 1, 2: 1}

        def memo(n):
            if n in cache:
                return cache[n]
            res = memo(n - 3) + memo(n - 2) + memo(n - 1)
            cache[n] = res
            return res

        return memo(n)
