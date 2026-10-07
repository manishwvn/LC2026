# Last updated: 10/7/2026, 2:41:54 PM
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        g = defaultdict(list)

        for i, x in enumerate(nums):
            g[x].append(i)

        special = 0

        for idxs in g.values():
            for i in range(1, len(idxs)):
                if idxs[i] != idxs[i-1] + 1:
                    break
            else:
                special += 1

        return special