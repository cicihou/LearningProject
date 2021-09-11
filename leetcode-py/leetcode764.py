class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        '''
        这个比起来 221 来，多加了一次循环

        本题需要知道每个点 (i, j) 在四个方向的延长臂的长度
        221 只需要在正方形上从上而下自左向右进行一次循环
        如果我们只进行这一次循环，那我们只知道(i, j) 的「左」和「上」方向分别有多少延长臂距离
        需要知道(i, j)的「右」和「下」方向的延长臂距离，本题需要从相反方向再扫一次。
        这样每个点所对应 min(左，上，右，下) 的连续距离，就是我们最终想要的答案

        为什么要分四个dp 分别记录呢，因为左和上不能一起记录
        因为左和上一起记录的话，实际上我们需要的 sign 比较特别是十字形的，会影响最终的结果
        （lc 221 可以一起记录，如果这道题也那样写就是错的）
        '''
        dp_left = [[0 for _ in range(n)] for _ in range(n)]  # left
        dp_up = [[0 for _ in range(n)] for _ in range(n)]  # up
        dp_right = [[0 for _ in range(n)] for _ in range(n)]  # right
        dp_down = [[0 for _ in range(n)] for _ in range(n)]  # down

        res = 0
        mines = {tuple(i) for i in mines}
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines:
                    if j == 0:
                        dp_left[i][j] = 1
                    else:
                        dp_left[i][j] = dp_left[i][j - 1] + 1

                    if i == 0:
                        dp_up[i][j] = 1
                    else:
                        dp_up[i][j] = dp_up[i - 1][j] + 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines:
                    if i == n - 1:
                        dp_down[i][j] = 1
                    else:
                        dp_down[i][j] = dp_down[i + 1][j] + 1

                    if j == n - 1:
                        dp_right[i][j] = 1
                    else:
                        dp_right[i][j] = dp_right[i][j + 1] + 1

        for i in range(n):
            for j in range(n):
                res = max(res, min(dp_left[i][j], dp_up[i][j], dp_down[i][j], dp_right[i][j]))
        return res
