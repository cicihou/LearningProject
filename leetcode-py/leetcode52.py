class Solution:
    def totalNQueens(self, n: int) -> int:
        '''
        跟 51 题一模一样，不过进行了一些简化，不再需要生成 board
        需要注意的是需要声明 res 为全局变量

        将 row 行作为 backtrack 的累增值，总之一定会是每行只有一个，所以 row 是自然累增的
           queen 作为记录放置有效 N 皇后 col 的数组
        upward_diagonal: row+col
        downwar_diagonal: row-col

        时间复杂度 O(n!)
        空间复杂度 O(1)
        '''
        columns = set()
        upward_diagonal = set()
        downward_diagonal = set()

        global res
        res = 0

        def backtrack(row):
            if row == n:
                global res
                res += 1
            else:
                for col in range(n):
                    if not any([col in columns, col + row in upward_diagonal, col - row in downward_diagonal]):
                        columns.add(col)
                        upward_diagonal.add(col + row)
                        downward_diagonal.add(col - row)
                        backtrack(row + 1)
                        columns.remove(col)
                        upward_diagonal.remove(col + row)
                        downward_diagonal.remove(col - row)

        backtrack(0)
        return res
