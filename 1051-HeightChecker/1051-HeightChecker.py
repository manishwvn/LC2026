# Last updated: 10/7/2026, 3:01:39 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
                
        return count
        