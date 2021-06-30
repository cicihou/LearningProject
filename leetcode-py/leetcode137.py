from typing import List

from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        本题很简单，方法也很多
        time: O(n^2)
        space: O(1)
        '''
        for i in range(0, len(nums)):
            if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
                return nums[i]

    def singleNumber2(self, nums: List[int]) -> int:
        '''
        time: O(n^2), nums.count is a O(n)
        space: O(1)
        '''
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber3(self, nums: List[int]) -> int:
        '''
        time: O(n)
        space: O(n)
        '''
        dic = defaultdict(lambda: 0)
        for num in nums:
            dic[num] += 1
        for k, v in dic.items():
            if v == 1:
                return k


s = Solution()
print(s.singleNumber([2, 2, 3, 2]))
print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
