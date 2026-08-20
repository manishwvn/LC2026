# Last updated: 8/20/2026, 2:13:53 AM
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        string = list(s)
        
        vowels = "aeiouAEIOU"
        
        l, r = 0, len(s) - 1
        
        while l < r:
            print(l, r)
            if string[l] in vowels and string[r] in vowels:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
                
            elif string[l] not in vowels:
                l += 1
                
            elif string[r] not in vowels:
                r -= 1
                
            else:
                l += 1
                r -= 1
                
                
        return "".join(string)