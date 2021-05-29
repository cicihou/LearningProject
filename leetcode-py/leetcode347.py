class Solution(object):
    def topKFrequent(self, nums, k):
        ''' method 1 '''
        # from collections import Counter
        # counts = Counter(nums)
        # top_count = counts.most_common(k)
        # res = [c[0] for c in top_count]
        # return res

        ''' method 2'''
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        tmp = {}
        for key, v in dic.items():
            tmp.setdefault(v, []).append(key)

        res = []
        for i in range(k):
            key = max(tmp.keys())
            res.extend(tmp.pop(key))
            if len(res) == k:
                return res

        ''' method 3'''
        # TODO


s = Solution()
s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
s.topKFrequent(nums = [1], k = 1)
