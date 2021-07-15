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
