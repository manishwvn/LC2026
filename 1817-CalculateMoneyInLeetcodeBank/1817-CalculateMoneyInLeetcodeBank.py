# Last updated: 8/20/2026, 2:00:39 AM
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        first_week = 28
        last_week = 28 + 7 * (weeks - 1) # Gaussian formula?
        result = (weeks * (first_week + last_week) // 2)
        monday = weeks + 1
        for index in range(n % 7):
            result += index + monday
        return result
        