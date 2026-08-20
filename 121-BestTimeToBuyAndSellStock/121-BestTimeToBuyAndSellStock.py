# Last updated: 8/20/2026, 2:17:35 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr_profit, max_profit = 0, 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price

            curr_profit = price - min_price
            max_profit = max(curr_profit, max_profit)

        return max_profit


        