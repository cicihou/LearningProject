# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         if n == 1:
#             return True
#         while n:
#             n = n / 2
#             if n == 1:
#                 return True
#             if n % 2 != 0:
#                 return False
#         return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n // 2 != n / 2:
                return False
            else:
                n = n // 2
        return True


s = Solution()
print(s.isPowerOfTwo(1), 't')
print(s.isPowerOfTwo(16), 't')
print(s.isPowerOfTwo(218), 'f')
print(s.isPowerOfTwo(0), 'f')
print(s.isPowerOfTwo(3), 'f')