class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        left = 0
        right = 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            maxp = max(maxp, profit)
            if prices[left] > prices[right]:
                left = right
            right += 1

        return maxp
