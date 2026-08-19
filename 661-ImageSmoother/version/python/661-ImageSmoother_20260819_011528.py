# Last updated: 8/19/2026, 1:15:28 AM
1class Solution:
2    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
3        m, n = len(img), len(img[0])
4        result = [[0] * n for _ in range(m)]
5
6        for i in range(m):
7            for j in range(n):
8                total = 0
9                count = 0
10
11                for di in [-1, 0, 1]:
12                    for dj in [-1, 0, 1]:
13                        ni, nj = i + di, j + dj
14                        if 0 <= ni < m and 0 <= nj < n:
15                            total += img[ni][nj]
16                            count += 1
17            
18                result[i][j] = total // count
19    
20        return result