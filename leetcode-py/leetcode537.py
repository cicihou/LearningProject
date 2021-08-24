class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        '''
        (a+ib)×(x+iy)=ax + i^2 * by + i(bx+ay) = ax − by + i(bx+ay)
        '''
        num1 = [int(i) for i in num1.replace('i', '').split('+')]
        num2 = [int(i) for i in num2.replace('i', '').split('+')]

        real = num1[0] * num2[0] - num1[1] * num2[1]
        imaginary = num1[1] * num2[0] + num1[0] * num2[1]
        return str(real) + '+' + str(imaginary) + 'i'
