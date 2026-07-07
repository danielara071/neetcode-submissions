class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        left = 0
        right = 1
        n = len(prices)
        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxp = max(maxp, profit)
            else:
                left = right
            right += 1
        return maxp