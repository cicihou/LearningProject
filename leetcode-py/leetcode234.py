# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        method 1

        time: O(N)
        space: O(N)

        :param head:
        :return:
        '''
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes = ''.join([str(i) for i in nodes])
        return nodes == nodes[::-1]

        '''
        method 2
        '''
        if not head.next:
            return True
        fast = slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        cur = slow

        while cur:
            if stack and cur.val != stack.pop():
                return False
            cur = cur.next
        return True
