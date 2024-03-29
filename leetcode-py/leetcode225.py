from collections import deque

'''
用两个 queue 实现一个栈，画一下比较容易明白
'''


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque([])
        self.help_q = deque([])
        self.peek = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        self.peek = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q) > 1:
            top = self.q.popleft()
            self.help_q.append(top)
            self.peek = top
        x = self.q.popleft()
        self.q, self.help_q = self.help_q, self.q
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.peek

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
