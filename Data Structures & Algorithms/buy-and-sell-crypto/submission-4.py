class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                while prices[l] > prices[r]:
                    l += 1
            
            profit = max(profit, prices[r] - prices[l])
        
        return profit