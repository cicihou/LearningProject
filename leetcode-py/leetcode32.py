class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        method 1 stack
        1. 若当前遍历的值为 ( ，将 index 入栈，i.e. 记录 ( 的 index
        2. 若当前遍历的值为 ），出栈
            1. 若此时 stack 为空，说明不能匹配的值多了一个，将 ) 的 index 入栈
            2. 若此时 stack 不为空，重新计算最长的有效数 为 max(res, i-stack[-1])，计算中间有多少个有效的数

        :param s:
        :return:
        '''
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res

        '''
        method 2 dp
        
        if s[i] == ')' and s[i-1] == '('
            dp[i] = dp[i-2] + 2
        elif s[i] == s[i-1] == ')'
            dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
            
        需要理解，没太懂
        '''
        dp = [0] * (len(s))
        res = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
            res = max(res, dp[i])
        return res
