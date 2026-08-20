# Last updated: 8/20/2026, 1:52:37 AM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        frnds = set(friends)
        res = []

        for id in order:
            if id in frnds:
                res.append(id)

        return res
        