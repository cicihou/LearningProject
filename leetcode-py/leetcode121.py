class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        类似于 53 题

        Brute Force

        max(prices[j]−prices[i])

        time: O(n^2)
        space: O(1)
        '''
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit

        '''
        DP 
            one-pass solution

            if prices[i] - buy > profit:
                profit = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
        
        time O(n)
        space O(1)
        '''
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return profit
