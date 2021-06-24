'''
Manacher's Algorithm
视频讲解：https://www.youtube.com/watch?v=V-sEwsca1ak
wiki 介绍：https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2
intro: https://www.hackerrank.com/topics/manachers-algorithm
Time O(n)


DP
视频：https://www.youtube.com/watch?v=UflHuQj6MVA&t=441s
代码：https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
Time O(n^2)
Space O(n^2)
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        DP
        视频：https://www.youtube.com/watch?v=UflHuQj6MVA&t=441s
        代码：https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

        思想：
        先判断最长的子串是否为 1，2，及大于 3
            max_length = 1, max_str = s[0], dp[i][i] = 1
            max_length = 2, max_str = s[i:i+2], dp[i][i+1] = 1
            max_length >= 3, max_str = s[i:i+k], k is the length of substring
                k 的范围是 [3, n+1] 表示整体往 dp 的右上方向遍历，结合视频中的那张图理解
                i 从 0 开始，直到 n-k+1 行。也就是 i 从 第 0 行开始，斜向下遍历（以下是 dp table, 可以结合一下视频）
                3
                ( 0 2 ) ( 1 3 ) ( 2 4 ) ( 3 5 ) ( 4 6 ) ( 5 7 )
                4
                ( 0 3 ) ( 1 4 ) ( 2 5 ) ( 3 6 ) ( 4 7 )
                5
                ( 0 4 ) ( 1 5 ) ( 2 6 ) ( 3 7 )
                6
                ( 0 5 ) ( 1 6 ) ( 2 7 )
                7
                ( 0 6 ) ( 1 7 )
                8
                ( 0 7 )

        生成 dp table 用来记录状态
        状态转移方程：dp[i+1][j-1] and s[i] == s[j]
        这里借用了一个大小为 M * N 二维的 dp table

        Time O(n^2)
        Space O(n^2)
        '''
        n = len(s)
        # 这里不能直接用 dp = [[0] * n] * n，因为这样复制出来的列表是引用，一个改变就会跟着改变（给我气吐了 =-=）
        # 要用列表生成式生成出来
        dp = [[0 for _ in range(n)] for _ in range(n)]

        max_length = 1
        max_str = s[0]

        # substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = 1

        # check substring of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_str = s[i:i+2]
                max_length = 2

        # check for length greater than 2
        # k is the length of substring
        # [3, n+1] 表示往 dp 的右上方向遍历，结合视频中的那张图理解
        # i 从 0 开始，直到 n-k+1 行。也就是 i 从 第 0 行开始，斜向下遍历（这里打印并且结合一下视频）
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    if k > max_length:
                        max_str = s[i:j+1]
                        max_length = k
        return max_str

    def longestPalindrome2(self, s: str) -> str:
        '''
        扩展中心法 Expand Around Center
            1. 遍历 str 中的点，以每个点为中心分别进行奇数、偶数开始向外扩展
            2. 记录下扩展后得到的最大 str
            3. 注意 extend 函数推出的时间点
        '''
        n = len(s)
        res = s[0]
        def extend(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                # 无法扩展时推出，推出时的 i,j 已经不符合要求，上一个答案就是我们找到的最大回文串
                i -= 1
                j += 1
            return s[i+1:j]

        # 注意这里由于 i 要向后扩展一位，因此 为保证 s[i+1] 有效， i + 1 < len(s)， i.e. i < len(s) - 1
        for i in range(n-1):
            e1 = extend(i, i)  # 奇数回文
            e2 = extend(i, i+1)  # 偶数回文
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res


s = Solution()
s.longestPalindrome("aacabdkacaa")
s.longestPalindrome("aaaabbaa")
