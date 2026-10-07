# Last updated: 10/7/2026, 2:43:23 PM
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        for i in range(1, len(cost)):
            cost[i] = min(cost[i], cost[i-1])

        return cost

        