class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        视频：https://www.youtube.com/watch?v=awxaRgUB4Kw
        记住吧，我也没找到什么特别好的方法，就是跟二进制计数和进位的特征相关而已
        :param n:
        :return:
        '''
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = res[i//2] + i % 2
        return res
