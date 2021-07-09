class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        method 1
        跟 lc 56 一模一样，只是 lc 56 中没有显式的 newInterval
        把这道题变成 lc 56 来做

        time: O(nlogn)
        space: O(n)
        '''
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
