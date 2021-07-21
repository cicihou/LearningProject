"""
遍历两次，第一次将链表中的所有节点映射到 hashmap
第二次将映射节点中的 random 和 next 赋值

beautiful solution
https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution

time: O(n)
space: O(n)
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        method 1
        time: O(N), 2N is N
        space: O(N)
        :param head:
        :return:
        '''
        cache = {}
        cur = curr = head
        while cur:
            cache[cur] = Node(cur.val)
            cur = cur.next

        while curr:
            cache[curr].next = cache.get(curr.next)
            cache[curr].random = cache.get(curr.random)
            curr = curr.next

        return cache.get(head)

        '''
        method 2
        
        shorter than method 1
        将 cache 变成 defaultdict, 将循环和赋值同时发生
        直接给 cache[n] 赋值 val, next, random
        time: O(n)
        space: O(n)
        '''
        cache = collections.defaultdict(lambda: Node(0))
        n = head
        cache[None] = None
        while n:
            cache[n].val = n.val
            cache[n].next = cache[n.next]
            cache[n].random = cache[n.random]
            n = n.next
        return cache[head]
