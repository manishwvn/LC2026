# Last updated: 10/7/2026, 2:43:42 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if j in used:
                    continue
                if fruits[i] <= baskets[j]:
                    used.add(j)
                    break

            if len(used) == len(baskets):
                break

        return len(fruits) - len(used)