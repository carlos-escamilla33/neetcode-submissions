class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0

        for i in range(len(prices)):
            currProfit = prices[i] - prices[l]
            if currProfit <= 0:
                l = i
            maxProfit = max(maxProfit, currProfit)

        return maxProfit
        