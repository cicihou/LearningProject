class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        DP
        两根指针 left, right
        right 指针每次右移一次，左指针都回到起点，逐个比较，直到遍历完这个子序列
            if arr[left] < arr[right]:
                t[right] = max(t[right], t[left]+1)
        https://www.youtube.com/watch?v=CE2b_-XfVDk

        time: O(n^2)
        space: O(n)
        '''
        left = 0
        dp = [1] * len(nums)
        for right in range(1, len(nums)):
            while left < right:
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], dp[left] + 1)
                left += 1
            left = 0
        return max(dp)

        '''
        method 2
        binary search 优化 + DP
        
        time: O(nlogn)
        space: O(n)
        
        https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
        '''
        # TODO
