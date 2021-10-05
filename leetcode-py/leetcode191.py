class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        python tricks
        :param n:
        :return:
        '''
        return bin(n).count('1')

        '''
        method 2
        
        time: O(1), the run time depends on the number of bits in n. The input must be a binary string of length 32, thus the time complexity is O(1)
        space: O(1), the space complexity is O(1), since no additional space is allocated
        '''
        count = 0
        while n:
            if n % 2:
                count += 1
            n //= 2
        return count
