class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProfit = 0

        for i in range(len(prices)):
            l = 0
            r = l + i

            while r < len(prices):
                maxProfit = max(maxProfit, prices[r] - prices[l])
                l += 1
                r += 1
        
        return maxProfit