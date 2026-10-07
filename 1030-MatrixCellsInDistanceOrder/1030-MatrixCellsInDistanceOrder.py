# Last updated: 10/7/2026, 3:02:10 PM
class Solution:
    def get_distance(self, cell):
        return abs(cell[0] - self.rCenter) + abs(cell[1] - self.cCenter)

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        self.rCenter = rCenter
        self.cCenter = cCenter
        
        matrix = [[r, c] for r in range(rows) for c in range(cols)]
        matrix.sort(key=self.get_distance)
        return matrix