'''
https://www.youtube.com/watch?v=1ZGJzvkcLsA

reproduce via youtube fake code

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
top = 0
left = 0
right = len(matrix[0]) - 1
down = len(matrix) - 1

res = []

# 0 ➡，1 ⬇, 2 ⬅, 3 ⬆
# 0 -> 1 -> 2 -> 3 is also the spiral order required
direc = 0
# while len(res) < len(matrix) * len(matrix[1]): 这个如果边界值没写错也没毛病，但如果边界值错了就会报错，不好调试
# 注意几个边界值，由于 range 是左闭右开的 [) ，需要在边界值上相加/相减
while top <= down and left <= right:
    if direc == 0:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
    if direc == 1:
        for i in range(top, down + 1):
            res.append(matrix[i][right])
        right -= 1
    if direc == 2:
        for i in range(right, left - 1, -1):
            res.append(matrix[down][i])
        down -= 1
    if direc == 3:
        for i in range(down , top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    direc = (direc + 1) % 4

print(res)


# method 2
a super cool python one line code
https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

The meaning of return a and b is that when a is empty, the function jumps out. When a is not empty, b is executed. I am confused about this.


def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1

        res = []

        direc = 0
        while top <= down and left <= right:
            if direc == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            if direc == 1:
                for i in range(top, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direc == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direc == 3:
                for i in range(down , top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            direc = (direc + 1) % 4
        return res
