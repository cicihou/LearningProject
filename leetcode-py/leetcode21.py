# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
链表合并问题

Simple 5 lines Python：
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        method1, iteration

        time: O(n+m)
        space: O(1)
        '''
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 or l2:
            cur.next = l1 or l2
        return dummy.next

        '''
        method2, recursion
        
        time: O(n+m)
        space: O(n+m)
        '''
        if l1 is None or l2 is None:
            return l1 or l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
