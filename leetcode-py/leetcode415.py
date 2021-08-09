class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = 0
        m = max(len(num1), len(num2))

        for i in range(m, 0, -1):
            x, y = len(num1) - i, len(num2) - i

            tmp = 0
            if x >= 0:
                tmp += int(num1[x])
            if y >= 0:
                tmp += int(num2[y])

            res = res * 10 + tmp
        return str(res)
