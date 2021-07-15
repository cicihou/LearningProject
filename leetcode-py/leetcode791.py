class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        res = ''
        for ch in order:
            if ch in hashmap:
                res += hashmap[ch] * ch
                hashmap.pop(ch)
        for k, v in hashmap.items():
            res += k*v
        return res
