# Last updated: 8/20/2026, 2:19:19 AM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def is_safe(board, r, c):
            #check for same column
            for i in range(r):
                if board[i][c]: return False

            #check for upper left column
            i, j = r, c
            while(i >= 0 and j >= 0):
                if board[i][j]: 
                    return False
                i -= 1
                j -= 1

            #upper right diagonal
            i, j = r, c
            while(i >= 0 and j < n):
                if board[i][j]: return False
                i -= 1
                j += 1

            return True
        
        
        if not n: return []
        if n == 1: return [["Q"]]
        
        
        board = [[False for _ in range(n)] for _ in range(n)]
        result = []
        
        def backtrack(board, r):
        #base
            if r == n:
                soln = []

                for i in range(n):
                    rowstr = ""
                    for j in range(n):
                        if board[i][j]:
                            rowstr += "Q"
                        else:
                            rowstr += "."
                    soln.append(rowstr)
                result.append(soln)
                return 
        
            #logic
            for c in range(n):
                if is_safe(board, r, c):

                    #action
                    board[r][c] = True

                    #recurse
                    backtrack(board, r + 1)

                    #backtrack
                    board[r][c] = False
        
        backtrack(board, 0)
        return result
    
    
    
    
        if not n:
            return []
    
        if n == 1:
            return [['Q']]
    
        result = []
        board = [[False for _ in range(n)] for _ in range(n)]
    
        backtrack(board, 0, result)
        return result
        