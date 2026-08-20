# Last updated: 8/20/2026, 2:01:57 AM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        res = numBottles
        empty = numBottles

        while empty >= numExchange:
            full = empty // numExchange
            res += full
            empty = full + (empty % numExchange)
        
        return res