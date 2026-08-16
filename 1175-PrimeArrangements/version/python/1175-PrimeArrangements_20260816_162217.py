# Last updated: 8/16/2026, 4:22:17 PM
1class Solution:
2    def numPrimeArrangements(self, n: int) -> int:
3        MOD = 10**9 + 7
4
5        # Helper function to check if a number is prime
6        def is_prime(num: int) -> bool:
7            if num < 2:
8                return False
9            for i in range(2, int(num**0.5) + 1):
10                if num % i == 0:
11                    return False
12            return True
13
14        # Count primes in the range [1, n]
15        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
16        non_prime_count = n - prime_count
17
18        # Compute factorials manually modulo 10^9 + 7
19        ans = 1
20        for i in range(1, prime_count + 1):
21            ans = (ans * i) % MOD
22
23        for i in range(1, non_prime_count + 1):
24            ans = (ans * i) % MOD
25
26        return ans