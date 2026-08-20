# Last updated: 8/20/2026, 2:16:14 AM
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dna = set()
        result = set()
        
        for i in range(len(s) - 9):
            curr = s[i:i+10]
            if curr in dna:
                result.add(curr)
            dna.add(curr)
            
        return list(result)