'''
假设字符串的长度是 5
那么要满足单调递增的特性，只可能是以下的结果
00000, 00001, 00011, 00111, 01111, 11111

那么我们要求，如果用最少的反转，满足一个字符串，分成两段时左边全是 0 且右边全是 1
'''


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        flag0 标记该位置之后有多少个 0，（这些 0 都需要变成 1）
        flag1 标记该位置之前有多少个 1，（这些 1 都需要变成 0）
        二者相加就是当前坐标为翻转点的最少移动次数

        代码：https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/solution/jiang-zi-fu-chuan-fan-zhuan-dao-dan-diao-di-zeng-b/

        :param s:
        :return:
        '''
        n = len(s)
        flag0 = [0] * (n+1)
        flag1 = [0] * (n+1)

        for i in range(n):
            flag1[i+1] = flag1[i]
            if s[i] == '1':
                flag1[i+1] += 1

        for i in range(n-1, -1, -1):
            flag0[i] = flag0[i+1]
            if s[i] == '0':
                flag0[i] += 1

        return min(x+y for x, y in zip(flag0, flag1))
