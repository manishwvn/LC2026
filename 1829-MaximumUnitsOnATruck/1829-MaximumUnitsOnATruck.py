# Last updated: 8/20/2026, 2:00:34 AM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        
        result = 0
        
        for box in boxTypes:
            count, units = box[0], box[1]
            count = min(truckSize, count)
            result += count * units
            truckSize -= count
            
            if truckSize == 0:
                break
                
        return result
        
        
        