# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
method 1

这道题指针操作比较复杂，最主要是使用了三个中间变量，head, start, tail
head 记录需反转列表的第一个节点
start 记录需反转列表的上一个节点
tail 记录需反转列表的下一个节点（或者说是，下一个需反转列表的第一个节点，i.e. 下一次循环的 start）

https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/172576/Python-or-Follow-up-of-LC206

有点难理解，多画画图吧
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k <= 1:
            return head

        dummy = ListNode()
        dummy.next = head
        start = dummy

        while head:
            tail = start
            # 查看剩余部分长度是否大于等于 k，把 tail 节点向后定位 k 步
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next = tail.next
            head, tail = self.reverse(head, tail)
            start.next = head
            tail.next = next
            start = tail
            head = next
        return dummy.next

    def reverse(self, head, tail):
        # 翻转一个子链表，并返回新的头和尾
        terminal = tail.next
        cur = head
        pre = None
        while cur != terminal:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return tail, head


'''
method 2 递归 recursion
https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11653/Python-recursive-and-iterative-solutions-with-comments.
'''

# TODO
