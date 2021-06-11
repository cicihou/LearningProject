class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        实际上应该是 binary search + bit manipulation
        '''
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return int(dividend / divisor)
