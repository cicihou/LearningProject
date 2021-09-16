from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        从 lc 1054 改的
        :param s:
        :return:
        '''
        counter = Counter(s)
        items = sorted([(-val, key) for key, val in counter.items()])
        cur = []
        for v, k in items:
            cur += [k] * (-v)

        j = 0
        n = len(s)
        res = [''] * n
        for i in range(0, n, 2):
            res[i] = cur[j]
            j += 1
        for i in range(1, n, 2):
            res[i] = cur[j]
            j += 1
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                return ''
        return ''.join(res)
