class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        trapped water for a block = (water level - block height) * width

        method 1
        利用 prefix_sum 逐格计算降水量

        视频：https://www.youtube.com/watch?v=m18Hntz4go8
        h[i] 等于左右两侧柱子的最大值中的较小值，即 h[i] = min(maximum left, maximum right)
        让我们维护两个 prefix_max 数组
        一个从前向后，记录 prefix_max
        一个从后向前，记录 suffix_max

        因此，每个格子 i 可以积攒的降水就是 min(prefix_max[i], suffix_max[i]) - height[i]

        time: O(n)
        space: O(n)
        '''
        if not height:
            return 0

        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)

        # 注意这样生成的数组中，我们在计算中会忽略 prefix_max 中 height[0] 和 suffix_max 中 height[-1] 的值
        prefix_max[0] = height[0]
        suffix_max[-1] = height[-1]

        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])
        res = 0
        for i in range(len(height)):
            res += min(prefix_max[i], suffix_max[i]) - height[i]
        return res

        '''
        method 2
        two-pointer
        '''
        # TODO
