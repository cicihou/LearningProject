class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        method 1 memoize + recursion

        如果都合法的时候，答案就是 fibbo(len(s)+1)

        递归：
            有多少个需要计算的值，我们可以假设取第一位或者取第二位数

            base case:
                当 length = 0 时，res = 1
                当 s[k:] 的第一位是 0 是，表示这是一个无效的子串，所以也返回 0

            res = func(length - 1) + func(length - 2)
            注意 length - 2 需要判断有效性

        time: O(n)
        space: O(n)

        视频：https://www.youtube.com/watch?v=qli-JCrSwuk
        :param s:
        :return:
        '''
        memo = {}
        n = len(s)

        def func(length):
            '''
            k is start, length 是剩下的位数

            :param string:
            :param length:
            :return:
            '''
            if length in memo:
                return memo[length]

            if length == 0:
                return 1
            k = n - length
            if s[k] == '0':
                return 0
            res = func(length-1)
            if length >= 2 and int(s[k:k+2]) <= 26:  # 判断有效性
                res += func(length-2)
            memo[length] = res
            return res

        return func(n)

        '''
        method 2 DP
        '''
        # TODO
