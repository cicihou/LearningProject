class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': -1, ')': 1, '{': -2, '}': 2, '[': -3,  ']':3}
        item = []
        sum = 0
        for letter in s:
            n = parentheses[letter]
            sum += n
            if n < 0:
                item.append(n)
            if n > 0:
                if item and item.pop() + n == 0:
                    continue
                else:
                    return False
        if item or len(s) % 2 != 0 or sum != 0:
            return False
        return True

s = Solution()
print(s.isValid("()"),'t')
print(s.isValid("()[]{}"),'t')
print(s.isValid("(]"),'f')
print(s.isValid("([)]"),'f')
print(s.isValid("{[]}"),'t')
print(s.isValid("{"),'f')
print(s.isValid("}"),'f')
print(s.isValid("}}"),'f')