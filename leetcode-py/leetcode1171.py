# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        '''
        Prefix Sum
        两次遍历，
        第一次将数字的前缀和添加进入 hashmap，k 为 prefix_sum， value 为最后一个满足这个 prefix_sum 的节点
        第二次遍历，如得到跟 hashmap 中的相同的前缀和，表示中间这一段节点的和为0，因此可以直接跳过
         Go from the dummy node again to set the next node to be the last node for a prefix sum
        Note⚠️: 本身 value 为 0 的节点也需要跳过，所以第二次遍历从 dummy 开始
        '''
        prefix_sum = {}
        s = 0
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            s += cur.val
            prefix_sum[s] = cur
            cur = cur.next

        cur = dummy
        s = 0
        while cur:
            s += cur.val
            cur.next = prefix_sum[s].next
            cur = cur.next

        return dummy.next


head = ListNode(0)
s = Solution()
s.removeZeroSumSublists(head)
