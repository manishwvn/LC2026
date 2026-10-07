# Last updated: 10/7/2026, 2:56:14 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        res = numBottles
        empty = numBottles

        while empty >= numExchange:
            full = empty // numExchange
            res += full
            empty = full + (empty % numExchange)
        
        return res