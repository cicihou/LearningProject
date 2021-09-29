from itertools import zip_longest


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        res = []
        for i, j in zip_longest(even, odd):
            res.append(i)
            res.append(j)
        return res
