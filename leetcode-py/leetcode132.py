class Solution:
    def minCut(self, s: str) -> int:
        '''
        视频：https://www.youtube.com/watch?v=WPr1jDh3bUQ
             https://www.youtube.com/watch?v=kTCymFbU2ok

        代码：https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/

        dp[i][j] 表示 以 s以i开头以j结尾时(s[i:j+1]) 是否为回文

        time: O(n^2)
        space: O(n^2)

        复习的时候多默写几遍，第一个二层循环的时候，记得是需要完成矩阵自对角线向右上方延伸的所有值

        :param s:
        :return:
        '''
        n = len(s)
        dp = [[1 for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])

        cuts = [float('inf')] * n

        for i in range(n):
            if dp[0][i]:  # dp[0][i] 表示 s[0:i+1] 是一个回文串
                cuts[i] = 0
            else:  #  如果这个字符串本身不是一个回文串，那找到最少的 cut 次数
                for j in range(i):
                    if dp[j+1][i]:  # 如果 s[j+1] 到 i 是一个回文，那么 cut[i] = cur[j]+1 （把当前回文串跟 j及之前的字符分开就可以了）
                        cuts[i] = min(cuts[i], cuts[j]+1)
        return cuts[-1]
