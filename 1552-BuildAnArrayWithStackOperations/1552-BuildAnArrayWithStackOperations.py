# Last updated: 8/20/2026, 2:02:29 AM
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        seq = []
        curr = 1
        
        while len(stack) < len(target):
            stack.append(curr)
            seq.append("Push")
            
            # Check if stack match target
            if stack == target:
                break
            
            # If top not in target, pop
            if curr != target[len(stack) - 1]:
                stack.pop()
                seq.append("Pop")
            
            curr += 1
        
        return seq