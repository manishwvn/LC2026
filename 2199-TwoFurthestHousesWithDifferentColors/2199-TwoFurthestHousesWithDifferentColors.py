# Last updated: 8/20/2026, 1:58:24 AM
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0 
        for i in range(len(colors)): 
            if colors[i] != colors[0]: max_dist = max(max_dist, i)
            if colors[i] != colors[-1]: max_dist = max(max_dist, len(colors)-1-i)
        return max_dist 