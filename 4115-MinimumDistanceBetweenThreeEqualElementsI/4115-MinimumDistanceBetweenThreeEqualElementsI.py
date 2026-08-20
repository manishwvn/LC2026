# Last updated: 8/20/2026, 1:52:32 AM
import collections

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        
        last_seen = {}        
        second_last_seen = {}  
        min_distance = float('inf') 

  
        for i, value in enumerate(nums):
            
            if value in second_last_seen:

                first_index = second_last_seen[value]
                current_dist = 2 * (i - first_index)
                
                min_distance = min(min_distance, current_dist)
                

                second_last_seen[value] = last_seen[value]
                last_seen[value] = i 
                
            elif value in last_seen:

                second_last_seen[value] = last_seen[value]
                last_seen[value] = i 
                
            else:

                last_seen[value] = i 

        return min_distance if min_distance != float('inf') else -1