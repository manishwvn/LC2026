# Last updated: 10/7/2026, 2:54:44 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    
        counts = [0, 0]
        for s in students:
            counts[s] += 1

        rem = len(sandwiches)

        for s in sandwiches:
            if counts[s] == 0 or rem == 0:
                break
            counts[s] -= 1
            rem -= 1
        
        return rem
        
        