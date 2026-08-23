# Last updated: 8/23/2026, 2:27:46 AM
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.indices = {}
        self.adj_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        self.diag_dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
        for row in range(self.n):
            for col in range(self.n):
                self.indices[grid[row][col]] = (row, col)
        

    def adjacentSum(self, value: int) -> int:
        r, c = self.indices[value]
        neigh_sum = 0
        for dr, dc in self.adj_dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < self.n and 0 <= nc < self.n:
                neigh_sum += self.grid[nr][nc]
        return neigh_sum

    def diagonalSum(self, value: int) -> int:

        r, c = self.indices[value]
        diag_sum = 0
        for dr, dc in self.diag_dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < self.n and 0 <= nc < self.n:
                diag_sum += self.grid[nr][nc]
        return diag_sum

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)