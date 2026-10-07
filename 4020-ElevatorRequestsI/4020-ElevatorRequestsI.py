# Last updated: 10/7/2026, 2:41:50 PM
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:

        moves = 0
        curr = 0

        for req in requests:
            moves += abs(req-curr)
            curr = req

        return moves


        