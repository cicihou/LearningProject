class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ''' between(i, j) 等于 atMostK(j) - atMostK(i-1)'''
        def noGreaterThan(R):
            ''' atMostK 一定要掌握，这是前缀和的灵魂啊 '''
            ans = cnt = 0
            for a in nums:
                if a <= R:
                    cnt += 1
                else:
                    cnt = 0
                ans += cnt
            return ans
        return noGreaterThan(right) - noGreaterThan(left - 1)
