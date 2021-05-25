# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        method 1
        两次循环，
        第一次找到所有重复的数，存进 dict，并且将重复的数删至只剩一个
        第二次遍历链表，删去所有 dict 中有的值
        需要注意，node.val 的范围是 [-100, 100]，而 ListNode() 默认的 val 为 0
        因此在创建 dummy 的时候，要么显式的赋值其不符合 node.val 的范围，要么第一次循环遍历从 head 开始
        '''
        # dummy = ListNode(float('-inf'))
        # dummy.next = head
        # cur = head
        #
        # dic = {}
        # while cur and cur.next:
        #     if cur.val == cur.next.val:
        #         dic[cur.val] = None
        #         cur.next = cur.next.next
        #     else:
        #         cur = cur.next
        #
        # if dic:
        #     prev = dummy
        #     cur = head
        #     while cur:
        #         if cur.val in dic:
        #             prev.next = cur.next
        #             cur = cur.next
        #         else:
        #             prev = cur
        #             cur = cur.next
        # return dummy.next

        '''
        method 2
        了解一下 lc 的命名法
        sentinel 哨兵，表示虚拟头节点
        predecessor 前任，前辈，i.e. prev
        
        这个的双节点移动很巧妙，实质上就是快慢指针法
        cur 记录的是出现重复元素之前的一个节点，head 记录的是出现重复的最后一个节点
        cur.next = head.next 就完成了跳表
        辅助画图，便于理解
        
        时间 O(n)，空间 O(1) 因为其未额外使用任何空间
        
        如果这个方法的命名不好理解，可以参考，都是用了快慢指针法：
        https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1002902/Python-2-pointers-solution-explained
        https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28398/clean-python-solution-involving-dummy-node
        这些用了更多变量，代码上更加清晰
        '''
        dummy = ListNode(-200, head)

        cur = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
        return dummy.next
