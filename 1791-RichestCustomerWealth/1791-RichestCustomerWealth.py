# Last updated: 8/20/2026, 2:00:46 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        m, n = len(accounts), len(accounts[0])
        maxm = 0

        for i in range(m):
            curr = sum(accounts[i])
            maxm = max(curr, maxm)

        return maxm

        