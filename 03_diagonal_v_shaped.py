class Solution:
    def longestVPath(self, grid):
        n, m = len(grid), len(grid[0])
        dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]   # ↘, ↙, ↖, ↗
        clockwise = {0:1, 1:2, 2:3, 3:0}

        def expected(k):   # sequence pattern
            if k==1: return 1
            return 2 if k%2==0 else 0

        from functools import lru_cache
        @lru_cache(None)
        def dfs(r,c,d,turn,k):
            best = k
            dr,dc = dirs[d]
            nr,nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and grid[nr][nc]==expected(k+1):
                best = max(best, dfs(nr,nc,d,turn,k+1))
            if not turn:   # try clockwise turn
                nd = clockwise[d]
                dr,dc = dirs[nd]
                nr,nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==expected(k+1):
                    best = max(best, dfs(nr,nc,nd,1,k+1))
            return best

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    for d in range(4):
                        ans = max(ans, dfs(i,j,d,0,1))
        return ans
