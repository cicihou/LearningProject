class Solution:
    def productExceptSelf(self, nums):
        from operator import mul
        from functools import reduce
        product = reduce(mul, [num for num in nums[:] if num != 0], 1)
        count = nums.count(0)
        if count > 1:
            return [0] * len(nums)
        elif count == 1:
            res = [0] * len(nums)
            res[nums.index(0)] = product
            return res
        else:
            res = []
            for i in nums[:]:
                re = product // i
                res.append(re)
        return res

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]), '[24, 12, 8, 6]')
print(s.productExceptSelf([0, 2, 3, 4]), '[24, 0,0,0]')
print(s.productExceptSelf([0, 2, 3, 0]), '[0,0,0,0]')