# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

        ''' method 2 遍历，操作节点（via dummy head）
        https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode
        '''

        if not head or not head.next:
            return head
        cur = ListNode()
        cur.next = head
        res = cur
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return res.next
