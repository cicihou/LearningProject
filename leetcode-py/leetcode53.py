class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ''' method 1
        brute force
        time O(n^2)
        '''
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            tmp = s
            for j in range(i, len(nums)):
                ans = max(tmp, ans)
                tmp += nums[j]
        return ans


        '''
        method 2
        Kadane Algorithm
        
        How Dynamic Programming works : https://www.youtube.com/watch?v=2MmGzdiKR9Y
        
        只比较前后两个数，max(nums[i], nums[i] + nums[i-1])，递推遍历进行比较
        再比较之前的答案和当前前后两个数的 max
        '''
        ans = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur+nums[i])
            ans = max(ans, cur)
        return ans
