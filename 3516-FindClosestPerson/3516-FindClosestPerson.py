# Last updated: 10/7/2026, 2:43:25 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        if abs(y-z) > abs(z-x):
            return 1
        elif abs(y-z) < abs(z-x):
            return 2
        else:
            return 0

        