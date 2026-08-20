# Last updated: 8/20/2026, 2:04:41 AM
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # 1. Sieve of Eratosthenes to count primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        prime_count = sum(is_prime)
        non_prime_count = n - prime_count

        # 2. Compute factorials (prime_count! * non_prime_count!) modulo 10^9 + 7
        ans = 1
        for i in range(1, prime_count + 1):
            ans = (ans * i) % MOD

        for i in range(1, non_prime_count + 1):
            ans = (ans * i) % MOD

        return ans