class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        index = 0
        for i in range(1, n+1):
            if n % i == 0:
                index += 1
            if index == k:
                return i
        return -1
