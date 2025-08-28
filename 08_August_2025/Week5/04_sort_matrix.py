class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
     for k in range(len(grid)):
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if i<j and i+1<len(grid) and j+1<len(grid):
                    if grid[i][j]>grid[i+1][j+1]:
                        grid[i][j],grid[i+1][j+1]=grid[i+1][j+1],grid[i][j]
                elif i+1<len(grid) and j+1<len(grid):
                    if grid[i][j]<grid[i+1][j+1]:
                        grid[i][j],grid[i+1][j+1]=grid[i+1][j+1],grid[i][j]
     return grid