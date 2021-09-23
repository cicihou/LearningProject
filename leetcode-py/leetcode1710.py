class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        for box, unit in boxTypes:
            if truckSize <= 0:
                return res
            res += min(box, truckSize) * unit
            truckSize -= box
        return res
