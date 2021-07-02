class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        在 nums 中找到两个 sum 相等的子集，就相当于是在一个序列中找到 sum 为 sum(nums) / 2 的子序列
        同时，我们可知，如果 sum(nums) 是奇数，那就一定不存在
        prune 如下：
            1. sum is odd, -> False
            2. sum is even, -> find the subsut sum equals to sum / 2
            3. if max(nums) > sum / 2 -> False

        将问题转换成 subset sum problem: https://www.youtube.com/watch?v=obhWqDfzwQQ
        subset sum problem: https://www.youtube.com/watch?v=s6FhG--P7z0

        比较像回溯，TLE
        '''
        total = sum(nums)
        if total % 2 != 0:
            return False

        nums.sort(reverse=True)

        def dfs(target, start):
            if target < 0:
                return
            elif target == 0:
                return True

            for i in range(start, len(nums)):
                if dfs(target-nums[i], i+1):
                    return True
            return False
        return dfs(total/2, 0)

        '''
        DP
        https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
        这题不太理解
        '''
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False
        target = total // 2  # 返回的需要是int, 而非 float
        if max(nums) > target:
            return False

        dp = [[0] * (target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target+1):
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]
