from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        time: O(n)
        space: O(n)
        '''
        res = defaultdict(lambda: 0)
        for num in nums:
            res[num] += 1
        return [k for k, v in res.items() if v == 1]
