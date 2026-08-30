class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxP = 0, 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                while prices[r] < prices[l]:
                    l += 1
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        return maxP