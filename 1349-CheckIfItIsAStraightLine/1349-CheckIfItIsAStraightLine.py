# Last updated: 8/20/2026, 2:04:09 AM
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2:
            return True
        
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]

        for i in range(2,len(coordinates)):
            x, y = coordinates[i][0], coordinates[i][1]

            if (y - y1) * (x - x0) != (y - y0) * (x - x1):
                return False

        return True