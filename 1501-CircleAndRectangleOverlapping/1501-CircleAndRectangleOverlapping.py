# Last updated: 8/20/2026, 2:02:53 AM
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        

        near_x = max(x1, min(x2, xCenter))
        near_y = max(y1, min(y2, yCenter))

        dist_x = near_x - xCenter
        dist_y = near_y - yCenter

        return (dist_x ** 2) + (dist_y ** 2) <= radius ** 2