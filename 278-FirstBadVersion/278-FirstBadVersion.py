# Last updated: 8/20/2026, 2:14:39 AM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1

            else:
                l = mid + 1
        
        return l