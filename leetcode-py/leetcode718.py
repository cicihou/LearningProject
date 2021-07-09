'''
视频：https://www.youtube.com/watch?v=BysNXJHzCEs

if input[i] == input[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = 0

可以比较一下 else 条件中，本题 跟 lc 1143 的不同

lc1143 是求 subsequence，lc718 要求 subarray
'''


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        time: O(M*N)
        space: O(M*N)
        '''
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        return res
