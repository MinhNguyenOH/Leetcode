class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_price = prices[0]
        for r in range(len(prices)):
            if prices[r] < lowest_price:
                lowest_price = prices[r]
            res = max(res, prices[r]-lowest_price)
        return res