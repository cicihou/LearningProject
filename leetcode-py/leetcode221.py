class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        用 dp[i][j] 表示右下角，且只包含 1 的正方形的边长最大值
            1. 该位置的值为 0 时，dp[i][j] = 0，当前位置不可能在由 1 组成的正方形中
            2. 该位置的值为 1 时，dp[i][j] 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定
            （当前位置的元素值由三个相邻位置的元素中的最小值加一）
                如果 dp[i][j] 不在边上
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                若 dp[i][j] 在边上
                    dp[i][j] = 0

        视频：https://www.youtube.com/watch?v=RElcqtFYTm0
        代码：https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
        :param matrix:
        :return:
        '''
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    res = max(res, dp[i][j])
        return res ** 2
