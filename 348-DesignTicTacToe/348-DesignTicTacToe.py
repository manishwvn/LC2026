# Last updated: 8/20/2026, 2:13:48 AM
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.rev_diag = 0
        self.n = n
        
        

    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.rows[row] +=add
        self.cols[col] +=add
        if row == col:
            self.diag += add
        if row + col == self.n-1:
            self.rev_diag +=add
        
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.rev_diag) == self.n:
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)