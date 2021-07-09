class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        x = str(x)
        if x[0] == '-':
            sign = -1
            x = x[1:]
        res = 0
        for i in x[::-1]:
            res *= 10
            res += int(i)
        res *= sign
        if -2 ** 31 <= res <= 2 **31 - 1:
            return res
        return 0
