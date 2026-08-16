# Last updated: 8/16/2026, 4:10:47 PM
1from typing import List
2
3
4class Solution:
5
6    def largestTriangleArea(self, points: List[List[int]]) -> float:
7        n = len(points)
8        max_area = 0.0
9
10        # Explicit three nested loops instead of combinations
11        for i in range(n):
12            x1, y1 = points[i]
13            for j in range(i + 1, n):
14                x2, y2 = points[j]
15                for k in range(j + 1, n):
16                    x3, y3 = points[k]
17
18                    # Shoelace formula for area
19                    area = 0.5 * abs(
20                        x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
21                    )
22
23                    if area > max_area:
24                        max_area = area
25
26        return max_area