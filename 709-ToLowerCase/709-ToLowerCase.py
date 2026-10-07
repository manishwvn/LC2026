# Last updated: 10/7/2026, 3:06:00 PM
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for char in s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + ord('a') - ord('A'))
            else:
                result += char
        
        return result