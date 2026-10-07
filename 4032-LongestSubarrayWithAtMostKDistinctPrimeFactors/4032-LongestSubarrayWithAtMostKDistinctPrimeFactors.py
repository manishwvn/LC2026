# Last updated: 10/7/2026, 2:42:10 PM
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:

        MAX_VAL = 100000
        spf = list(range(MAX_VAL + 1))
        for i in range(2, int(MAX_VAL ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX_VAL + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def prime_factors(x: int) -> list[int]:
            factors = []
            while x > 1:
                p = spf[x]
                factors.append(p)
                while x % p == 0:
                    x //= p
            return factors

        n = len(nums)
        factor_lists = [prime_factors(v) for v in nums]

        freq = {}
        distinct = 0
        left = 0
        best = 0

        for right in range(n):
            for p in factor_lists[right]:
                cnt = freq.get(p, 0)
                if cnt == 0:
                    distinct += 1
                freq[p] = cnt + 1

            while distinct > k:
                for p in factor_lists[left]:
                    freq[p] -= 1
                    if freq[p] == 0:
                        distinct -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
        