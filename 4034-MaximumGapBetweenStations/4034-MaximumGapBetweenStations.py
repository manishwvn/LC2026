# Last updated: 8/20/2026, 1:52:35 AM
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        if len(skill) == 1: return 0
        
        n, m = len(skill), len(station)

        left = [0] * n
        ptr = 0
        for i in range(n):
            while station[ptr] != skill[i]:
                ptr += 1
            left[i] = ptr
            ptr += 1
        
        right = [0] * n
        ptr = m -1
        for i in range(n-1, -1, -1):
            while station[ptr] != skill[i]:
                ptr -= 1
            right[i] = ptr
            ptr -= 1
        
        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, right[i] - left[i - 1])
        return max_gap
            