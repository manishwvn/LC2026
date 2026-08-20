# Last updated: 8/20/2026, 1:58:08 AM
from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        color_map = defaultdict(set)

        for i in range(0, len(rings), 2):
            color_map[rings[i + 1]].add(rings[i])
        return sum(1 for colors in color_map.values() if len(colors) == 3)