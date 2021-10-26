class Solution:
    def solve(self, nums, target):
        target = sum(nums) - target
        if target == 0:
            return len(nums)
        elif target < 0:
            return -1

        l = total = res = 0
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                res = max(res, r-l+1)
        return len(nums) - res if res > 0 else -1
