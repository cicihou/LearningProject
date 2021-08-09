class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        interval: 2n - 2, n is numRows
        step: interval - 2i,

        图解：https://leetcode.com/problems/zigzag-conversion/discuss/3435/If-you-are-confused-with-zigzag-patterncome-and-see!

        可以看成是一道找规律题，
        numRows 是行数，头尾各掐掉一个，numRows - 2就是会消耗字母的中间区间

        字母的分布只有两个区间，竖直区间，对角区间
        竖直区间会消耗 numRows 个字母，对角区间会消耗 numRows - 2 个字母

        因此 2 * numRows - 2 就是一个正常的周期会消耗的个数

        :param s:
        :param numRows:
        :return:
        '''

        n = len(s)

        if numRows > n or numRows <= 1:
            return s

        k = 2 * numRows - 2

        res = [''] * n

        for i in range(len(s)):
            if i % k >= numRows:  # 表示已经进入了字母对角区间
                res[k - i % k] += s[i]  # 对角区间实际上就是在取反，因为它是逆序上升的，index 跟字符串遍历的顺序其实是相反的
            else:
                res[i % k] += s[i]  # 竖直区间就正常消耗字母
        return ''.join(res)
