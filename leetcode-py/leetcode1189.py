from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text) // len('balloon') + 2
        target = Counter('balloon')
        counter = Counter(text)
        res = 0
        for _ in range(n):
            for k, v in target.items():
                if k in counter and counter[k] - v >= 0:
                    counter[k] -= v
                else:
                    break
                if counter[k] == 0:
                    del counter[k]
            else:
                res += 1
        return res

        '''
        一个跟 lambda 和 filter 写法相关的优化
        '''
        target = {'b': 1, 'a': 1, 'n': 1, 'o': 2, 'l': 2}
        counter = Counter(text)
        res = 0

        def func(key):
            if key in counter:
                counter[key] -= target[key]
                return counter[key] >= 0

        while len(list(filter(lambda x: x is True, map(func, target.keys())))) == len(target):
            res += 1
        return res
