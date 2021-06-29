class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        '''
        题意就是马走日，指定步数、棋盘大小、马所在的初始行列之后，求 马在走了相应步数之后，落出棋盘的概率
        1. 马的初始状态为 1，其他位置都为 0
        2. 按步更新二维数组每个位置的概率，每个（棋盘内合法）位置我们都计算上一轮的马跳一次能否到达这个位置
            （因为每一步都有八种选择路线，因此选择到该位置的概率是 1/8 ）
            如果当前位置有效，我们把概率加到当前位置上
            if 0 <= lastR < n and 0 <= lastC < n:
                dpTemp[i][j] += dp[lastR][lastC] * 0.125
        3. 完成每个步数时，我们把本次的棋盘作为上一轮的棋盘状态，在下一轮开始前把当前棋盘清零，下次循环使用时的概率累加到上一轮的状态棋盘即可

        time: K * N^2
        space: N^2
        '''
        direc = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1

        for step in range(1, k+1):
            dpTemp = [[1 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for r, c in direc:
                        lastR = i - r
                        lastC = j - c
                        if 0 <= lastR < n and 0 <= lastC < n:
                            dpTemp[i][j] += dp[lastR][lastC] * 0.125
            dp = dpTemp
        return sum(sum(d) for d in dp)
