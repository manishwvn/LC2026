# Last updated: 8/20/2026, 1:52:55 AM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        if abs(y-z) > abs(z-x):
            return 1
        elif abs(y-z) < abs(z-x):
            return 2
        else:
            return 0

        