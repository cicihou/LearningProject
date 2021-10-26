class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        classic two-pointers，双指针

        双指针 l, r 判断字符串是否相等
        碰到第一个不相等的字母，检查其是否是唯一一个令其不相等的字符
        尝试删去 s[l] 或者删去 s[r] 看一下剩下的字符串是否是一个 palindrome
        在纸上画一下，删去左边就是 s[l+1:r+1]，删去右边就是 s[l:r]

        time: O(n)
        space: O(1)
        '''
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                one = s[l:r]
                two = s[l + 1:r + 1]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1
        return True
