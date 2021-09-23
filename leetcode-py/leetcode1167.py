from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        res = 0
        heapify(sticks)
        while len(sticks) > 1:
            fir = heappop(sticks)
            sec = heappop(sticks)
            tmp = fir + sec
            res += tmp
            heappush(sticks, tmp)
        return res
