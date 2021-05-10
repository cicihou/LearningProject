class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 将列表按大小排序，最小的列表最先添加进结果列表，遍历列表；
        # 假如遍历的列表和结果列表的末尾元素列表有overlapping，修改结果列表的末尾元素列表
        # 没有overlapping，将当前正在遍历的列表添加入结果列表
        intervals.sort(key=lambda x:x[0], reverse=False)
        if len(intervals) <= 1:
            return intervals
        merged = []
        for interval in intervals:
            if not merged or merged[len(merged)-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[len(merged)-1][1] = max(merged[len(merged)-1][1], interval[1])
        return merged

s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([[1,4],[0,4]]))

