'''
Triangle

找到三角形中自顶而下，值最小的路径
经典 DP 入门题
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        method 1

        每一步只能移动到下一行「相邻的节点」上，因此想走到位置(i, j)，上一步就只能在位置(i-1, j-1) 或者 (i-1, j)
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        注意当 j = 0 时，只能从 [i-1][j] 转移过来；i.e. 直角三角形的最左侧
        注意当 j = i 时，只能从 [i-1][j-1] 转移过来；i.e. 直角三角形的最右侧

        dp[0][0] = triangle[0][0]  # 初始边界条件

        time: O(N^2)
        space: O(N^2)

        :param triangle:
        :return:
        '''
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[-1])

        '''
        method 2
        三角形自底向上，DP 查找 minimum path sum 的路径
        
        time: O(N^2)
        space: O(N)
        '''
        n = len(triangle)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            for j in range(0, i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
