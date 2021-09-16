class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        method 1 这种挺慢的
        :param s:
        :return:
        '''
        k = len(set(s))
        while k < len(s):
            sep = s[0:k]
            if len(set(s.split(sep))) == 1:
                return True
            k += 1
        return False

        '''
        method 2 操作的是指针就会快很多

        题目要求必须是包含重复的，因此我们可以首先排除 abcde 这种无重复的字符串
        至少会产生一个重复，因此只需要遍历 s 的一半
        当 len(s) 是 i 的整数倍，可以将 s[:i] 重复 n 次，判断是否等于 s
        若等于，则表明题意成立；若完成一半的遍历仍不等于，则返回 False
        '''
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        return False
