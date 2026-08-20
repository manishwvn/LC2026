# Last updated: 8/20/2026, 1:52:14 AM
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:

        best_dist = float('inf')
        best_idx = -1
        for i in range(len(drones)):
            x, y, r = drones[i]
            dist = abs(x - target[0]) + abs(y - target[1])
            if dist <= r and dist < best_dist:
                best_dist = dist
                best_idx = i

        return best_idx
            
        