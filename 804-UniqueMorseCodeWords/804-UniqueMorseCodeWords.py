# Last updated: 10/7/2026, 3:05:03 PM
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