class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Work backwards to find the best selling prices 
        # for stocks bought at time 'i'
        max_sell = [None for i in range(len(prices))]
        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                max_sell[i] = prices[i]
            else:
                max_sell[i] = max(prices[i], max_sell[i + 1])

        # Compute max profits with each of the (purchase) prices
        max_profit = 0
        for i, buy_price in enumerate(prices):
            max_profit = max(max_profit, max_sell[i] - buy_price)

        return max_profit
