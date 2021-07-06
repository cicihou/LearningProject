class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        DP
            核心思想以及 dp 方程与 lc 300 一致
            这样直接遍历会 TLE，需要 prune
        '''
        n = len(intervals)
        dp = [1] * n
        intervals.sort()
        for i in range(n):
            for j in range(i+1):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return n - max(dp)

        '''
        DP + prune
            题目本身是区间，我们只比较相邻两个区间的头尾
            因此，越大的区间在越后面
            那我们从后往前找这个状态，一旦证明这一个状态/子问题 需要删除，就退出本次循环，进入到下一个子问题
        
        time: O(n^2)
        space: O(n)
        '''
        n = len(intervals)
        dp = [1] * n
        intervals.sort()
        for i in range(n):
            for j in range(i-1, -1, -1):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        return n - max(dp)

        '''
        method 3 贪心 greedy + 二分 binary search
            https://leetcode-solution.cn/solutionDetail?type=3&id=58&max_id=2
        time: O(nlogn)
        space: O(n)
        '''
        # TODO
