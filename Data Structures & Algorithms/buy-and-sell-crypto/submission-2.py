class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        left = 0 
        right = 1
        while right < n:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            if prices[left] > prices[right]:
                left = right
            else:
                right += 1
        return max_profit