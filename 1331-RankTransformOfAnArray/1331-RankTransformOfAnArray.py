# Last updated: 10/7/2026, 3:00:13 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sort_arr = sorted(set(arr))
        
        ranks = defaultdict()
        
        for i, num in enumerate(sort_arr):
            ranks[num] = i+1
            
        result = [ranks[num] for num in arr]
        return result
        