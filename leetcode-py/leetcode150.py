import operator

class Solution:
    ''' 这题用栈来做
        其实准确来说应该是 math.ceil，只是刚好 int(val) 也拥有了这样的特性
        真正的算法不是不停用 testcase 去将涉及到的边界值的条件都覆盖到，elegant 的写法跟具体采用的思想相关
    '''
    def evalRPN(self, tokens) -> int:
        ops = {"+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.truediv}
        if len(tokens) == 1:
            return tokens[0]
        tmp = []

        # 需要注意数和运算符的顺序，后出栈的在左，先出栈的在右
        for i in tokens:
            if i not in ops:
                tmp.append(int(i))
            else:
                right, left = tmp.pop(), tmp.pop()
                tmp.append(int(ops[i](left, right)))

        return tmp


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]), 9)
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
print(s.evalRPN(["2","1","/","3","*"]), 6)
print(s.evalRPN(["0","1","/","3","*"]), 0)
print(s.evalRPN(["4","13","5","/","+"]), 6)
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
print(s.evalRPN(["18"]), 18)
print(s.evalRPN(["3","11","+","5","-"]), 9)


'''
wrong method

    一开始的思路中， 新赋值一个变量 val 记录栈顶，相当于当 val 有值之后，val就称为了栈顶(right)，当 val 没有值时，从 tmp.pop() 出栈顶。
    但是实际中，计算出来的值 val ，并不总是在栈顶(或者说 right)，也有可能是在 right
    这种写法就不能通过要求 val 不是 栈顶(right) 的情况 ["3","11","+","5","-"]
    需要用更加复杂的边界写法，相当于将问题复杂化了
        
        ops = {"+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.truediv}
        if len(tokens) == 1:
            return tokens[0]
        tmp = []
        val = None
        for i in tokens:
            if i not in ops:
                tmp.append(int(i))
            else:
                right = val if val is not None else tmp.pop()
                left = tmp.pop()
                val = int(ops[i](left, right))

        return val
'''
