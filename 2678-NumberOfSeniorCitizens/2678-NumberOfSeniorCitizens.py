# Last updated: 10/7/2026, 2:47:46 PM
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        res = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                res += 1

        return res