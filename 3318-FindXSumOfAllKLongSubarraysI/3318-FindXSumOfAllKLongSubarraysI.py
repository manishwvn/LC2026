# Last updated: 10/7/2026, 2:44:41 PM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = Counter(window)

            # Sort by frequency (descending), then by value (descending)
            top_x = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))

            total = 0
            count = 0
            for val, f in top_x:
                if count < x:
                    total += val * f
                    count += 1
                else:
                    break

            result.append(total)

        return result