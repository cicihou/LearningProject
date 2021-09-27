class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        cache = {}
        for x, y in points:
            dis = x ** 2 + y ** 2
            cache.setdefault(dis, []).append([x, y])
        res = []
        i = 0
        for tmp in sorted(cache):
            res += cache[tmp]
            i += len(cache[tmp])
            if i >= k:
                return res
