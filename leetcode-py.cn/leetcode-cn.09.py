'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

维护两个栈，一个主栈用来存放数据，另外一个作为辅助栈
当 push 数据时，直接 push 到主栈就好了
当 pop 时，看辅助栈内有没有数据，有就直接 pop
辅助栈没数据时就将主栈的数据依次 push 进辅助栈，然后再 pop

https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

题解思路：
维护两个栈，一个主栈用来存放数据，另外一个作为辅助栈
当 push 数据时，直接 push 到主栈就好了
当 pop 时，看辅助栈内有没有数据，有就直接 pop
辅助栈没数据时就将主栈的数据依次 push 进辅助栈，然后再 pop
'''


class CQueue:

    def __init__(self):
        self.stack = []
        self.help_stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if self.help_stack:
            return self.help_stack.pop()
        else:
            if self.stack:
                while self.stack:
                    self.help_stack.append(self.stack.pop())
                return self.help_stack.pop()
            else:
                return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
