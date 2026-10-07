# Last updated: 10/7/2026, 2:56:38 PM
class Solution:
    def average(self, salary: List[int]) -> float:

        n = len(salary)
        minm, maxm = min(salary), max(salary)

        return (sum(salary) - minm - maxm) / (n - 2)
        