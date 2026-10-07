# Last updated: 10/7/2026, 3:00:50 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:

        def_ip = ""

        for char in address:
            if char == ".":
                def_ip += "[.]"
            else:
                def_ip += char
        return def_ip
        