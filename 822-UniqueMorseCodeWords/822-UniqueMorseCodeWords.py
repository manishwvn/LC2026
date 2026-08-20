# Last updated: 8/20/2026, 2:08:37 AM
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_chars = {}
        for i, char in enumerate(morse):
            morse_chars[chr(97 + i)] = char

        transformations = set()
        for word in words:
            transformation = ""
            for char in word:
                transformation += morse_chars[char]
            transformations.add(transformation)
        
        return len(transformations)