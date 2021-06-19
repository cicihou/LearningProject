'''
N 皇后问题

用 state space tree 穷举所有可能性，找到符合 N 皇后要求 的路径
https://www.youtube.com/watch?v=xFv_Hl4B83A


前 11 min 讲思路，后面结合动画演示代码: https://www.youtube.com/watch?v=xouin83ebxE
代码：https://github.com/mission-peace/interview/blob/master/src/com/interview/recursion/NQueenProblem.java
思想是当一个皇后在某个位置 [i, j] 的时候，剩下的行，列，对角线都处于被攻击状态
 row:       [i, n!]，
 colomn:    [n!, j]
 diagonal:  [i-1, j-1](until 0)
            [i+1, j+1](until n)
            [i-1, j+1](until 0 or n)
            [i+1, j-1](until 0 or n)
类似枚举，当第一个 N 皇后位置摆好的时候，后面的皇后不能摆放到攻击区域


lc 官方代码：https://leetcode-cn.com/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
这个给出了一个很有意思的判断[i, j] diagonal 判断方法
同个 diagonal，i-j 或 i+j 一定会相等
从上面的坐标系也可以看出：
    趋势为下降的线，同个 diagonal 上，横纵坐标相减之后相等
    趋势为上升的线，同个 diagonal 上，横纵坐标相加之后相等

'''
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        将 row 行作为 backtrack 的累增值，总之一定会是每行只有一个，所以 row 是自然累增的
            queen 作为记录放置有效 N 皇后 col 的数组
        upward_diagonal: row+col
        downward_diagonal: row-col

        当 queen 出现一个暂时有效的答案时(row 是累增, col 是需要记录摆放的位置)，我们用 queens[row] = col
        '''
        solutions = []
        queens = [-1] * n

        # 这三个 set() 必须单独定义，一行的时候定义成了引用会相互干扰
        columns = set()
        diagonal_upward = set()
        diagonal_downward = set()

        def generateBoard():
            row = ['.'] * n
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(row):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for col in range(n):
                    if not any([col in columns, row-col in diagonal_downward, row+col in diagonal_upward]):
                        queens[row] = col
                        columns.add(col)
                        diagonal_upward.add(row+col)
                        diagonal_downward.add(row-col)
                        backtrack(row+1)
                        columns.remove(col)
                        diagonal_upward.remove(row+col)
                        diagonal_downward.remove(row-col)

        backtrack(0)
        return solutions


s = Solution()
s.solveNQueens(4)
