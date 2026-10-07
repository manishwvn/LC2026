# Last updated: 10/7/2026, 2:42:58 PM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        
        def solve(start1, duration1, start2, duration2):
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i]+duration1[i])
            
            finish2 = inf
            for i in range(len(start2)):
                finish2 = min(finish2, max(start2[i], finish1) + duration2[i])
            return finish2

        lw = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        wl = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(lw, wl)