'''
代码：https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions

这题用 DFA 做很合适
https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0:
            return 0

        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            del ls[0]

        i = 0
        res = 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + int(ls[i])  # ord(ls[i]) - ord(0) 可以替换 int(ls[i])，并且避免使用了内置函数
            i += 1

        return max(-2**31, min(2**31-1, res*sign))
