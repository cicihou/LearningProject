class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': -1, ')': 1, '{': -2, '}': 2, '[': -3,  ']':3}
        item = []
        total = 0
        # prune: 当 s 长度为奇数时无需进行计算
        if len(s) % 2 != 0:
            return False

        for letter in s:
            n = parentheses[letter]
            total += n
            if n < 0:
                item.append(n)
            if n > 0 and item and item.pop() + n != 0:
                return False
        return not item and total == 0


        '''
        stack
        '''
        stack = []
        combo = {'}': '{', ')': '(', ']': '['}
        for i in range(len(s)):
            if stack and combo.get(s[i]) == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0


s = Solution()
print(s.isValid("()"),'t')
print(s.isValid("()[]{}"),'t')
print(s.isValid("(]"),'f')
print(s.isValid("([)]"),'f')
print(s.isValid("{[]}"),'t')
print(s.isValid("{"),'f')
print(s.isValid("}"),'f')
print(s.isValid("}}"),'f')
