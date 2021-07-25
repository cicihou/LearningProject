from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([num for num in range(1, n+1)], k)
