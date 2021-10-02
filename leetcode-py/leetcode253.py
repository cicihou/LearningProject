from heapq import heappush, heapreplace


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        用最简单的 simulation 做
        先将会议排序
        创建一个堆，表示分配的会议室个数（只需要存储会议的结束时间）
        如果当前会议的开始时间 >= 最早的结束时间，我们就把当前会议的结束时间插入堆，更新替换堆底部最大的那个结束时间（表示结束时间后移了）；i.e. 当前会议虽然不需要分配会议室，但是我们需要更新并推后 会议的最晚结束时间（堆底）
        若当前会议的开始时间 < 最早的结束时间，说明（当前的会议室都被占用）需要一个新的会议室


        出于堆的特性，堆顶做比较的一定会是最早的结束时间。堆底被替换的一定是最晚的结束时间
        循环结束后，判断一共用了多少的会议室，i.e. len(heap)

        time: O(nlogn)
        space: O(n)
        '''
        intervals.sort()
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapreplace(heap, i[1])
            else:
                heappush(heap, i[1])
        return len(heap)
