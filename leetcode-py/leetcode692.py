class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cache = {}
        for word in words:
            cache[word] = cache.get(word, 0) + 1
        ans = {}
        for key, v in cache.items():
            ans.setdefault(v, []).append(key)
        res = []
        while len(res) < k:
            tmp = ans.pop(max(ans))
            if len(res) + len(tmp) <= k:
                res += sorted(tmp)
            else:
                res += sorted(tmp)[:k-len(res)]

        return res
