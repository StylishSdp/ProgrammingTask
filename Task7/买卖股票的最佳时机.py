class Solution:
    def maxProfit(self, prices):

        if not prices or len(prices) == 1:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)

        return profit