import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        bfs
        先将所有坐标为 0 的点，加到 visited 和 queue 中
        然后再遍历queue，如果 queue mat[i][j] 向四周扩散的元素是有效的点，且不在 visited 中，则为 mat[i][j] + 1
        '''
        m = len(mat)
        n = len(mat[0])

        visited = set()
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    mat[x][y] = mat[i][j] + 1
                    visited.add((x, y))
                    q.append((x, y))  # 如果这里的 queue 不加入我们新遍历的点，那么不与 0 接壤的点就无法被走到

        return mat

        '''
        method 2 DP
        '''
        # TODO


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(B):
    # write your code in Python 3.6
    m = len(B)
    n = len(B[0])

    block = set()

    start = None

    def get_block_way(i, j, sign):
        block_ways = set()
        block_ways.add((i, j))
        if sign == '^':
            while i >= 0 and B[i][j] != 'v':
                block_ways.add((i, j))
                i -= 1
        elif sign == 'v':
            while i < m and B[i][j] != '^':
                block_ways.add((i, j))
                i += 1
        elif sign == '>':
            while j < n and B[i][j] != '<':
                block_ways.add((i, j))
                j += 1
        elif sign == '<':
            while j >= 0 and B[i][j] != '>':
                block_ways.add((i, j))
                j -= 1
        return block_ways

    for i in range(m):
        for j in range(n):
            if B[i][j] == 'X':
                block.add((i, j))
            if B[i][j] in ('<', '>', 'v', '^'):
                blocking = get_block_way(i, j, B[i][j])
                block = blocking.union(block)
            if B[i][j] == 'A':
                start = (i, j)
    if (m - 1, n - 1) in block:
        return False
    if start == (m - 1, n - 1):
        return True

    q = collections.deque([start])
    visited = set()
    while q:
        i, j = q.popleft()
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and (x, y) not in block:
                visited.add((x, y))
                q.append((x, y))
                if (m - 1, n - 1) == (x, y):
                    return True
    return False


