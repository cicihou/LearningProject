# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ''' method1
        假设 pa 是短指针，如果短指针遍历完毕，就从更长的那一个 linked list 重新开始走

        如果有相交
        这样 相当于拼了一个超长的链表 A(a_start + common) + B(b_start + common)
        也就是无论 a_start 和 b_start 有多长，两个指针遍历结果的都是一样的
        pa 的遍历为：a_start + common + b_start + common
        pb 的遍历为：b_start + common + a_start + common
        如果有相交，在最后一段 common 时，pointer 一定会达成 pa == pb 的循环推出条件

        如果没有相交，
        相当于遍历了两个链表
        '''
        if not headA or not headB:
            return

        pa = headA
        pb = headB

        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa
