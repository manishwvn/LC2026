# Last updated: 8/20/2026, 1:52:25 AM
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        toggles = [0] * (101)

        for i in range(len(bulbs)):
            if toggles[bulbs[i]] == 0:
                toggles[bulbs[i]] = 1
            else:
                toggles[bulbs[i]] = 0

        res = []
        for i in range(1, 101):
            if toggles[i] == 1:
                res.append(i)

        return res



        