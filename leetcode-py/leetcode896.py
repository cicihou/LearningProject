class Solution:
    def isMonotonic(self, A) -> bool:
        if A[0] > A[len(A) -1]:
            # decreasing
            for i in range(1, len(A)):
                if A[i] > A[i-1]:
                    return False
        elif A[0] == A[len(A) - 1]:
            return bool(len(set(A)) == 1)
        else:
            # increasing
            for i in range(1, len(A)):
                if A[i] < A[i-1]:
                    return False
        return True

s = Solution()
print(s.isMonotonic([1, 2, 2, 3]), 't')
print(s.isMonotonic([6, 5, 4, 4]), 't')
print(s.isMonotonic([1,3,2]), 'f')
print(s.isMonotonic([1,2,4,5]), 't')
print(s.isMonotonic([1,1,1]), 't')