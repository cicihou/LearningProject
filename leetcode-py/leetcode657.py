class Solution:
    def judgeCircle(self, moves: str) -> bool:
        '''
        time: O(n)
        space: O(1)
        '''
        up_down = 0
        left_right = 0
        for m in moves:
            if m == 'U':
                up_down += 1
            elif m == 'D':
                up_down -= 1
            elif m == 'L':
                left_right += 1
            elif m == 'R':
                left_right -= 1
        return up_down == left_right == 0
