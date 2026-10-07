# Last updated: 10/7/2026, 2:53:21 PM
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        count = {}
        for i in logs:
            for v in range(i[0],i[1]):
                count[v] = count.get(v,0) + 1
        m = max(count.values())
        return min([i for i in count if count[i] == m])