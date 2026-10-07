# Last updated: 10/7/2026, 2:50:44 PM
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        start, end = s.split(":")
        row_1, row_2 = int(start[1]), int(end[1])
        col_1, col_2 = ord(start[0]), ord(end[0])
        result = []
        
        for i in range(col_1, col_2 + 1):
            for j in range(row_1, row_2 +1):
                result.append(chr(i) + str(j))
                
        return result
        