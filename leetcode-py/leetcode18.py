from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        time: O(n^3)
        space: O(n), n // 4 依然是 n

        target - sk < nums[-1] 这里是一个剪枝，如果 已经比最大的数还大，没必要再往下算了
        '''
        nums.sort()

        if len(nums) < 4:
            return []

        res = set()

        for i in range(len(nums)-3):
            si = nums[i]
            for j in range(i+1, len(nums)-2):
                sj = si + nums[j]
                for k in range(j+1, len(nums)-1):
                    sk = sj + nums[k]
                    if target - sk < nums[-1] and target - sk in nums[k+1:]:
                        res.add(tuple([nums[i], nums[j], nums[k], target-sk]))

        return res


s = Solution()
s.fourSum([1,0,-1,0,-2,2], 0)
s.fourSum([0,0,0,0], 0)
