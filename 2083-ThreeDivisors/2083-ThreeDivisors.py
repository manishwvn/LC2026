# Last updated: 8/20/2026, 1:59:11 AM
class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n**0.5)
        
        # Must be a perfect square greater than 1
        if root * root != n or root < 2:
            return False
            
        # Sieve of Eratosthenes up to 'root'
        is_prime = [True] * (root + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(root**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, root + 1, i):
                    is_prime[j] = False  # Mark multiples as non-prime
                    
        return is_prime[root]