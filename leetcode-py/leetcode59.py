'''
注意看一下 二维数组的列表表达式生成
attention the generation of matrix
don't use, not available: matrix = [[None] * 3] * 3
这个是浅拷贝，改其中一个列表的值，另外的列表的值也会发生改变

# >>> a = [[None] * n] * 3
# >>> a
# [[None, None, None], [None, None, None], [None, None, None]]
# >>> a[1][1] =1
# >>> a
# [[None, 1, None], [None, 1, None], [None, 1, None]]
# >>> b = [[None for _ in range(n)] for j in range(n)]
# >>> b
# [[None, None, None], [None, None, None], [None, None, None]]
# >>> b[1][1] = 1
# >>> b
# [[None, None, None], [None, 1, None], [None, None, None]]

'''

class Solution:
    def generateMatrix(self, n: int):
        matrix = [[None for _ in range(n)] for j in range(n)]
        direc = 0
        left = 0
        right = n - 1
        top = 0
        down = n - 1

        val = 1
        while left <= right and top <= down:
            if direc == 0:
                for i in range(left, right + 1):
                    matrix[top][i] = val
                    val += 1
                top += 1
            if direc == 1:
                for i in range(top, down + 1):
                    matrix[i][right] = val
                    val += 1
                right -= 1
            if direc == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = val
                    val += 1
                down -= 1
            if direc == 3:
                for i in range(down, top - 1, -1):
                    matrix[i][left] = val
                    val += 1
                left += 1
            direc = (direc + 1) % 4
        return matrix


s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(4))
