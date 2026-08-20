# Last updated: 8/20/2026, 2:02:14 AM
class Solution:
    def average(self, salary: List[int]) -> float:

        n = len(salary)
        minm, maxm = min(salary), max(salary)

        return (sum(salary) - minm - maxm) / (n - 2)
        