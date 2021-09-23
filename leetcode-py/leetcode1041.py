class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        lc 657 的变种

        这个问题比较 tricky，其实更接近数学问题
        实际上只要判断机器人最后是否面朝北，就可以知道是不是回到了原点

        关于为什么 instructions *= 4 是最小限度的解释：
        https://leetcode.com/problems/robot-bounded-in-circle/discuss/850437/Python-O(n)-solution-explained
        https://leetcode.com/problems/robot-bounded-in-circle/discuss/290915/Python-Concise-%2B-Explanation

        note: 这个 direc 的判断思想好好记一下，我自己写的时候直觉要用两个数组表达左右方向，其实左右方向只是周期不同
        '''
        direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d = 0

        start = (0, 0)
        instructions *= 4

        for ch in instructions:
            if ch == 'G':
                nx, ny = direc[d]
                start = start[0] + nx, start[1] + ny
            else:
                if ch == 'L':
                    d = (d + 1) % 4
                if ch == 'R':
                    d = (d + 3) % 4

        return start == (0, 0)

        '''
        更加 tricky 的数学解法：判断机器人是否朝北，不朝北就一定能走回来
        
        https://leetcode.com/problems/robot-bounded-in-circle/discuss/291221/Python-O(N)-time-O(1)-space-beats-100-detailed-explanations
        '''
        direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d = 0
        start = (0, 0)
        for ch in instructions:
            if ch == 'L':
                d = (d+1) % 4
            elif ch == 'R':
                d = (d+3) % 4
            else:
                nx, ny = direc[d]
                start = start[0] + nx, start[1] + ny
        return start == (0, 0) or d != 0
