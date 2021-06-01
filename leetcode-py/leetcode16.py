class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        '''
        method 1
        排序后用左右指针不断进行比较，缩小范围
            将 「target」 和 「三数之和sum」 之间的差值设为 diff
            diff 越小表示越接近，diff = target - sum(three closest number)
            当 「三数之和sum」小于 target，left 指针右移（表示取一个相对更大一点的数）
            当 「三数之和sum」大于 target，right 指针左移（表示取一个相对更小一点的数）
        注意，不能用 sliding window，因为sliding window 是连续的，无法保证一定能找到最接近的数
        '''
        nums.sort()
        i = 0
        diff = float('inf')
        while i < len(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = sum([nums[i], nums[l], nums[r]])
                if tmp == target:
                    return target
                if abs(target-tmp) < abs(diff):
                    diff = target - tmp
                if tmp < target:
                    l += 1
                else:
                    r -= 1
            i += 1
        return target - diff


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
print(s.threeSumClosest([2, 2, 6, 8], 4), 10)
print(s.threeSumClosest([-3, -2, -5, 3, -4], -1), -2)
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82), 82)

