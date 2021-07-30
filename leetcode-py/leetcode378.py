class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for m in matrix:
            res.extend(m)
        res.sort()
        return res[k-1]

        '''
        method 2 binary search + heap
        '''
        # TODO
