# Last updated: 8/20/2026, 1:52:28 AM
class Solution:
    def reverseByType(self, s: str) -> str:
        res_list = list(s)

        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                res_list[i], res_list[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            else:
                j -= 1

        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha() and not s[j].isalpha():
                res_list[i], res_list[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].isalpha():
                i += 1
            else:
                j -= 1

        return "".join(res_list)