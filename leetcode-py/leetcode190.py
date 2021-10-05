class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        bit manipulation 我真的一点都不会

        time: O(1)
        space: O(1)
        :param n:
        :return:
        '''
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res
