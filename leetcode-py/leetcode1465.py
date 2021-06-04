class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        ''' 题目的要求是要 return 10**9 + 7 的余数, no why '''
        horizontalCuts.sort()
        verticalCuts.sort()
        hh = max(horizontalCuts[0], h - horizontalCuts[-1])
        vv = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            hh = max(horizontalCuts[i] - horizontalCuts[i - 1], hh)
        for j in range(1, len(verticalCuts)):
            vv = max(verticalCuts[j] - verticalCuts[j - 1], vv)
        return hh * vv % (10 ** 9 + 7)
