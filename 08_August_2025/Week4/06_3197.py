from typing import List

class Solution:

    # 🔹 Helper function: bounding rectangle area in a subgrid
    def minimumSum2(self, grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
        n, m = len(grid), len(grid[0])
        min_i, max_i = n, -1
        min_j, max_j = m, -1

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)

        if max_i == -1:  # no '1' found
            return 10**9   # INF
        return (max_i - min_i + 1) * (max_j - min_j + 1)

    # 🔹 Rotate grid 90° clockwise
    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ret = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ret[j][n - 1 - i] = grid[i][j]
        return ret

    # 🔹 Core solver (one orientation)
    def solve(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = n * m

        # Case 1: L-shaped partitions
        for i in range(n - 1):
            for j in range(m - 1):
                res = min(res,
                          self.minimumSum2(grid, 0, i, 0, m - 1) +
                          self.minimumSum2(grid, i + 1, n - 1, 0, j) +
                          self.minimumSum2(grid, i + 1, n - 1, j + 1, m - 1))
                res = min(res,
                          self.minimumSum2(grid, 0, i, 0, j) +
                          self.minimumSum2(grid, 0, i, j + 1, m - 1) +
                          self.minimumSum2(grid, i + 1, n - 1, 0, m - 1))

        # Case 2: Horizontal 3 bands
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(res,
                          self.minimumSum2(grid, 0, i, 0, m - 1) +
                          self.minimumSum2(grid, i + 1, j, 0, m - 1) +
                          self.minimumSum2(grid, j + 1, n - 1, 0, m - 1))
        return res

    # 🔹 Main entry point
    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.solve(grid), self.solve(self.rotate(grid)))
