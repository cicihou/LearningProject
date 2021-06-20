# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        method 1
        直接照抄 21 题，遍历 lists，进行两两排序合并成 K 个数组排序
        注意 dummy 初始化的时候要是一个排在最小的值
        '''
        ans = ListNode(float('-inf'))

        def mergeTwoLists(l1, l2):
            if not l1 or not l2:
                return l1 or l2

            dummy = ListNode()
            cur = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur = cur.next
            if l1 or l2:
                cur.next = l1 or l2
            return dummy.next

        for l in lists:
            mergeTwoLists(ans, l)
        return ans.next


        '''
        method 2 MultiDict
        原创的噢 XD，通过了，还比上种方法快很多
        lc 官方提供的 priority queue 的方法由于自定义结构不支持比较，在不重写 queue 结构的前提下已经失效
        我觉得这种方法有点类似于 priority queue，不过是用另一种结构实现的
        '''
        dic = {}
        for l in lists:
            if l:
                dic.setdefault(l.val, []).append(l)

        dummy = ListNode()
        cur = dummy
        while dic:
            min_val = min(dic)
            values = dic.pop(min_val)
            for l in values:
                # 节点赋值
                cur.next = ListNode(min_val)
                cur = cur.next
                # 链表遍历
                l = l.next
                if l:
                    dic.setdefault(l.val, []).append(l)
        return dummy.next
