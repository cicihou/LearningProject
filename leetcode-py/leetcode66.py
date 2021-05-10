class Solution:
    def plusOne(self, digits):
        # 方法一
        # 有缺陷
        for i in range(len(digits)-1,0,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[i-1] == 9:
                    digits[i-1] += 1
        else:
            if digits[0] == 0:
                digits.insert(0,1)
            if digits[0] > 9:
                digits[0] = 0
                digits.insert(0, 1)
        return digits

        # 方法二
        # num = ''.join([str(n) for n in digits])
        # number = str(int(num) + 1)
        # res = [int(n) for n in number]
        # return res

        # 方法3  虽然只是抽出方法二，但是速度会提升
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