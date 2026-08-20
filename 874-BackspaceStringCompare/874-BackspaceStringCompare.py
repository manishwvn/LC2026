# Last updated: 8/20/2026, 2:08:14 AM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def valid_char(string, index):
            backspace = 0

            while index >= 0:
                if backspace == 0 and string[index] != '#':
                    break
                elif string[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index
        
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = valid_char(s, i)
            j = valid_char(t, j)

            char_s = s[i] if i >= 0 else ""
            char_t = t[j] if j >= 0 else ""

            if char_s != char_t:
                return False
            i -= 1
            j -= 1
        return True       