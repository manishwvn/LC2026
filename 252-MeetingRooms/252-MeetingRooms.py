# Last updated: 8/20/2026, 2:14:59 AM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i+1][0] < intervals[i][1]:
                return False

        return True
        