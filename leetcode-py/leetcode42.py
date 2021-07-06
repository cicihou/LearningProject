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
        
        我们实际上只关心左右两侧更小的哪一个，并不需要将两者实际算出来
            如果 l[i + 1] < r[i]，那最终积水的高度由 i 的左侧最大值决定的
            如果 l[i + 1] >= r[i]，那么最终积水的高度由 i 的右侧最大值决定的
        因此我们无需维护两个完整数组，而可以只进行一次遍历，同时维护左侧最大值和右侧最大值
        
        1. 维护两个指针 left right 指向头尾
        2. 初始化左侧和右侧的最高的高度都为 0
        3. 比较 height[left] 和 height[right]
            3.1 如果 height[left] < height[right], 那么瓶颈在于 height[left]，不需要考虑 height[right]
                3.1.1 如果 height[left] < left_max， 则当前格子积水面积为(left_max - height[left])，否则无法积水，即积水面积为 0。
                      也可将逻辑统一为盛水量为 max(0, left_max - height[left])
                3.1.2 左指针右移一位。（其实就是左指针的位置的雨水量已经计算完成了，我们移动到下个位置用同样的方法计算）
            3.2 否则 瓶颈在于 height[right]，不需要考虑 height[left]
                3.2.1 如果 height[right] < right_max, 则当前格子积水面积为(right_max - height[left])，否则无法积水，即积水面积为 0。
                      也可将逻辑统一为盛水量为 max(0, right_max - height[right])
                3.2.2 右指针右移一位。（其实就是右指针的位置的雨水量已经计算完成了，我们移动到下个位置用同样的方法计算）
        
        time: O(n)
        space: O(1)
        '''
        n = len(height)
        l_max = r_max = 0
        l, r = 0, n-1
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < l_max:
                    res += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    res += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return res

        '''
        method 3
        mono-stack
        '''
        # TODO
