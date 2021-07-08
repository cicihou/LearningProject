class Solution:
    def numTrees(self, n: int) -> int:
        '''
        recursion: TLE，纯粹递归会超时

        1. 生成一个 [1:n+1] 的数组（题目给的要求就是 从 1 到 n，换成程序语言就是range(1, n+1) ）
        2. 遍历一次数组，并执行以下逻辑
            1. 对于每一项，我们都假设其是断点，断点左侧是 A，断点右侧是 B
            2. 那么 A 就是 i - 1 个数，B 是 n-i 个数
        3. 递归，将 A 和 B 的结果相乘即可

        F(i, n) = G(i-1) * G(n-i)
        视频: https://www.youtube.com/watch?v=GgP75HAvrlY
        '''
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i-1) * self.numTrees(n-i)
        return res


class Solution2:
    '''
    recursion + memoize

    time: O(n^2)，循环是 N，递归的深度也是 N，因此总体时间复杂度是 O(n^2)
    space: O(n)，递归的栈深度和 visited 的大小都是 N
    '''
    memo = {}

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo.get(n)
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        self.memo[n] = res
        return res


class Solution3:
    def numTrees(self, n: int) -> int:
        '''
        DP
        视频: https://www.youtube.com/watch?v=OIc0mHgHUww
        time: O(n^2)
        space: O(n)
        '''
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
