# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        method 1 reverse linked list to array and sort
        :param head:
        :return:
        '''
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        cur = dummy = ListNode(-1)
        nodes.sort()

        for i in range(len(nodes)):
            cur.next = ListNode(nodes[i])
            cur = cur.next

        return dummy.next

        '''
        method 2 hashmap to count value
        '''
        cache = {}
        while head:
            cache[head.val] = cache.get(head.val, 0) + 1
            head = head.next
        dummy = cur = ListNode()
        for k in sorted(cache):
            for _ in range(cache[k]):
                cur.next = ListNode(k)
                cur = cur.next
        return dummy.next

        '''
        method 3 merge sort
        https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
        https://leetcode.com/problems/sort-list/solution/
        
        1. 找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法。对两个子链表分别排序。
        2. 将两个排序后的子链表合并，得到完整的排序后的链表。可以参考 lc 21，将两个有序的子链表进行合并。
        '''
        def merge_sort(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(merge_sort(head, mid), merge_sort(mid, tail))

        def merge(head1, head2):
            dummy = cur = ListNode()
            l1, l2 = head1, head2

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next

        return merge_sort(head, None)
