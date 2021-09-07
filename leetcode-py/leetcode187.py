class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cache = {}
        res = set()
        for i in range(len(s)-9):
            key = s[i:i+10]
            if key in cache:
                res.add(key)
            cache[key] = cache.get(key, 0) + 1
        return res
