'''
区间 DP

定义 f[l][r] 为考虑区间 [l, r]，在双方都做最好选择的情况下，先手与后手的最大得分差值是多少
那么 f[1][n]f[1][n] 为考虑所有石子，先手与后手的得分差值：

f[1][n] > 0f[1][n]>0，则先手必胜，返回 True
f[1][n] < 0f[1][n]<0，则先手必败，返回 False

https://leetcode-cn.com/problems/stone-game/solution/gong-shui-san-xie-jing-dian-qu-jian-dp-j-wn31/

我看不懂，并且我对本题的博弈论解释大为震撼
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for length in range(1, n+1):  # 枚举区间长度
            for l in range(1, n-length+2):
                r = l + length - 1
                a = piles[l-1] - dp[l+1][r]  # l 为先手
                b = piles[r-1] - dp[l][r-1]  # r 为先手
                dp[l][r] = max(a, b)
        return dp[1][n] > 0
