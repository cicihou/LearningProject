'''
method 1
time:
insert O(1)
sum O(N * S)

space:
O(N)

数据量足够大的时候，本题可以用 Trie 优化
'''

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for k, v in self.hashmap.items():
            if k.startswith(prefix):
                res += v
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


'''
method 2

Trie

如果同时 insert 两次 apple，相当于在 Trie 上修改了 apple 对应的 count
因此需要用一个 map 来记录哪些值是已经输入过进行的update( += diff )，
                      哪些值 是完全 insert( += val ) 的新增
'''

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class MapSum2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        root = self.root
        root.count += diff
        for ch in key:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
            root.count += diff

    def sum(self, prefix: str) -> int:
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return 0
            root = root.children[ch]
        return root.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


obj = MapSum2()
obj.insert('apple', 2)
obj.insert('app', 3)
obj.sum('ap')
