class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        前置题：1047
        同时记录字符和出现次数
        '''
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i, 1])
            elif stack[-1][0] == i:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return ''.join([c*i for i, c in stack])


s = Solution()
print(s.removeDuplicates('aaccabbbc', 3))
