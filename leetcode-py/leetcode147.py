# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        method 1 reverse linked list to array and sort
        投机取巧法
        '''
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        dummy = cur = ListNode()
        nodes.sort()
        for val in nodes:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

        '''
        method 2 insertion sort
        插入排序：维护一个有序序列，
                初始时有序序列只有一个元素，每次将一个新的元素插入到有序序列中，有序序列的长度增加 1，直到全部元素都加入到有序序列中。
        
        time: O(n^2)
        space: O(n)
        
        1. 维护三个指针，dummy(虚拟头), lastSorted(指向第一个元素/头节点), cur(指向第二个元素)
        2. 遍历 cur （cur 及更之后的就是需要排序的链表）
            1. 如果 cur.val < dummy.next，就将 cur.val 插入最前面
            2. 如果 cur.val >= lastSorted.val，就将 cur.val 插入到有序序列的最后面（由于我们遍历的是 cur，相当于原地不动）
            3. 如果 dummy.next < cur.val < lastSorted.val，表示 cur.val 的值应该在有序数列的中间，我们遍历有序数列找到这个值
        3. 返回 dummy.next
        '''

        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        lastSorted = head
        cur = head.next

        while cur:
            if lastSorted.val <= cur.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next

        return dummy.next
