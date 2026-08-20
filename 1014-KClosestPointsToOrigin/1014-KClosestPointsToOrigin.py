# Last updated: 8/20/2026, 2:07:04 AM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        def partition(points, left, right):
            pivot_index = (left + right) // 2
            pivot_dist = distance(points[pivot_index])
            points[pivot_index], points[right] = points[right], points[pivot_index]  # move pivot to end

            store_index = left
            for i in range(left, right):
                if distance(points[i]) < pivot_dist:
                    points[store_index], points[i] = points[i], points[store_index]
                    store_index += 1

            points[store_index], points[right] = points[right], points[store_index]  # move pivot to final place
            return store_index

        def quick_select(points, k):
            left, right = 0, len(points) - 1
            while left <= right:  # <-- FIXED: prevents invalid partition call
                pivot_index = partition(points, left, right)
                if pivot_index == k:
                    break
                elif pivot_index < k:
                    left = pivot_index + 1  # <-- FIXED: ensure progress
                else:
                    right = pivot_index - 1
            return points[:k]

        return quick_select(points, k)