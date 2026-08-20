# Last updated: 8/20/2026, 2:12:26 AM
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Clean and uppercase all alphanumerics
        cleaned = [ch.upper() for ch in s if ch.isalnum()]
        
        # Reverse for easier grouping from end
        cleaned.reverse()
        
        # Group characters into parts of size k
        res = []
        for i in range(0, len(cleaned), k):
            res.append(''.join(cleaned[i:i+k]))
        
        # Join with '-' and reverse the full string
        return '-'.join(res)[::-1]