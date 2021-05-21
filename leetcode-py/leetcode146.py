class DoubleLinkedListNode:
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.next = self.prev = None


'''
双向链表 + hashtable 讲的特别清楚的一个视频
https://www.youtube.com/watch?v=S6IfqDXWa10

思路：
双向链表，创建 dummy_head 和 dummy_tail
核心在于，
put 要方便删除尾巴(tail)，
get/put 方便的把元素移到头部(head): i.e. 在链表原有位置删除元素 + 在头部新增
在双向链表中，我们都可以通过操作指针完成

hashtable 中 k 存储题目中的key, v 存储节点 node
当需要获取 val 的时候，通过 node.val 获取

也可以直接写，但是避免出错，最好是将 add_head/remove_tail/remove_node 三个方法抽象出来写
注意，双向链表在增加和删除的时候，需要操作 3 个节点(prev, cur, next)的 4 个指针
分别是 prev.next, cur.prev, cur.next, next.prev

如果是删除，
prev.next = next
next.prev = prev
这样就自然去掉了 中间的节点

如果是增加，假设 cur = new_node
操作以下四个节点就可以完成
prev.next = cur
next.prev = cur
cur.next = next
cur.prev = prev


还有个解法是 python 的 ordered dict 
相当于用 python 内置的 advanced structure 完成了 double linked list
ordered dict 本身就是基于 double linked list 实现的
https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashtable:
            node = self.hashtable[key]
            self.remove_node(node)
            self.add_head(node)
            return node.v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]
            node.v = value
            self.remove_node(node)
            self.add_head(node)
        else:
            new_node = DoubleLinkedListNode(key, value)
            if len(self.hashtable) >= self.capacity:
                self.remove_tail()
            self.hashtable[key] = new_node
            self.add_head(new_node)

    def add_head(self, node):
        '''
        将 传入的 node 放到头部
        :param node:
        :return:
        '''
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def remove_node(self, node):
        '''
        将传入的 node 在原有位置删除
        :param node:
        :return:
        '''
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def remove_tail(self):
        '''
        删除双向链表的尾巴
        :return:
        '''
        node = self.tail.prev
        self.remove_node(node)
        del self.hashtable[node.k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
