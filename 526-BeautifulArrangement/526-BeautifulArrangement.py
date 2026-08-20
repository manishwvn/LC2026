# Last updated: 8/20/2026, 2:11:56 AM
class Solution:
    def countArrangement(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        count = 0
        counts = set()
        
        def helper(pos, counts):
            nonlocal count
            
            if len(counts) == n:
                count += 1
                
            
            for i in range(1, n+1):
                if (i not in counts) and (pos % i == 0 or i % pos == 0):
                    counts.add(i)
                    
                    helper(pos+1, counts)
                    
                    counts.remove(i)
        
        helper(1, counts)
        return count
        