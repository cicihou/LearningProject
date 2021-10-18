class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        '''
        time: O(1)
        space: O(1)
        '''
        sh, sm = map(int, startTime.split(':'))
        fh, fm = map(int, finishTime.split(':'))

        start = 60 * sh + sm
        end = 60 * fh + fm

        if start > end:
            end += 24 * 60

        # 将 end 向前进位
        end = end // 15 * 15
        return max(0, (end - start) // 15)
