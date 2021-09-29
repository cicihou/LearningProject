from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        ''' method 1
        counter
        '''
        counts = Counter(nums)
        top_count = counts.most_common(k)
        res = [c[0] for c in top_count]
        return res

        ''' method 2
        纯手写
        '''
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        tmp = {}
        for key, v in dic.items():
            tmp.setdefault(v, []).append(key)

        res = []
        for i in range(k):
            res += tmp.pop(max(tmp))
            if len(res) == k:
                return res

        ''' method 3
        note: 变量命名在同一个函数中千万千万不要重复，不要觉得在遍历的 形参 就没事
        counter + 手写，这种对 hashmap 的使用会比上面更好，没有改变 hashmap
        '''
        counter = Counter(nums)
        cache = {}
        for key, v in counter.items():
            cache.setdefault(v, []).append(key)
        res = []
        for i in sorted(cache, reverse=True):
            res += cache[i]
            k -= len(cache[i])
            if k == 0:
                return res
        return res


s = Solution()
s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
s.topKFrequent(nums = [1], k = 1)
