import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        method 1 跟 lc 264 一模一样的 min heap 写法
                不过可能是越来越卷了，现在 TLE/MLE(Memory Limit Exceeded) 了

        :param n:
        :param primes:
        :return:
        '''
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for p in primes:
                tmp = p * curr
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(heap, tmp)
        return heapq.heappop(heap)

        '''
        method 2 DP
        '''
        m = len(primes)
        pointers = [1] * m
        ugly_nums = primes[:]
        ugly = 1
        dp = [1]

        for i in range(1, n):
            for j in range(0, m):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[pointers[j]] * primes[j]
                    pointers[j] += 1
            ugly = min(ugly_nums)
            dp.append(ugly)

        return dp[-1]
