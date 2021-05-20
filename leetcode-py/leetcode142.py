# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ''' method 1 via hash'''
        # i = 0
        # dic = {}
        # while head:
        #     if head in dic:
        #         return head
        #     else:
        #         dic[head] = i
        #         i += 1
        #     head = head.next

        ''' method 2 via fast/slow pointer'''
        fast = slow = head
        while fast:
            if not (fast and fast.next and fast.next.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                break
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
