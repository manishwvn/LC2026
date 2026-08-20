# Last updated: 8/20/2026, 1:55:50 AM
class Solution:
    def minLength(self, s: str) -> int:
        s = list(s)  # Convert string to list for in-place modification
        write = 0  # Acts like the top of a stack

        for read in range(len(s)):
            s[write] = s[read]  # Overwrite with the current character
            
            # Check if the last two characters form "AB" or "CD"
            if write > 0 and ((s[write] == 'B' and s[write - 1] == 'A') or 
                              (s[write] == 'D' and s[write - 1] == 'C')):
                write -= 1  # Remove the last two characters (equivalent to popping from stack)
            else:
                write += 1  # Move the write pointer forward
        
        return write  # The length of the modified string