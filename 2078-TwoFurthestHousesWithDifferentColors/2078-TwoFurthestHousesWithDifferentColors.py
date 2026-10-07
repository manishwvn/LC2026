# Last updated: 10/7/2026, 2:51:36 PM
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0 
        for i in range(len(colors)): 
            if colors[i] != colors[0]: max_dist = max(max_dist, i)
            if colors[i] != colors[-1]: max_dist = max(max_dist, len(colors)-1-i)
        return max_dist 