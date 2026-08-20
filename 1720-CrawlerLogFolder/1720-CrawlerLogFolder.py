# Last updated: 8/20/2026, 2:01:23 AM
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0

        for s in logs:
            if s == "../":
                if count > 0:
                    count -= 1
            elif s == "./":
                continue
            else:
                count += 1

        return count