from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        res = float('inf')
        for k, v in counter.items():
            if v == 1:
                res = min(res, s.index(k))
        return res if res != float('inf') else -1
