class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        time: O(n)
        space: O(n)
        '''
        cache = {}
        cache2 = {}
        for a, b in trust:
            cache.setdefault(b, []).append(a)
            cache2.setdefault(a, []).append(b)
        for i in range(1, n + 1):
            if len(cache.get(i, [])) == n - 1 and cache2.get(i, 0) == 0:
                return i
        return -1
