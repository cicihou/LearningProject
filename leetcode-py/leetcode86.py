# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ''' 略微借鉴了 21 mergeTwoSortedList 的比较思想'''
        mid = large = ListNode()
        dummy = small = ListNode()
        while head:
            if head.val < x:
                small.next = ListNode(head.val)
                small = small.next
            else:
                large.next = ListNode(head.val)
                large = large.next
            head = head.next
        small.next = mid.next
        return dummy.next
