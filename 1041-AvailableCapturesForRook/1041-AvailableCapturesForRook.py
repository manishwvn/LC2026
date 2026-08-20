# Last updated: 8/20/2026, 2:06:46 AM
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # locate R
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    break
            else:
                continue
            break
        
        cnt = 0
        # scan up, down, left, right
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            x, y = r + dr, c + dc
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'B':  # blocked
                    break
                if board[x][y] == 'p':  # capture
                    cnt += 1
                    break
                x += dr
                y += dc
        return cnt