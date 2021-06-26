from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        相似题 300/674
        在 300 基础上改成二维，先求出最长的子数列
            if nums[right] > nums[left]
                if lengths[left] >= lengths[right]:
                    length[right] = lengths[left] + 1
                    count[right] = count[left]
                elif lengths[left] + 1 == lengths[right]:  # 连续子数组
                    counts[right] += counts[left]
        子序列的长度，i.e. length
        子序列的个数，i.e. count，有多少条路径可以走到当前的位置

        当满足右边的数 > 左边的数时：
            1. 如果 nums[left] 的子序列长度 >= nums[right]，说明找到了更长的子序列
                那么 nums[right] 要更新继承左边的个数，nums[right] 子序列长度在 left 基础上同步 + 1
            2. 如果 nums[left] 的子序列长度 + 1 就是 length [right] 的子序列长度
                说明找到了同样长的子序列（另一条路径），此时我们需要加上 left 对应的子序列个数

        Time O(n^2)
        Space O(n)
        '''
        n = len(nums)
        length = [1] * n
        counts = [1] * n
        for right in range(1, n):
            for left in range(right):
                if nums[right]>nums[left]:
                    if length[right] <= length[left]:
                        counts[right] = counts[left]
                        length[right] = length[left] + 1
                    elif length[right] == length[left] + 1:
                        counts[right] += counts[left]
        max_len = max(length)
        # res = 0
        # for i in range(len(length)):
        #     if length[i] == max_len:
        #         res += counts[i]
        res = sum(counts[i] for i in range(len(length)) if length[i] == max_len)
        return res

        '''
        method 2 Segment Tree 线段树
        '''
        # TODO


s = Solution()
s.findNumberOfLIS([1,3,5,4,7,7])
