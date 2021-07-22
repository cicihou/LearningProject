# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        method 1
        time: O(n)
        space: O(n)

        从 lc2 修改得来的，也可以直接新建一个 ListNode，然后依次从 stack1, stack2 pop 而出进行加和
        我这里是直接复用了更长的那个
        '''
        stack1 = []
        stack2 = []

        while l1 or l2:
            if l1:
                stack1.append(l1)
                l1 = l1.next
            if l2:
                stack2.append(l2)
                l2 = l2.next
        if len(stack1) > len(stack2):
            stack, tmp = stack1, stack2
        else:
            stack, tmp = stack2, stack1
        flag = 0
        for i in range(1, len(stack) + 1):
            j, k = len(stack) - i, len(tmp) - i
            val = tmp[k].val if k >= 0 else 0
            s = stack[j].val + val + flag
            flag = s // 10
            stack[j].val = s % 10

        if flag:
            head = ListNode(flag)
            head.next = stack[0]
            stack.insert(0, head)
        return stack[0]

        '''
        method 2 
        
        直接计算出对应的 integer，将其变成新的 ListNode
        '''
        n1 = n2 = 0
        while l1:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2 * 10 + l2.val
            l2 = l2.next

        total = str(n1 + n2)

        cur = dummy = ListNode()
        for ch in total:
            cur.next = ListNode(int(ch))
            cur = cur.next

        return dummy.next
