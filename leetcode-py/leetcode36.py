class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        这题只需要判断真假，比较无脑，循环就可以了

        值得注意的是，box_index 的写法 box_index = (i // 3) * 3 + j // 3

        由于题目很明确的给出了 board.length == 9，因此这题就是 constant 级别的计算
        time: O(1)
        space: O(1)

        :param board:
        :return:
        '''
        n = len(board)
        boxes = [[] for _ in range(n)]
        rows = [[] for _ in range(n)]
        columns = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val != '.':
                    box_index = (i // 3) * 3 + j // 3
                    if val not in rows[i] and val not in columns[j] and val not in boxes[box_index]:
                        rows[i].append(val)
                        columns[j].append(val)
                        boxes[box_index].append(val)
                    else:
                        return False
        return True
