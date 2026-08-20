# Last updated: 8/20/2026, 2:06:33 AM
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