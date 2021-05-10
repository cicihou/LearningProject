class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        counts = Counter(nums)
        top_count = counts.most_common(k)
        res = [c[0] for c in top_count]
        return res

s = Solution()
s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
s.topKFrequent(nums = [1], k = 1)