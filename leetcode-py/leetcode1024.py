from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        '''
        实质上求选择最少的数组，达到最长的覆盖区间（如果不能完成全覆盖就返回 -1）
        跟 lc45 思想相似

        通过对 clips 的预处理，将 clips 转换成 lc 45 的跳跃数组
        将问题变成，在数组中如何通过最小的步数到达终点

        我们尽量找出能够覆盖最远位置的视频，并记录它的覆盖范围的坐标点
        使用 furthest[i] 记录每一个位置 i 能够覆盖的最长视频距离
        比如 [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
        我们处理后就变成 [2, 9, 9, 9, 9, 9, 9, 9, 10, 10]
            last = max(furthest[i], last)
        当 i == end 时，说明这一个视频已经到了区间的end，需要一个新的 clip 区间才能扩展范围，我们更新 end

        理论上说，i 必须要小于 last, 因为当前能走的最远步数必定要超过当前所在的位置
        当 i == last 时，说明视频片段存在错位，返回 -1
        i.e. 本问题存在到达不了的可能性，此时返回 -1

        这题需要多理解一下其与 lc45 的关联

        time: O(n^2)
        space: O(n)
        '''
        furthest = [0] * time
        for start, end in clips:
            for i in range(start, end+1):
                # 当范围超出我们所需的最大值时，无需记录
                # furthest 每个坐标点都记录当前我们可以到达的最远距离
                if i >= time:
                    break
                furthest[i] = max(furthest[i], end)
        end = last = res = 0
        for i in range(time):
            last = max(last, furthest[i])
            if i == last:
                return -1
            if i == end:
                res += 1
                end = last
        return res


s = Solution()
s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10)
s.videoStitching([[0,2],[3,4]],4)
s.videoStitching([[0,1],[3,4]],5)
