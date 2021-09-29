from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([])

        for i in range(m):
            if '*' in grid[i]:
                j = grid[i].index('*')
                q.append((i, j))
                break
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                if grid[i][j] == '#':
                    return res
                seen.add((i, j))

                for x, y in direc:
                    nx, ny = i+x, j+y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 'X' and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))
            res += 1
        return -1
