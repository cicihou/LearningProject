class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        method 1 使用贪心策略，每次都在可跳范围内选择跳的最远的距离
        到达我们上一轮的跳点之后，产生新一次跳跃，每次跳跃计为1，并重新更新边界

        note: 到达 nums 的最后一个数，或者更后的位置，都算是到达了边界

        furthest 统计我们当前获得的跳跃数，在本轮跳跃所覆盖的区间中，能够到达的 index 的最远位置

        time: O(n)
        space: O(1)
        '''

        n = len(nums)
        furthest = cnt = end = 0

        # 最后一个数及更之后都算是到达终点，因此遍历只需要 n-1 次
        for i in range(n-1):
            furthest = max(furthest, nums[i] + i)
            if i == end:
                cnt += 1
                end = furthest
        return cnt
