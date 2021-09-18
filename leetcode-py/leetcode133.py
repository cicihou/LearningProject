"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        method 1 DFS

        1. 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        2. 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        3. 哈希表存储
        4. 遍历该节点的邻居并更新克隆节点的邻居列表
        '''
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]
        new_node = Node(node.val, [])

        self.visited[node] = new_node

        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return new_node
