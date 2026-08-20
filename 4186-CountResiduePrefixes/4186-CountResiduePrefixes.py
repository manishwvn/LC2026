# Last updated: 8/20/2026, 1:52:31 AM
class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        residue_count = 0
        
        for i, char in enumerate(s):
            seen.add(char)
            
            prefix_len = i + 1
            distinct_count = len(seen)
            
            if distinct_count == prefix_len % 3:
                residue_count += 1
                
        return residue_count