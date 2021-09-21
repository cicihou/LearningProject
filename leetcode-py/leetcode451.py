class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        res = ''
        hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        for k, v in hashmap:
            res += k * v
        return res

        '''
        to make it simple
        '''
        counter = Counter(s)
        cache = sorted([(-v, k) for k, v in counter.items()])
        res = ''
        for count, key in cache:
            res +=  -count * key
        return res
