# Last updated: 10/7/2026, 3:02:15 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = ""
        depth = 0

        for char in s:
            if char == '(':
                if depth:
                    res += char
                depth += 1
            else:
                depth -= 1
                if depth:
                    res += char

        return res