# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        method 1
        快慢指针法
        https://leetcode-cn.com/problems/rotate-list/solution/dong-hua-yan-shi-kuai-man-zhi-zhen-61-xu-7bp0/
        
        首先计算 k 是否大于链表长度，若大于，则取余
        e.g. 链表长度为 5，k 为18，则 18 % 5 = 3，就可以把问题中的 k 简化成 3
        
        慢指针 始终比 快指针 慢了 k 步，于是 当快指针走到结尾时，慢指针停下来的点就是 len(linked_list) - k
        也符合题意，rotate the list to the right by k places.
        将最右边的 k 个席位 拼来左边
        '''
        # if not (head and head.next):
        #     return head
        #
        # length = 0
        # cur = head
        # while cur:
        #     length += 1
        #     cur = cur.next
        # k = k % length
        #
        # fast = slow = head
        # while fast.next:
        #     if k <= 0:
        #         slow = slow.next
        #     fast = fast.next
        #     k -= 1
        # fast.next = head
        # head = slow.next
        # slow.next = None
        # return head


        ''' method 2 操作节点，先找出 关键的 k th 节点，然后将 k 节点之前的链表拼到 k th 后面去
        https://leetcode.com/problems/rotate-list/discuss/883252/Python-O(n)-solution-explained
        
        我觉得这种方法其实不太好理解，而且操作边界值挺容易出错的
        '''
        # if not (head and head.next):
        #     return head
        #
        # length = 0
        # last = head
        #
        # # 便于理解，用 tail 记录一下尾部节点
        # # 若直接用 last 记录尾部节点: 则循环条件为 while last.next 且 length 初始值为 1
        # while last:
        #     length += 1
        #     tail = last
        #     last = last.next
        # k = k % length
        #
        # # 这一句很重要，不可省略，不然 middle 的循环会变成 range(length - 1)，比正常的就少走了一步
        # if k == 0:
        #     return head
        #
        # middle = head
        # for i in range(length - k - 1):
        #     middle = middle.next
        # new_head = middle.next
        # tail.next = head
        # middle.next = None
        # return new_head


        '''
        method 3
        这个是对 method 2 的简化；将整个head 先拼起来，节约了节点操作
        https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
        
        这个方法很巧妙也很聪明，多画画图理解
        '''
        if not (head and head.next):
            return head
        last = head
        # 关于这里 length = 1 可以参考 method 2
        length = 1
        while last.next:
            last = last.next
            length += 1
        k = k % length

        # 生成了一个环
        last.next = head

        tmp = head
        for _ in range(length - k - 1):
            tmp = tmp.next

        # 相当于 res 是头节点，tmp 指向 None 后变成尾节点
        res = tmp.next
        tmp.next = None

        return res
