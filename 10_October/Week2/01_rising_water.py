class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        def dfs(x,y,t,vis):
            if x==n-1 and y==n-1:
                return True
            vis[x][y]=True
            for dx, dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx <n and 0 <= ny<n and not vis[nx][ny] and grid[nx][ny]<=t:
                    if dfs(nx,ny,t,vis):
                        return True
            return False

        low, high, ans =0, n*n-1, float('inf')
        while low<=high:
            mid = (low+high)//2
            vis =[[False]*n for _ in range(n)]
            if grid[0][0] <=mid and dfs(0,0,mid,vis):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        

'''
For each t, the 5×5 grid prints the cell value if that cell is submerged (value ≤ t), otherwise a . (dot) means not submerged yet.

Grid reference:
[ 0,  1,  2,  3,  4]
[24, 23, 22, 21,  5]
[12, 13, 14, 15, 16]
[11, 17, 18, 19, 20]
[10,  9,  8,  7,  6]


t = 0

 0  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 1

 0  1  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 2

 0  1  2  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 3

 0  1  2  3  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 4

 0  1  2  3  4
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 5

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  .


t = 6

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  6


t = 7

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  7  6


t = 8

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
 .  .  8  7  6


t = 9

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
 .  9  8  7  6


t = 10

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
 .  .  .  .  .
10  9  8  7  6


t = 11

 0  1  2  3  4
 .  .  .  .  5
 .  .  .  .  .
11  .  .  .  .
10  9  8  7  6


t = 12

 0  1  2  3  4
 .  .  .  .  5
12  .  .  .  .
11  .  .  .  .
10  9  8  7  6


t = 13

 0  1  2  3  4
 .  .  .  .  5
12 13  .  .  .
11  .  .  .  .
10  9  8  7  6


t = 14

 0  1  2  3  4
 .  .  .  .  5
12 13 14  .  .
11  .  .  .  .
10  9  8  7  6


t = 15

 0  1  2  3  4
 .  .  .  .  5
12 13 14 15  .
11  .  .  .  .
10  9  8  7  6


t = 16

 0  1  2  3  4
 .  .  .  .  5
12 13 14 15 16
11  .  .  .  .
10  9  8  7  6

Quick notes:

At t = 16 the highlighted (non-dot) cells form a continuous swimmable path connecting (0,0) to (4,4).

For every t < 16 there is no full 4-directional path from top-left to bottom-right — hence the minimum required time is 16.
'''