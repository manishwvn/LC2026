# Last updated: 10/7/2026, 2:42:55 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        frnds = set(friends)
        res = []

        for id in order:
            if id in frnds:
                res.append(id)

        return res
        