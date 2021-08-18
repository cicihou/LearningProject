class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        埃氏筛/素数筛
        如果 x 是质数(prime)，那么 2x, 3x, 4x, 一定不是质数

        用 isPrime list 表示是否为质数
        从 i*i 开始，因为 i*i 之前的数必定会被前面的质数给访问掉，比如 质数为 3 的时候，6 会被质数为 2 时的循环搞定，只需要从 3*3 开始考虑
        '''
        isPrime = [1] * n

        res = 0

        for i in range(2, n):
            if isPrime[i]:
                res += 1
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        return res

        '''
        method 2 线性筛，积性函数
        '''
        # TODO
