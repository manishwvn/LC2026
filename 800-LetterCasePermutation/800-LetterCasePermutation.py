# Last updated: 8/20/2026, 2:08:53 AM
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        result = []
        
        def helper(i, path):
            #base
            if i == len(s):
                result.append("".join(path))
                return 
            
            #logic
            if not s[i].isnumeric():
                path.append(s[i])
                helper(i+1, path)
                path.pop()
                
            if s[i].isnumeric():
                path.append(s[i])
                
            elif s[i].islower():
                path.append(s[i].upper())
            
            else:
                path.append(s[i].lower())
                
            helper(i+1, path)
            path.pop()
            
        helper(0, [])
        return result
        