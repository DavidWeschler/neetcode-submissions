class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro, buyPrice = 0, prices[0]

        for i in range(1, len(prices)):
            if prices[i] - buyPrice > maxPro:
                maxPro = prices[i] - buyPrice
            if prices[i] < buyPrice:
                buyPrice = prices[i]
        return maxPro