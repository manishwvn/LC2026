# Last updated: 8/21/2026, 12:18:46 AM
from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        size = 1 << n

        # Precompute LCM and inclusion-exclusion sign for every subset (bitmask) of coins.
        lcm_arr = [0] * size
        sign = [0] * size
        for mask in range(1, size):
            low = mask & (-mask)              # lowest set bit
            i = low.bit_length() - 1
            prev = mask ^ low                 # mask without that bit
            if prev == 0:
                lcm_arr[mask] = coins[i]
            else:
                l = lcm_arr[prev]
                lcm_arr[mask] = l * coins[i] // gcd(l, coins[i])
            sign[mask] = 1 if bin(mask).count("1") % 2 == 1 else -1

        # count(x) = how many amounts in [1, x] are reachable by at least one coin,
        # via inclusion-exclusion over subsets of coins.
        def count(x: int) -> int:
            total = 0
            for mask in range(1, size):
                total += sign[mask] * (x // lcm_arr[mask])
            return total

        lo, hi = 1, min(coins) * k   # smallest coin alone reaches k-th multiple by "hi"
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo