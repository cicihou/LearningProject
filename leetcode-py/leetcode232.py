class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.

        如果用栈的思想来做，栈在 push 不能保证先入先出的
        每一次要用一个help_stack 实现栈的翻转
        while self.stack:
            self.help_stack.append(self.stack.pop())
        self.help_stack.append(x)
        while self.help_stack:
            self.stack.append(self.help_stack.pop())
        """
        self.item.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.item.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.item[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.item) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
