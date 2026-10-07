# Last updated: 10/7/2026, 2:47:52 PM
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def is_prime(val):
            if val < 2: return False
            if val == 2: return True
            if val % 2 == 0: return False

            for i in range(3, int(sqrt(val))+1, 2):
                if val % i == 0:
                    return False

            return True

        max_prime = 0

        for i in range(len(nums)):
            val1 = nums[i][i]
            val2 = nums[i][len(nums) - i - 1]

            if val1 > max_prime and is_prime(val1):
                max_prime = val1
            if val2 > max_prime and is_prime(val2):
                max_prime = val2

        return max_prime