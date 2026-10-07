# Last updated: 10/7/2026, 2:57:55 PM
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = collections.Counter(s), collections.Counter(t)
        steps = 0
        
        for c in c1:
            steps += max(0,(c1[c] - c2[c]))
        
        return steps
                
        