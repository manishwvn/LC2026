# Last updated: 10/7/2026, 2:42:45 PM
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