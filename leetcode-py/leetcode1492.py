class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        '''
        method 1 Brute Force

        time: O(n)
        space: O(1)
        '''
        index = 0
        for i in range(1, n+1):
            if n % i == 0:
                index += 1
            if index == k:
                return i
        return -1

        '''
        method 2
        
        time: O(n)
        space: O(n)
        '''
        small, big = [], []
        for i in range(1, isqrt(n)+1):
            if n % i == 0:
                if n // i == i:
                    small.append(i)
                else:
                    small.append(i)
                    big.append(n//i)
        big.reverse()
        factors = small + big
        return factors[k-1] if len(factors) >= k else -1

        '''
        method 3
        
        核心就是，每个 n % factor1 == 0，必然有一个与其对应的factor 2，
        因此我们可以简化问题到 square root of n, 
        
        isqrt 是 python 3.8 的特性，相当于 int(sqrt())，向下取整
        
        视频：https://www.youtube.com/watch?v=s18rSWOvfOU
        
        time: O(n**0.5), square root of n
        space: O(1)
        '''
        isqrt = math.isqrt(n)
        for i in range(1, isqrt + 1):
            if n % i == 0:
                p -= 1
                if p == 0:
                    return i
        for i in reversed(range(1, isqrt + 1)):
            if i * i == n:  # 处理 perfect square 的情况，这个我们在上面那个循环已经处理过了
                continue
            if n % i == 0:
                p -= 1
                if p == 0:
                    return n // i
        return -1
