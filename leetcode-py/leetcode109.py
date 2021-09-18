'''
the problem is to convert LinkedList to Tree
it could be divided into 2 problems

1. how to find the median value from a linked list, and cut it into two linked list
2. how to construct a BST from ordered list(108)

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head) -> TreeNode:
        '''
        time: O(nlogn)
        space: O(logn)

        :param head:
        :return:
        '''
        if not head:
            return head
        if not head.next:
            # 注意此处也是需要用 treeNode 返回的
            return TreeNode(head.val)

        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

        '''
        method 2
        ordered linked list 遍历完缓存起来，key 是其 index
        这样我们直接构造一个树，每一次就取index 的median 就好（知道length 可以很快求中点）
        
        time: O(n), 递归树每个节点的时间复杂度为 O(1)，每次处理一个节点，因此总的节点数就是 n， 也就是说总的时间复杂度为O(n)
        space: O(n)，缓存了整个 linked list
        
        代码：https://leetcode-solution.cn/solutionDetail?type=3&id=9&max_id=2
        '''
        # TODO
