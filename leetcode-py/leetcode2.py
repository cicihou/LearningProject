# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
concise solution：https://leetcode.com/problems/add-two-numbers/discuss/1032/Python-concise-solution.
tricky: https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode()
        cur = dummy
        flag = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + flag
            flag = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if flag:
            cur.next = ListNode(flag)
        return dummy.next
