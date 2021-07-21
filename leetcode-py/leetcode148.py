# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        method 1 reverse linked list to array and sort
        :param head:
        :return:
        '''
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        cur = dummy = ListNode(-1)
        nodes.sort()

        for i in range(len(nodes)):
            cur.next = ListNode(nodes[i])
            cur = cur.next

        return dummy.next

        '''
        method 2 merge sort
        https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
        '''
        # TODO 
