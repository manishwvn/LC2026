# Last updated: 8/20/2026, 2:03:54 AM
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        result = []
        products.sort()
        
        l, r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            char = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
                
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1
                
            result.append([])
            rem = r - l + 1
            
            for j in range(min(3, rem)):
                result[-1].append(products[l+j])
                
        return result
                
                