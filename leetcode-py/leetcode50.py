class Solution:
    def myPow(self, x: float, n: int) -> float:
        ''' method
        most common people will use this method
        '''
        return x ** n

        '''
        well I guess the LC would like to see us solve it via BINARY SEARCH
        
        m 是 无符号的 n
        https://leetcode.com/problems/powx-n/discuss/19566/Iterative-JavaPython-short-solution-O(log-n)
        
        We can see that every time we encounter a 1 in the binary representation of N, 
        we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent. 
        Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc) and multiply it by the answer when we see a 1.
        '''
        m = abs(n)
        ans = 1.0
        while m:
            if m % 2 != 0:
                ans *= x
            x *= x
            m //= 2
        return ans if n >= 0 else 1 / ans
