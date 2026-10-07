# Last updated: 10/7/2026, 3:03:27 PM
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        unique = set()
        
        for email in emails:
            before, domain = email.split('@')
            
            local_chars = []
            for char in before:
                if char == "+":
                    break
                elif char == ".":
                    continue
                else:
                    local_chars.append(char)
                    
            local = ''.join(local_chars)
            
            final = local + '@' + domain
            unique.add(final)
            
        return len(unique)
            
            
        