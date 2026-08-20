# Last updated: 8/20/2026, 1:52:53 AM
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        for i in range(1, len(cost)):
            cost[i] = min(cost[i], cost[i-1])

        return cost

        