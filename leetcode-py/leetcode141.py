# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ''' method 1'''
        # dic = {}
        # while head:
        #     if head not in dic:
        #         dic[head] = None
        #     else:
        #         return True
        #     head = head.next
        # return False

        ''' method 2 slow/fast pointer'''
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
