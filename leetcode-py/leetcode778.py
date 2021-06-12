'''
statement: At time t, the depth of the water everywhere is t.
meaning: the val in the grid(matrix) is constant and increasing

i.e.
in a ordered matrix, we find the least number to have a route
if the mid value cannot meet the demand, the numbers less than mid can also meet the demand

1. 求的是时间，其实也是平台的高度
2. [left, right] 中存在最小的 ret，使路径可以从[0,0] 到达[len-1,len-1]
3. 二分取mid，测试mid 能否通关；如果通关， r = mid - 1；否则，l = mid + 1
    1. 通关的函数测试中，有四种情况可以剪枝，提前推出循环
        a. (x, y) 溢出范围
        b. grid[x][y] > mid，说明我们当前测试的这个mid 不符合条件
        c. (x,y) 到了最尾部
        d. (x,y) 已经访问过
    2. 如果没有提前推出，则需要dfs 访问 (x,y) 的上下左右四个点，直至到达满足剪枝条件的 prune 推出点为止。
    3. 如果到达最尾部的推出点，说明当前 mid 对应了一条可行的路径，减小 r 看能不能找到更小的 mid；
       如果没有到达最尾部，说明 mid 不是一条可行的路径，增大 l 找更大的 mid
4. left 和 right 彼此之间逐渐逼近。实质上就是求最小的满足一定条件的 l 值，满足之后推出时的 left 就是我们想要的值
5. 注意 seen 在每次 l<=r 循环结束后必须标0，因为上次的循环是一次单独的路径试探，不能反映下次循环的任何情况，也没有任何用处

时间复杂度：O(NlogM)，其中 M 为 grid 中的最大值， N 为 grid 的总大小。
空间复杂度：O(N)，其中 N 为 grid 的总大小。
'''


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()

        l = 0
        r = max(max(vec) for vec in grid)

        def dfs(mid, x, y):
            ''' 前面这些可以理解成剪枝，prune，提前推出循环'''
            if not 0 <= x < m or not 0 <= y < n:
                return False
            if grid[x][y] > mid:
                return False
            if (x, y) == (m-1, n-1):
                return True
            if (x,y) in seen:
                return False
            seen.add((x,y))
            return dfs(mid, x+1, y) or dfs(mid, x-1, y) or dfs(mid, x, y+1) or dfs(mid, x, y-1)

        while l <= r:
            mid = (l+r) // 2
            if dfs(mid, 0, 0):
                r = mid - 1
            else:
                l = mid + 1
            seen = set()
        return l
