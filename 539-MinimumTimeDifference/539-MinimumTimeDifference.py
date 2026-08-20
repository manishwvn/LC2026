# Last updated: 8/20/2026, 2:11:46 AM
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        for i, time in enumerate(timePoints):
            hours, mins = time.split(':')
            total_mins = int(hours) * 60 + int(mins)
            timePoints[i] = total_mins

        timePoints.sort()
        min_diff = 1440 - timePoints[-1] + timePoints[0]
        for i in range(1, len(timePoints)):
            min_diff = min(min_diff, timePoints[i] - timePoints[i - 1])

        return min_diff