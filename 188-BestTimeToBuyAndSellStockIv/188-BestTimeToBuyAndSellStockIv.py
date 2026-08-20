# Last updated: 8/20/2026, 2:16:12 AM
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        buy = [float('inf') for _ in range(k+1)]
        sell = [0 for _ in range(k+1)]

        for price in prices:
            for i in range(1, k+1):
                buy[i] = min(buy[i], price - sell[i-1])
                sell[i] = max(sell[i], price - buy[i])

    
        return sell[-1]
