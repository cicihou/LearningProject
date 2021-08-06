'''
需要频繁进行增删，并且还要元素有序，所以直接使用双向链表（方便进行增删操作）
为了逻辑上的统一，设置一个空的头节点与尾节点
内部再设置一个变量存当前节点个数（每次对节点增删时同步更新），方便判满与判空
剩下的操作都是链表的插入删除操作
'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.pre = self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.current_vol = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.head.pre = self.tail
        self.tail.next = self.head
        self.tail.pre = self.head

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        new_node = Node(value)
        next = self.head.next
        self.head.next = new_node
        new_node.pre = self.head
        new_node.next = next
        next.pre = new_node
        self.current_vol += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        new_node = Node(value)
        prev = self.tail.pre
        prev.next = new_node
        new_node.pre = prev
        new_node.next = self.tail
        self.tail.pre = new_node
        self.current_vol += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.current_vol -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = self.tail.pre
        self.current_vol -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.tail.pre.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.current_vol == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.current_vol == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
