class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        '''
        这里不能排序，因为其求的是最小的 subarray ，要求要按其原顺序
        method 1 two pointer
        '''
        count = float('inf')
        s = 0
        left = 0
        for i in range(len(nums)):
            # to make edge case faster
            if nums[i] >= target or count == 1:
                return 1

            s += nums[i]
            while s >= target:
                count = min(count, i - left + 1)
                s -= nums[left]
                left += 1

        return count if count != float('inf') else 0


s = Solution()

# s.minSubArrayLen(7, [2,3,1,2,4,3])
# s.minSubArrayLen(4, [1,4,4])
# s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])
# s.minSubArrayLen(11, [1,2,3,4,5])
print(s.minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
