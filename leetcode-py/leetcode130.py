class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        method 1 DFS

        :param board:
        :return:
        '''
        regions = {}
        reserved = set()
        seen = set()

        m = len(board)
        n = len(board[0])

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, flag):
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x, y) not in seen:
                seen.add((x, y))
                regions.setdefault(flag, []).append((x, y))
                if x in [0, m - 1] or y in [0, n - 1]:
                    reserved.add(flag)
                for nx, ny in dir:
                    dfs(x + nx, y + ny, flag)

        index = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in seen:
                    dfs(i, j, index)
                    index += 1
        for i in reserved:
            regions.pop(i)
        for k, v in regions.items():
            for x, y in v:
                board[x][y] = 'X'

        '''
        method 2 BFS
        '''
        # TODO
