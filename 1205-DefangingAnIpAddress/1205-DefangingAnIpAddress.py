# Last updated: 8/20/2026, 2:05:28 AM
class Solution:
    def defangIPaddr(self, address: str) -> str:

        def_ip = ""

        for char in address:
            if char == ".":
                def_ip += "[.]"
            else:
                def_ip += char
        return def_ip
        