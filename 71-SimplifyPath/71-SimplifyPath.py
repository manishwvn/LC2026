# Last updated: 8/20/2026, 2:18:47 AM
class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        
        return "/" + "/".join(stack)