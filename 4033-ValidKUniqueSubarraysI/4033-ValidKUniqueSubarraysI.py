# Last updated: 10/7/2026, 2:42:56 PM
class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:

        n = len(nums)
        q = len(queries)
        tag = {}
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x not in tag:
                tag[x] = random.getrandbits(64)
            pre[i + 1] = pre[i] ^ tag[x]

        bit = [0] * (n + 1)

        def add(i, d):
            i += 1
            while i <= n:
                bit[i] += d
                i += i & -i

        def psum(i):
            if i < 0:
                return 0
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        by_r = [[] for _ in range(n)]
        for idx in range(q):
            by_r[queries[idx][1]].append(idx)

        ans = [False] * q
        last = {}

        for i, x in enumerate(nums):
            if x in last:
                add(last[x], -1)
            add(i, 1)
            last[x] = i

            for idx in by_r[i]:
                l, r = queries[idx]
                if pre[r + 1] != pre[l]:
                    continue
                ans[idx] = psum(r) - psum(l - 1) == k

        return ans