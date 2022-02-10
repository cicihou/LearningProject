class Solution:
    def plusOne(self, digits):
        '''
        method 1
        :param digits:
        :return:

        time: O(n)
        space: O(n), the operation in-place (i.e. on the input list itself)
            in the worst scenario, we would allocate an intermediate space to hold the result, which contains the N+1 elements
            hence the overall space complexity of the algorithm is O(n)
        '''
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

        '''
        method 2 
        python tricks
        '''
        # num = ''.join([str(n) for n in digits])
        # number = str(int(num) + 1)
        # res = [int(n) for n in number]
        # return res

        '''
        method 3
        tricky python to make it faster
        '''
        # return [int(n) for n in str(int(''.join([str(n) for n in digits])) + 1)]


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9, 9, 9, 9]))
print(s.plusOne([8, 9, 9, 9]))
print(s.plusOne([1, 2, 0, 9, 9, 9]))
print(s.plusOne([1,2,3,0,9,9]))
print(s.plusOne([8,0,9,9]))
print(s.plusOne([9,8,9,9]))
print(s.plusOne([9,9,9,9]))
print(s.plusOne([0]))
print(s.plusOne([9]))
