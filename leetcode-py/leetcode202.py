class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()

        def happy(n):
            res = 0
            for i in str(n):
                res += int(i) ** 2
            return res

        while n not in res:
            res.add(n)
            n = happy(n)

        return False if n != 1 else True
