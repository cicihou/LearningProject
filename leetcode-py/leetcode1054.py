from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        method 1 direct sort via sorted()
        :param barcodes:
        :return:

        time: O(n + klogk)
        space: O(n)
        '''
        n = len(barcodes)
        counter = Counter(barcodes)
        items = sorted([(-val, key) for key, val in counter.items()])

        cur = []
        for v, k in items:
            cur += [k] * (-v)

        j = 0
        res = [0] * n

        # 这里就是直接排序，先将 res 中的偶数位赋值，再将奇数位赋值，注意遍历循环的只有 i，这里面 j 是一直自增的
        for i in range(0, n, 2):
            res[i] = cur[j]
            j += 1
        for i in range(1, n, 2):
            res[i] = cur[j]
            j += 1
        return res

        '''
        method 2 sort via maxHeap
        
        time: O(n + klogk)
        space: O(n)
        '''
        n = len(barcodes)
        counter = Counter(barcodes)
        items = [(-v, k) for k, v in counter.items()]
        heapq.heapify(items)

        cur = []
        while items:
            v, k = heapq.heappop(items)
            cur += [k] * -v
        j = 0
        res = [0] * n

        for i in range(0, n, 2):
            res[i] = cur[j]
            j += 1
        for i in range(1, n, 2):
            res[i] = cur[j]
            j += 1
        return res


s = Solution()
s.rearrangeBarcodes([1,1,1,1,2,2,3,3])
s.rearrangeBarcodes([5,8,5,4,5])
s.rearrangeBarcodes([1])
s.rearrangeBarcodes([1,1,2,3,4,56,7,8,24])
