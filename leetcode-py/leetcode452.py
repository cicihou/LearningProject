class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        lc 300/435/646
        这题数据量比较大，直接给出 prune 的写法，不然会超时
        :param points:
        :return:
        '''
        n = len(points)
        dp = [1] * n
        points.sort()
        for i in range(n):
            for j in range(i-1, -1, -1):
                if points[j][1] < points[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                    break
        return max(dp)
