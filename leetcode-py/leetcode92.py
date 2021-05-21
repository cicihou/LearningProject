# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
1. 把 cur 拨到 left 所在位置节点
2. 保存 cur(start) 以及 cur.next(end)
3. 将 linked_list[left, right] 中的节点倒转
4. connect

很不错的白板教程讲解: https://www.youtube.com/watch?v=wk8-_M-2fzI
'''


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        '''
        method 1
        多画图，注意指针节点的位置，避免成环
        将链表分为三段 LinkedListLeft + ReversedLinkedList + LinkedListRight
            i.e. left + reversed + right
        在需要反转的局部链表进行反转前 保存了 cur(start) 和 cur.next(end)
        start 相当于 left 的最后一个节点
        end(cur.next) 相当于 reversed 反转前的头，反转后的尾节点，用来接 right 链表
        '''
        if not head or not head.next or left == right:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        pre = None
        index = 0
        start = end = None
        while cur:
            next = cur.next
            if left <= index <= right:
                cur.next = pre
                pre = cur
            else:
                start = cur
                end = cur.next
            cur = next
            if right == index:
                break
            index += 1
        start.next = pre
        end.next = cur
        return dummy_head.next


        '''
        method 2
        思想上和 method 1 类似，这种解法用 m 和 n 统计遍历次数
        注意 range 和 xrange 都是 [}，计算循环次数时候需要小心一下边界条件
        而非直接操作链表节点来计数
        
        这种方法更不容易出现环，因为只有在链表逆转的时候才需要操作指针
        但是需要更加注意 start 和 end 的位置

        https://leetcode.com/problems/reverse-linked-list-ii/discuss/30681/Python-one-pass-concise-solution-with-comments.
        '''
        # Edge
        if not head or not head.next or left == right:
            return head

        # set starting point
        dummy_head = ListNode()
        dummy_head.next = head
        start = dummy_head
        for i in range(left - 1):
            start = start.next

        # set ending point
        end = cur = start.next

        # reverse
        prev = None
        for i in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # connnect
        start.next = prev
        end.next = cur
        return dummy_head.next


head = node = ListNode(1)
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)

s = Solution()
s.reverseBetween(head, 2, 4)
