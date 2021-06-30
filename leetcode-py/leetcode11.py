class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        method 1 Brutal Force, Intuitive
        TLE
        Time: O(n^2)
        Space: O(1)
        '''
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res

        '''
        method 2 two pointer
        time: O(n)
        space: O(1)
        '''
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            res = max(res, (r-l) * min(height[l], height[r]) )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
