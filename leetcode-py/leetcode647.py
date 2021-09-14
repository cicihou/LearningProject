class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        这一题跟 lc5 几乎一样，用中心扩展法判断有多少个 palindrome
        '''

        n = len(s)
        self.res = 0

        def extend(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                self.res += 1
                i -= 1
                j += 1

        for i in range(n):
            extend(i, i)
            extend(i, i + 1)
        return self.res
