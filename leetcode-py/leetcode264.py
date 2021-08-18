import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        method 1 min heap

        分别计算出 2x 3x 5x 的值，堆顶元素就是堆中最小的丑数
        为避免重复元素，使用 hashmap 去重，避免相同元素多次加入堆

        n-th 是 1 index 的，将 n-1 个数出堆（0-index），最小堆的值的堆顶自然就是我们需要的值

        :param n:
        :return:
        '''
        heap = [1]
        prime = [2, 3, 5]
        seen = {1}

        for i in range(n - 1):
            curr = heapq.heappop(heap)  # 将最小的数出堆
            for p in prime:
                tmp = p * curr
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(heap, tmp)
        return heapq.heappop(heap)


        '''
        method 2 DP
        
        heap 会重复计算
        
        dp[i] 为 第 i 个丑数， dp[n] 为第 n 个丑数
        用三根指针质数，取标记后最小的那个数，移动对应的指针
        
        丑数总是由丑数的乘积组成，因此是 dp[pointer] 分别 * 2， * 3， * 5
        
        e.g.
            dp[1] * 2, dp[1] * 3, dp[1] * 5
            dp[2] * 2, dp[2] * 3, dp[2] * 5
            dp[3] * 2, dp[3] * 3, dp[3] * 5
            
        误区：直接与 pointer 的自增相乘是错误的，很简单的例子 7 * 2 就不符合要求，应是 dp[7] * 2
        '''
        dp = [0] * (n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n+1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]
