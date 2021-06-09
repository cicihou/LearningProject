class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        将初始点标到左下角，如果 matrix[x][y] > target，则 x -= 1
        如果 matrix[x][y] < target，则 y += 1
        '''
        m = len(matrix)  # m 行
        n = len(matrix[0])  # n 列

        x = m - 1
        y = 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                x -= 1
            if matrix[x][y] < target:
                y += 1
        return False
