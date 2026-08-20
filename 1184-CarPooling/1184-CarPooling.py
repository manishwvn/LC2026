# Last updated: 8/20/2026, 2:05:36 AM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True