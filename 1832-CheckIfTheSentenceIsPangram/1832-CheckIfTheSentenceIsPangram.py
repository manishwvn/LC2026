# Last updated: 10/7/2026, 2:53:29 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        return len(set(sentence)) == 26