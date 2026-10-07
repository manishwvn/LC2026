# Last updated: 10/7/2026, 2:42:07 PM
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
            
        