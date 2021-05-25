# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        method 1
        双指针 prev 和 cur，前后差一步

        当节点重复时，prev.next 指向 cur.next（删除 cur 这个节点），cur 指向 next
        当节点不重复时，prev 和 cur 都向后移动一位
        '''
        # if head is None or head.next is None:
        #     return head
        # prev = head
        # cur = head.next
        # while prev and cur:
        #     next = cur.next
        #     if prev.val == cur.val:
        #         prev.next = next
        #         cur = next
        #     else:
        #         prev = cur
        #         cur = next
        # return head

        '''
        method 2 iteration straight forward
        note: if cur.val == cur.next.val: cur.next = cur.next.next
            in this step, dont move cur to its next, or it will skip continuous duplicate numbers
        '''
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
