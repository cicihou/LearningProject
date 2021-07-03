class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        视频：https://www.youtube.com/watch?v=vYYNp0Jrdv0

        1. 遍历矩阵，若矩阵的board[i][j] 符合 word 的第一个字符，判断其回溯空间状态
            1. 回溯空间状态中，如果 word 搜索状态到了最后一个词，返回 True
            2. 回溯空间状态中，如果 i, j 超出了 board 区域，或者 board[i][j] 不符合我们的要求，返回 False
            3. 将 回溯的 board[i][j] 标成空，然后搜寻四个方向的状态；注意完成搜索后还原回溯空间
            4. 返回搜索的四个方向的状态
        2. 矩阵的回溯空间状态满足要求，则认为这个字符串能够在矩阵中被找到
        '''
        m = len(board)
        n = len(board[0])

        def backtrack(board, i, j, count, word):
            if count == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[count]:
                return False
            tmp = board[i][j]
            board[i][j] = ' '
            found = backtrack(board, i+1, j, count+1, word) or \
                    backtrack(board, i, j+1, count+1, word) or \
                    backtrack(board, i-1, j, count+1, word) or \
                    backtrack(board, i, j-1, count+1, word)
            # 回溯之后还原状态空间
            board[i][j] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(board, i, j, 0, word):
                    return True

        return False
