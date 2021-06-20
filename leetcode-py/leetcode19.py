# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        two-pointer
        注意两个循环要分开写
        '''
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        nxt = slow.next
        if nxt:
            slow.next = slow.next.next
        else:
            slow.next = None
        return dummy.next
