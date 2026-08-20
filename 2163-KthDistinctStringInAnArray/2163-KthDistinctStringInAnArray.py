# Last updated: 8/20/2026, 1:58:36 AM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        str_map = Counter(arr)
        res_list = []

        for s in arr:
            if str_map[s] == 1:
                res_list.append(s)

        if len(res_list) < k:
            return ""

        return res_list[k-1]
        