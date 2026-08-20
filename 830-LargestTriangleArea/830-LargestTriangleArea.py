# Last updated: 8/20/2026, 2:08:35 AM
from typing import List


class Solution:

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Step 1: Compute Convex Hull using Monotone Chain Algorithm
        points = sorted(points)

        # Cross product of vector OA and OB
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (
                b[0] - o[0]
            )

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        # Concatenate hulls (remove duplicated endpoints)
        hull = lower[:-1] + upper[:-1]
        h = len(hull)

        if h < 3:
            hull = points
            h = len(hull)

        # Triangle Area helper function
        def area(p1, p2, p3):
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1])
                + p2[0] * (p3[1] - p1[1])
                + p3[0] * (p1[1] - p2[1])
            )

        # Step 2: Two/Three Pointers on Convex Hull
        max_area = 0.0
        for i in range(h):
            k = (i + 2) % h
            for j in range(i + 1, h):
                while area(hull[i], hull[j], hull[k]) < area(
                    hull[i], hull[j], hull[(k + 1) % h]
                ):
                    k = (k + 1) % h
                max_area = max(max_area, area(hull[i], hull[j], hull[k]))

        return max_area