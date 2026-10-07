# Last updated: 10/7/2026, 2:54:30 PM
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
        
        
        