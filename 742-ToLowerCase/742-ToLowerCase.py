# Last updated: 8/20/2026, 2:09:23 AM
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for char in s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + ord('a') - ord('A'))
            else:
                result += char
        
        return result