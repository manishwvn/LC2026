# Last updated: 8/20/2026, 2:10:06 AM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        dirs = {
            'U' : [0, 1],
            'D' : [0, -1],
            'L' : [-1, 0],
            'R' : [1, 0]
        }

        result = [0, 0]
        for move in moves:
            result[0] += dirs[move][0]
            result[1] += dirs[move][1]

        return result == [0, 0]