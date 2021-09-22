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
        without 
        '''
        count = 0
        while n:
            if n % 2:
                count += 1
            n //= 2
        return count
