# Last updated: 10/7/2026, 3:03:09 PM
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hm = {}
        
        for i, char in enumerate(order):
            hm[char] = i
            
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                
                if word1[j] != word2[j]:
                    if hm[word2[j]] < hm[word1[j]]:
                        return False
                    
                    break
                    
        return True
        