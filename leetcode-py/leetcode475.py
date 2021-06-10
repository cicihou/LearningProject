class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''
        binary search
            1. sort the list
            2. add two fake heaters, then any houses can be always between two heaters
            3. search to put house between heaters
            4. find the sortest distance of the two and compare it to the answer
        '''
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            # 每当 house 离起点的距离大于 下一个 heater 到起点的距离，就定位到下一个起点
            # 这样，house 会正好在两个 heaters 的中间
            while house > heaters[i+1]:
                i += 1
            # 计算 house 离前后两个起点，哪一个距离近
            dis = min(house - heaters[i], heaters[i+1] - house)
            # ans 是所有 house 中的，距离起点最远的那个值
            ans = max(ans, dis)
        return ans
