# Last updated: 8/20/2026, 2:14:56 AM
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if not costs or len(costs) == 0:
            return 0
    
        previous = costs[-1]
    
        for i in range(len(costs)-2, -1, -1):
            # current = deepcopy(costs[i])

            a,b,c = costs[i]
            a += min(previous[1], previous[2])
            b += min(previous[0], previous[2])
            c += min(previous[0], previous[1])
            previous = [a,b,c]

        return min(previous)