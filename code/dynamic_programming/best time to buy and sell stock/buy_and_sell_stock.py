# Two pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        max_profit = prices[sell] - prices[buy]
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_profit

# approach 2: Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        else:
            profit = 0
            minBuy = prices[0]
            for i in range(len(prices)):
                profit = max(prices[i] - minBuy, profit)
                minBuy = min(minBuy, prices[i])
            return profit
