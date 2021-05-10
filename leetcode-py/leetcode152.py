class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) <= 1:
            return nums[0] or 0
        res = nums[0]
        base = 1
        for i in range(1, len(nums)):
            if res*nums[i] > res:
                res *= nums[i]
            else:
                res = 1
            base = max(res, base)
        if base == 1 and max(nums) == 0:
            return max(nums)
        return base

        # m2
        # maximum=big=small=nums[0]
        # for n in nums[1:]:
        #     big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        #     maximum=max(maximum, big)
        # return maximum

        # m3
        # rnums = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] *= nums[i-1] or 1
        #     rnums[i] *= rnums[i-1] or 1
        # return max(nums + rnums)



s = Solution()
print(s.maxProduct([2, 3, -2, 4]),6)
print(s.maxProduct([-2, 0, -1]), 0)
print(s.maxProduct([-2, 1, 0,1, -1]), 1)
print(s.maxProduct([0,0,0,-5,2]), 2)
print(s.maxProduct([-2]), -2)
print(s.maxProduct([-4,-3]), 12)
print(s.maxProduct([-2,-1,0,1]), 2)
print(s.maxProduct([-1,-1]), 1)
print(s.maxProduct([-1,-1,0]), 0)
print(s.maxProduct([-1,-1,1]), 1)
print(s.maxProduct([0,2]), 2)