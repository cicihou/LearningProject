# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.

        [1,2,3,4,5,6,7]
        [1,7,2,6,3,5,4]

        所以相当于是两个 链表的 merge [1,2,3,4], [7,6,5]

        步骤如下：
        1. find the median
        2. reverse second half
        3. merge
        """

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        flag = 0
        l1 = head
        l2 = prev  # 注意是 prev 存的反转之后的链表
        cur = dummy = ListNode()
        while l1 and l2:
            if flag % 2 == 0:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            flag += 1

        return dummy.next
