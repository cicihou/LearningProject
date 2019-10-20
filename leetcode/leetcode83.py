# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        prev_node = cur
        curr_node = cur.next
        while prev_node and curr_node:
            if prev_node.val == curr_node.val:
                # 这里的坑在于，curr_node 必须也重新赋值，不然循环无法继续正确往下走
                prev_node.next = curr_node.next
                curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return cur
