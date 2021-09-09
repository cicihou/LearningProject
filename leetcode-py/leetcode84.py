'''
视频：https://www.youtube.com/watch?v=vcv3REtIvEo
monostack

1. find the nearest left bar with height < current bar
2. find the nearest right bar with height < current bar

分别从左向右，以及右向左维护两个单调栈，monostack

左边向右边时：
碰到比左边或者比右边小的，就 pop 掉当前的数，单调栈中存且只存比 cur 的 height 小的 index，
我们单独维护一个数组，存 nearest left bar less than cur 的 index + 1 值

右边向左边时：相反

最后求出每个index可以生成的 histogram 的最大值，(right - left + 1) * bar_height

这题关于单调栈，挺难的，我不是很理解
'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        method 1

        :param heights:
        :return:
        '''
        n = len(heights)
        left, right = [0] * n, [0] * n

        monostack = list()
        for i in range(n):
            while monostack and heights[monostack[-1]] >= heights[i]:
                monostack.pop()
            left[i] = monostack[-1] if monostack else -1
            monostack.append(i)

        monostack = list()
        for i in range(n-1, -1, -1):
            while monostack and heights[monostack[-1]] >= heights[i]:
                monostack.pop()
            right[i] = monostack[-1] if monostack else n
            monostack.append(i)

        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return res
