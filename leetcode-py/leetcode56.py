class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        将列表按大小排序，最小的列表最先添加进结果列表，遍历列表；
        假如遍历的列表和结果列表的末尾元素列表有overlapping，修改结果列表的末尾元素列表
        没有overlapping，将当前正在遍历的列表添加入结果列表

        time: O(nlogn), sort
        space: O(n)
        '''
        intervals.sort()
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,4],[0,4]]))
