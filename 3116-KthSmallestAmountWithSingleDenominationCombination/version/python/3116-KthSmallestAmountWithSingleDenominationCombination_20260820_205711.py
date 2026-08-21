# Last updated: 8/20/2026, 8:57:11 PM
1from math import gcd
2from typing import List
3
4class Solution:
5    def findKthSmallest(self, coins: List[int], k: int) -> int:
6        n = len(coins)
7        size = 1 << n
8
9        # Precompute LCM and inclusion-exclusion sign for every subset (bitmask) of coins.
10        lcm_arr = [0] * size
11        sign = [0] * size
12        for mask in range(1, size):
13            low = mask & (-mask)              # lowest set bit
14            i = low.bit_length() - 1
15            prev = mask ^ low                 # mask without that bit
16            if prev == 0:
17                lcm_arr[mask] = coins[i]
18            else:
19                l = lcm_arr[prev]
20                lcm_arr[mask] = l * coins[i] // gcd(l, coins[i])
21            sign[mask] = 1 if bin(mask).count("1") % 2 == 1 else -1
22
23        # count(x) = how many amounts in [1, x] are reachable by at least one coin,
24        # via inclusion-exclusion over subsets of coins.
25        def count(x: int) -> int:
26            total = 0
27            for mask in range(1, size):
28                total += sign[mask] * (x // lcm_arr[mask])
29            return total
30
31        lo, hi = 1, min(coins) * k   # smallest coin alone reaches k-th multiple by "hi"
32        while lo < hi:
33            mid = (lo + hi) // 2
34            if count(mid) >= k:
35                hi = mid
36            else:
37                lo = mid + 1
38        return lo