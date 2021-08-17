class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_x = []
        zero_y = []

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    zero_x.append(x)
                    zero_y.append(y)
        for x in range(m):
            for y in range(n):
                if x in zero_x:
                    matrix[x][y] = 0
                if y in zero_y:
                    matrix[x][y] = 0
