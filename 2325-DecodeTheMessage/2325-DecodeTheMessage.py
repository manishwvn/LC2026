# Last updated: 10/7/2026, 2:49:53 PM
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key_map = {}
        
        for char in key:
            if char != ' ' and char not in key_map:
                key_map[char] = chr(ord('a') + len(key_map))
                if len(key_map) == 26:
                    break
        res = []

        for char in message:
            if char == ' ':
                res.append(char)
            else:
                res.append(key_map[char])

        return "".join(res)