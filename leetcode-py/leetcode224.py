class Solution:
    def calculate(self, s: str) -> int:
        '''
        虽然只有加减法，理论上说括号带来的先后性对结果不造成任何影响
        但是 testcase 有这样的，因此还是要考虑括号的先后
        "- (3 + (4 + 5))"
        用 num 表示当前记录的数字，用 res 表示当前记录的结果，用 sign 记录符号位

        因此在遇到左括号时，把当前的res 值入栈，sign 也入栈（sign 记录的是 res跟括号之间的符号）
        将 res 重置为 0，sign 重置为 1 ，括号相当于重置了正负的符号

        在遇到右括号的时候，用 res += sign * num （当前括号的数计算完毕）
        重置 num
        此时 res 表示是括号对应的值，先 * 我们之前存的符号位，然后再加上之前存的数

        time: O(n)
        space: O(n)
        '''
        stack = []
        num = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in ('+', '-'):
                res += sign * num
                num = 0
                sign = 1 if ch == '+' else '-1'
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        res += sign * num
        return res
