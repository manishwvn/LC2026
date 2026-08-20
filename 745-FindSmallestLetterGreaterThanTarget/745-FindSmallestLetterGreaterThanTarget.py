# Last updated: 8/20/2026, 2:09:20 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return letters[0] if l == len(letters) else letters[l]