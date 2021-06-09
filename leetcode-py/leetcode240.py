class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        data = []
        for i in range(len(matrix[:])):
            data.extend(matrix[i])
        if target in data:
            return True
        return False

        '''
        binary search: 跟 74 题 思路完全一致
        '''
        m = len(matrix)
        n = len(matrix[0])

        x = m - 1
        y = 0

        while x >= 0 and y < n:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False


s = Solution()
print(s.searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 5))
print(s.searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20))

print(s.searchMatrix([[]],1))
