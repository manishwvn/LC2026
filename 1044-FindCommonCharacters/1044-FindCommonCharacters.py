# Last updated: 8/20/2026, 2:06:43 AM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        min_freq = [float('inf')] * 26
        result = []
        
        for word in words:
            char_freq = [0] * 26
            
            for char in word:
                char_freq[ord(char) - ord("a")] += 1
                
            for i in range(26):
                min_freq[i] = min(min_freq[i], char_freq[i])
                
        for i in range(26):
            while min_freq[i]:
                result.append(chr(i + ord("a")))
                min_freq[i] -= 1
                
        return result
                
        