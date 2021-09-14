'''
代码+图解：https://leetcode-cn.com/problems/perfect-squares/solution/hua-jie-suan-fa-279-wan-quan-ping-fang-shu-by-guan/

最差的情况就是
dp[i] = i，也就是说要构成 5 的完全平方差，需要 5个 1

优化的情况就是，创造一个 j，在 j 的平方小于当前所需要的数的情况下，用j 来优化我们所需要的正方形平方的个数

'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i  # 最坏情况
            j = 1
            while i - j**2 >= 0:
                dp[i] = min(dp[i], dp[i-j**2] + 1)  # 将当前的正方形个数优化
                j += 1
        return dp[n]
