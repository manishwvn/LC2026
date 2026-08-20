# Last updated: 8/20/2026, 2:12:21 AM
class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]




        