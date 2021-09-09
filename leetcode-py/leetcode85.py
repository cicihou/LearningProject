class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        based on lc 84，calculate the histogram of every row, and then get the maximum area of histogram

        monostack
        视频：https://www.youtube.com/watch?v=dAVF2NpC3j4

        这道题跟 lc 84 几乎一模一样的单调栈写法，只是需要将 matrix 每一行都处理成直方图的形式，然后逐行计算直方图的最大面积
        需要注意这题，循环里面计算的只是单个直方图的最大面积，用 tmp 暂存；然后跟我们最终结果 res 相比较，然后得到最后的结果

        这道题先理解 lc 84 后，理解这道题就不难了，84 的 monostack 有点难理解

        time: O(mn)
        space: O(mn)
        '''
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '1':
                    grid[i][j] = 1 if i == 0 else grid[i - 1][j] + 1

        res = 0
        for index in range(m):
            left = [0] * n
            right = [0] * n

            monostack = []
            heights = grid[index]
            for i in range(n):
                while monostack and heights[monostack[-1]] >= heights[i]:
                    monostack.pop()
                left[i] = monostack[-1] if monostack else -1
                monostack.append(i)

            monostack = []
            for i in range(n - 1, -1, -1):
                while monostack and heights[monostack[-1]] >= heights[i]:
                    monostack.pop()
                right[i] = monostack[-1] if monostack else n
                monostack.append(i)

            tmp = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
            res = max(res, tmp)
        return res
