class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = []
        for ch in s:
            if ch.isalpha():
                res.append(ch)

        ans = ''
        for i in range(len(s)):
            if s[i].isalpha():
                ans += res.pop()
            else:
                ans += s[i]
        return ans
