import random


class Node:
    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down


class Skiplist:
    '''
    跳表，这个结构有点难，我不太理解
    '''
    def __init__(self):
        self.head = Node(None)

    def search(self, target: int) -> bool:
        head = self.head
        while head:
            while head.next and head.next.val < target:
                head = head.next
            if not head.next or head.next.val > target:
                head = head.down
            else:
                return True
        return False

    def add(self, num: int) -> None:
        stack = []
        head = self.head
        while head:
            while head.next and head.next.val < num:
                head = head.next
            stack.append(head)
            head = head.down
        needInsert = True
        downNode = None
        while needInsert and len(stack):
            pre = stack.pop()
            pre.next = Node(num, pre.next, downNode)
            downNode = pre.next
            needInsert = random.random() < 0.5
        if needInsert:
            self.head = Node(None, Node(num, None, downNode), self.head)

    def erase(self, num: int) -> bool:
        head = self.head
        seen = False
        while head:
            while head.next and head.next.val < num:
                head = head.next
            if not head.next or head.next.val > num:
                head = head.down
            else:
                seen = True
                head.next = head.next.next
                head = head.down
        return seen

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
