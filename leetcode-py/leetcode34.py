class Solution:
    def searchRange(self, nums, target: int):
        '''
        binary search
        '''
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                # l <= mid <= r，考虑不断收缩 l 和 r 达到正确的范围
                while l >= 0 and nums[l] != nums[mid]:
                    l += 1
                while r < len(nums) and nums[r] != nums[mid]:
                    r -= 1
                return [l, r]
        return [-1, -1]


s = Solution()
s.searchRange([5,7,7,8,8,10], 8)
print(s.searchRange([], 1))
print(s.searchRange([1], 1))
