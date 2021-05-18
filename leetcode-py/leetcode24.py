# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        method 1 递归，请参考这个视频：https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dong-hua-yan-shi-die-dai-yu-di-gui-liang-ha0u/
        :param head:
        :return:
        '''
        if not head or not head.next:
            return head
        while head and head.next:
            pairs = self.swapPairs(head.next.next)
            next_pairs = head.next
            next_pairs.next = head
            head.next = pairs
            return next_pairs
