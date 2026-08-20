# Last updated: 8/20/2026, 2:04:53 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
         
        words = text.split(" ")
        broken = set(brokenLetters)
        count = 0
        
        for word in words:
            for char in word:
                if char in broken:
                    break  
            else:
                count += 1  
        
        return count
        