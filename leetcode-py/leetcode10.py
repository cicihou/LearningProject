'''
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element

example 1
a.b
True: acb, aab, avb
False: ab, acby, cb

example 2
a*b
True: b, ab, aab, aaab
False: a, acb

example 3
a*b.*y
True: by, bly, ably, ablmy
False: ay, ab

i 代表 text
j 代表 pattern

DP[i][j] = ?

if text[i] == pattern[j] || pattern[j] == '.'
    dp[i][j] = dp[i-1][j-1]
elif pattern[j] == '*'
    # zero occurence
    dp[i][j] = dp[i][j-2]
    if text[i] == pattern[j-1] || pattern[j-1] == '.':
        dp[i][j] = dp[i-1][j]
else:
    dp[i][j] = False

视频：https://www.youtube.com/watch?v=l3hda49XcDE
代码：https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/RegexMatching.java

这题好难啊，我懂了，好像又没懂 =-=
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        DP
        time: O(M*N)
        space: O(M*N)
        '''
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        # 当 str 和 pattern 都为空时，应该标成 True
        dp[0][0] = True

        # 当 pattern 存在 * 时，dp[i][j] = dp[i][j-2]，先单独处理第一行的情况（此时还没有对应任何字符串 text）
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[-1][-1]
