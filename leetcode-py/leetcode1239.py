class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cache = {}
        res = 0
        for ch in arr:
            if len(ch) != len(set(ch)):
                continue
            tmp = {}
            for k in cache:
                if len(ch) + len(k) == len(set(ch + k)):
                    tmp[ch + k] = len(ch) + len(k)
                    res = max(res, tmp[ch + k])
            cache.update(tmp)
            cache[ch] = len(ch)
            res = max(res, cache[ch])
        return res
