class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        method 1

        time: O(logN)
        space: O(1)
        '''
        if n <= 0:
            return False
        while n != 1:
            if n % 2:
                return False
            n = n // 2
        return True


        '''
        method 2 bit manipulation
        
        the problem will be solved in O(1) time with the help of bitwise operators. 
        The idea is to discuss such bitwise tricks as
            How to get / isolate the rightmost 1-bit : x & (-x).
            How to turn off (= set to 0) the rightmost 1-bit : x & (x - 1).
        
        time: O(1)
        space: O(1)
        
        我还是对位运算不太了解，理解的太表面，可能需要补一下二进制相关的知识
        '''
        if n == 0:
            return False
        return n & (-n) == n


s = Solution()
print(s.isPowerOfTwo(1), 't')
print(s.isPowerOfTwo(16), 't')
print(s.isPowerOfTwo(218), 'f')
print(s.isPowerOfTwo(0), 'f')
print(s.isPowerOfTwo(3), 'f')
