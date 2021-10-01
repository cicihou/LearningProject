# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        '''
        这题的关键就在于 ans + (i < remainder) - 1 这里是一个动态的值，
        在循环到第一个链表（有余数且循环还在余数范围内的时候）不需要 -1
        在循环到后面的链表时需要 -1

        这里比较难想

        time: O(N)
        space: O(N)

        :param head:
        :param k:
        :return:
        '''
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        res = []
        cur = head
        remainder = length % k
        ans = length // k
        for i in range(k):
            dummy = None
            if cur:
                dummy = cur
                for _ in range(ans + (i < remainder) - 1):
                    if cur:
                        cur = cur.next
                prev = cur
                if cur:
                    cur = cur.next
                prev.next = None
            res.append(dummy)

        return res
