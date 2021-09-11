from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        跟 lc 300 有一定相似，是 lc 413 的后续扩展题

        之前的状态值里有同样的 diff 的时候，说明才可能形成长度大于等于 3 的等差数列，此时记录结果；
        '''
        n = len(nums)
        if n < 3:
            return 0

        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] += dp[j][diff] + 1
                if diff in dp[j]:
                    res += dp[j][diff]
        return res
