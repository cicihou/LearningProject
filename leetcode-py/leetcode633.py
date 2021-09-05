from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if sqrt(c) == int(sqrt(c)):
            return True
        cache = {}
        for i in range(int(sqrt(c))+1):
            cache[c-i**2] = None  # 注意两个相同的数也是答案，因此这一句要放在判断的前面
            if i**2 in cache:
                return True
        return False
