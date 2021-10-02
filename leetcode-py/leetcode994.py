from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        res = -1
        q = deque([])
        left = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    left += 1
        # 处理两个 edge case，如果没有好橘子，返回 0；如果没有坏橘子，返回 -1
        if left == 0:
            return 0
        if not q:
            return -1

        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                seen.add((x, y))
                for dx, dy in direc:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))
                        left -= 1
            res += 1
        return res if left == 0 else -1
