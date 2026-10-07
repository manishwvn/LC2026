# Last updated: 10/7/2026, 2:56:12 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] - mid - 1 >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo + k