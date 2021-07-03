'''
lexicographically next permutation of numbers

Think of the list of numbers as a single integer. For example, think of [1,3,7,3,2] as 13732. Your goal is to create the next highest number, using only the same digits. In this case, the next biggest number is 17233. For more info, check out this link:

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

题意就是找到下一个，全排列组合中最小的数字
i.e. 找到一个大于当前序列的新序列，且变大的幅度尽可能小

1. 我们需要将一个左边的「较小数」和一个右边的「较大数」交换，使当前的排列变大
2. 同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后，「较大数」右边的数需要重新按照升序排列，保证新排列大于的同时，增长的幅度最小

这题理解起来稍微费劲
'''
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. 从右向左，找到第一个比右边数更小的较小数，设置其为 nums[left]
        2. 从右向左，找到第一个比 nums[left] 大的较大数，设置其为 nums[right]
        3. 交换 nums[left] 和 nums[right]
        4. 反转 nums[left + 1] 后面的数（本来是降序，将其变成升序，那么整个序列增加的幅度就是最小的）
        5. 如果整个nums 都是降序的，那么就省略 2-3，直接到第 4 步

        time O(n)
        space O(1)
        """
        if len(nums) < 2:
            return
        left = len(nums) - 2
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1

        if left >= 0:
            right = len(nums) - 1
            while nums[right] <= nums[left]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

        left, right = left + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()
print(s.nextPermutation([1, 2, 3]))
