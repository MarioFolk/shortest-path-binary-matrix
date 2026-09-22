from collections import deque
from typing import List

class Solution:
    """LeetCode 1091 - Shortest Path in Binary Matrix"""
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            r, c, length = q.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, length + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))           # 2
    print(sol.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))  # 4
    print(sol.shortestPathBinaryMatrix([[1,0],[0,0]]))           # -1
    print(sol.shortestPathBinaryMatrix([[0]]))                   # 1
