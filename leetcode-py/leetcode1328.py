class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''
        1. len == 1，无法将其变成 non-palindrome
        2. len > 1，将第一个不为 a 的字符串变成 a
        3. len > 1 且全是 a，将最后一个 a 变成 b
        '''
        n = len(palindrome)
        if n == 1:
            return ''
        if len(set(palindrome)) == 1 and palindrome[0] == 'a':
            return palindrome[:n-1] + 'b'
        for i in range(n):
            if palindrome[i] != 'a':
                res = palindrome[:i] + 'a' + palindrome[i+1:]
                if len(set(res)) != 1:
                    return res
        else:
            return palindrome[:n-1] + 'b'
