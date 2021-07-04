from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        题意要求，按 90度顺时针方向 逐行反转二维数组
            1. 先将数组中的值，按对角线坐标两两互换（完成逆时针反转）
            2. 然后逐行进行数组反转，就可以得到想要的结果

        视频：https://www.youtube.com/watch?v=Y72QeX0Efxw

        time: O(n^2)
        space: O(1)
        """
        n = len(matrix)

        for i in range(0, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
