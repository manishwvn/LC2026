# Last updated: 8/20/2026, 2:07:34 AM
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        if not board or len(board) == 0: return 0
        
        n = len(board)
        
        moves = [0] * (n * n)
        
        idx = 0
        even = 0
        i = n - 1
        j = 0
        while idx < n * n :
            if board[i][j] == -1:
                moves[idx] = board[i][j]
                
            else:
                moves[idx] = board[i][j] - 1
                
            idx += 1
            
            if even % 2 == 0:
                j += 1
                if j == n:
                    i -= 1
                    j -= 1
                    even += 1
            
            else:
                j -= 1
                if j == -1:
                    i -= 1
                    j += 1
                    even += 1
                    
                    
        queue = deque()
        queue.append(0)
        moves[0] = -2
        result = 0
        
        while queue:
            size = len(queue)
            for level in range(size):
                curr = queue.popleft()
                if curr == n*n - 1: return result
                
                for k in range(1, 7):
                    child = curr + k
                    if child < n * n:
                        if moves[child] != -2:
                            if moves[child] == -1:
                                queue.append(child)
                            else:
                                queue.append(moves[child])
                            moves[child] = -2
            
            result += 1
            
        
        return -1
                             
                    
        
                    
        
                    
        
        