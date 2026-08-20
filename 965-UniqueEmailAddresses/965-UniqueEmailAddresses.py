# Last updated: 8/20/2026, 2:07:25 AM
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
            
            
        