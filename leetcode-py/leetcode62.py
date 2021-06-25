'''
由 1 <= m, n <= 100 可推出，最大时间复杂度为O(n^4)，故本题不能使用 backtracking

good video: https://www.youtube.com/watch?v=t_f0nwwdg5o
从暴力优化到 dp
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        method 1
        intuitive recursion, TLE
        '''
        def countPaths(i, j):
            if i == m-1 and j == n-1:
                return 1
            elif i >= m or j >= n:
                return 0
            else:
                return countPaths(i+1, j) + countPaths(i, j+1)

        return countPaths(0, 0)

    def uniquePaths2(self, m: int, n: int) -> int:
        '''
        method 2
        recursion + memoize
        '''
        memo = {}
        def countPath(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m-1 and j == n-1:
                res = 1
            elif i >= m or j >= n:
                res = 0
            else:
                res = countPath(i+1, j) + countPath(i, j+1)
            memo[(i, j)] = res
            return res
        return countPath(0, 0)

    def uniquePaths3(self, m: int, n: int) -> int:
        '''
        method 3, DP
        dp(i, j) = dp(i-1, j) + dp(i, j-1)

        我们用 f(i, j) 表示从左上角走到 (i, j) 的路径数量，其中 i 和 j 的范围分别是 [0, m) 和 [0, n)。

        由于我们每一步只能从向下或者向右移动一步，因此要想走到 (i, j)
        如果向下走一步，那么会从 (i-1, j) 走过来；
        如果向右走一步，那么会从 (i, j-1) 走过来。因此我们可以写出动态规划转移方程：
            f(i, j) = f(i-1, j) + f(i, j-1)

        需要注意的是，如果 i=0，那么 f(i-1,j) 并不是一个满足要求的状态，我们需要忽略这一项；
        同理，如果 j=0，那么 f(i,j-1) 并不是一个满足要求的状态，需要忽略。

            初始条件为 f(0,0)=1，即从左上角走到左上角有一种方法。
            最终的答案即为 f(m-1,n-1)。

        为了方便代码编写，我们可以将所有的 f(0, j) 以及 f(i, 0) 都设置为边界条件，它们的值均为 1
        '''
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    res = 1
                else:
                    res = dp[i-1][j] + dp[i][j-1]
                dp[i][j] = res
        return dp[m-1][n-1]

    def uniquePaths4(self, m: int, n: int) -> int:
        '''
        Combination Math  组合数学计算公式
        https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/

        我看不懂，但我大为震撼 =-=
        '''
        import math
        return math.comb(m+n-2, n-1)
