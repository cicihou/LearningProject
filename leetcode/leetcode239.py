class Solution:
    def maxSlidingWindow(self, nums,k):
        if not nums:
            return []
        res = []
        for i in range(len(nums)):
            if i + k <= len(nums):
                res.append(max(nums[i:i+k]))
        return res

s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))