# Last updated: 8/20/2026, 1:58:44 AM
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()

        res = 0

        for i in range(len(seats)):
            res += abs(seats[i]-students[i])

        return res
        