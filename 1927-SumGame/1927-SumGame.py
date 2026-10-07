# Last updated: 10/7/2026, 2:52:59 PM
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')

        diff = left_sum - right_sum
        q_diff = right_q - left_q

        # Bob forces equality iff blank parity matches AND diff hits the exact midpoint
        if (left_q - right_q) % 2 == 0 and 2 * diff == 9 * q_diff:
            return False   # Bob wins
        return True         # Alice wins