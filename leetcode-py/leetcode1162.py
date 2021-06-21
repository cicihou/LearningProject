from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        '''
        Q: 遍历全部海洋区域，找到某个海洋区域点，离 最近陆地 的距离是最大的
            1. 找到所有陆地的点
            2. 遍历陆地的点，每一圈陆地边上的海洋都标记为同一层
            3. 离所有陆地最远的一层海洋，就满足题目要求
            4. 一共能循环的层数，就是答案
        '''
        m = len(grid)
        n = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque([(i, j) for j in range(n) for i in range(m) if grid[i][j] == 1])

        # If no land or water exists in the grid, return -1.
        if len(q) == m*n or len(q) == 0:
            return -1

        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in directions:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level - 1
