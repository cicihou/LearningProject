from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        利用 combinations 将所有的可能性进行非重复的排练组合，聪明的解法

        因为时针有 4 个点 [1,2,3,8]，时钟的亮灯次数只能对应[0,1,2,3]，如果四盏灯全亮会超过 12
        因此不管亮灯数有多少，按照时针的可能性来推排列组合的可能性，时针的可能性有且只有四种
        因此在时针处的循环是 min(4, turnedOn + 1)

        这个问题本身是常数级别的问题，因为时间的有穷性

        这道题还可以用 bit manipulation
        https://leetcode-solution.cn/solutionDetail?type=3&id=40&max_id=2
        https://leetcode.com/problems/binary-watch/discuss/302787/Python-20ms
        '''
        res = set()

        def possible_numbers(count, minute=False):
            if count == 0:
                return [0]
            if minute:
                return filter(lambda x: x < 60, map(sum, combinations([1,2,4,8,16,32], count)))
            return filter(lambda x: x < 12, map(sum, combinations([1,2,4,8], count)))

        for i in range(min(4, turnedOn + 1)):
            hours = possible_numbers(i)
            for a in hours:
                minutes = possible_numbers(turnedOn-i, True)
                for b in minutes:
                    res.add(str(a) + '%02d' % str(b))
        return res
