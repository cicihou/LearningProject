from collections import defaultdict


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ''' method 1 Brute Force
        time limit exceed
        不太优雅的 BF
        '''
        dic = defaultdict(lambda: 0)
        for flight in bookings:
            for i in range(flight[0], flight[1] + 1):
                dic[i] += flight[2]
        res = []
        for i in range(1, n + 1):
            res.append(dic[i])
        return res

        ''' method 2 Brute Force
        time limit exceed
        一种比较优雅的 BF，可惜还是TLE
        '''
        counter = [0] * n
        for i, j, k in bookings:
            while i <= j:
                counter[i - 1] += k
                i += 1
        return counter

        '''
        method 3 prefix sum
        time O(n)
        space O(1)
        '''
        counter = [0] * (n + 1)
        for i, j, k in bookings:
            counter[i-1] += k
            # 因为前缀和会把后面的区间也加上，所以在 [j:n] 的区间减去一个 k 值
            # 由于题目具有现实意义，因此 区间仅为 [1,n]
            # 在程序里面，counter 前缀和 的第一站为 counter[0]，那么 counter[j] 正好就是第一个不需要 += k 的区间边界值
            if j < n:
                counter[j] -= k
        for i in range(1, len(counter)):
            counter[i] += counter[i-1]
        return counter[:-1]
