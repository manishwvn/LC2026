# Last updated: 8/20/2026, 2:18:26 AM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                #pop
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index
                
            stack.append([start, h])
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
        