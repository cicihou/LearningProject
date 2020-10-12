class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s:
            if ' ' in s:
                s = [ i for i in s.split(' ') if i]
                return len(s[-1]) if s else 0
            else:
                return len(s)
        else:
            return 0


s = Solution()
print(s.lengthOfLastWord(' '), '0')
