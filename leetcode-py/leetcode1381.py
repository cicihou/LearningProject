class CustomStack:

    # def __init__(self, maxSize: int):
    #     self.max_size = maxSize
    #     self.item = []
    #
    # def push(self, x: int) -> None:
    #     if len(self.item) < self.max_size:
    #         self.item.append(x)
    #
    # def pop(self) -> int:
    #     if self.item:
    #         return self.item.pop()
    #     return -1
    #
    # def increment(self, k: int, val: int) -> None:
    #     length = len(self.item)
    #     for i in range(length):
    #         # attention: it should be <, cannot equals to
    #         # k is the volume starts from 1, while index start from 0
    #         if i < min(k, length):
    #             self.item[i] += val

    ''' method 2 differnce method(DM) 差分法, much more fast
        两个数组记录，一个数组记录直接推入的 stack 值，另一个记录 差值
        当 pop 的时候，将两个数组的值相加即可
        由于是从栈底开始加，只有实际调用 pop 统计上一次的差分
    '''
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        res = self.stack.pop() + self.inc.pop()
        print(res)
        return res

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
        print(self.inc)


s = CustomStack(3)
s.push(1)
s.push(2)
s.pop()
s.push(2)
s.push(3)
s.push(4)
s.increment(5, 100)
s.increment(2, 100)
s.pop()
s.pop()
s.pop()
