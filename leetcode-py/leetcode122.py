class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        相似题 121
        画出股票走势的折线图，得出每一个上坡（趋势向上的斜线）的差值，就是我们能够获得的最大利润

        time: O(n)
        space: O(1)
        '''
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
