# Last updated: 8/20/2026, 1:52:11 AM
class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:

        max_green = max(lights)
        max_wait_time = 0
        for car_time in arrivalTime:
            r = car_time % period
            if r >= max_green:
                max_wait_time = max(max_wait_time, period - r)

        return max_wait_time