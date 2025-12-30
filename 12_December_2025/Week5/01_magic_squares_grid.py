class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])

        def isMagic(r, c):
           
            if grid[r+1][c+1] != 5:
                return False

            seen = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)

            s = sum(grid[r][c:c+3])

           
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != s:
                    return False

           
            for j in range(3):
                if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != s:
                    return False

        
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count