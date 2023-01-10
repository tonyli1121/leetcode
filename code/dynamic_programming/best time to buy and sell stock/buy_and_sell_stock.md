![image](https://user-images.githubusercontent.com/53313027/211461100-a3af6615-7639-4c3a-bfa6-06f29f7fe3e9.png)


## Approach 1

Use two pointers, keep track of the largest profit, update the buying/selling date correspondingly.

``` python 3
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
```

This gives us a O(N) solution, but note that we are setting/keeping track a lot of variables (O(1) space complexity but use more space than approach 2)

![image](https://user-images.githubusercontent.com/53313027/211461242-ef305c36-4643-4001-9558-aa5f08a6f9f9.png)

## Approach 2

Using Kadane's Algorithm: O(N) time, O(1) space

``` python 3
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
```

![image](https://user-images.githubusercontent.com/53313027/211461379-6d6194ba-8bfe-49c6-b175-3a5fa7d930b7.png)
