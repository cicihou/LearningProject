class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        用 DP 的解法很好懂

        dp[i] 表示前 i 位的字符是否可以用 wordDict 中的单词表示
        遍历字符串 s 中所有索引

        :param s:
        :param wordDict:
        :return:
        '''
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True  # 空字符串
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
