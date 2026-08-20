# Last updated: 8/20/2026, 2:04:05 AM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        #building the string without stack using two pass
        
        
        temp_str, opens = "", 0
        
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                opens += 1
                temp_str += char
                
            elif char == ")":
                if opens:
                    opens -= 1
                    temp_str += char
                    
            else:
                temp_str += char
                
        res_str, closes = "", 0
        
        for i in range(len(temp_str) - 1, -1, -1):
            char = temp_str[i]
            if char == ")":
                closes += 1
                res_str += char
                
            elif char == "(":
                if closes:
                    closes -= 1
                    res_str += char
                    
            else:
                res_str += char
        
        
        return res_str[::-1]
        