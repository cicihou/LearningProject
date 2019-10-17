class Solution:
    def reverseVowels(self, s):
        if not s:
            return ''
        vowels = 'aeiouAEIOU'
        res = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(s[i])
                s[i] = '_'
        for i in range(len(s)):
            if s[i] == '_':
                s[i] = res.pop()
            if not res:
                break
        return ''.join(s)

s = Solution()
print(s.reverseVowels('hello'), 'holle')
print(s.reverseVowels('leetcode'), 'leotcede')
print(s.reverseVowels('aA'), 'Aa')

