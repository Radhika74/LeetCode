class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xmax = [0]*(n+1)
        ymax = [0]*(n+1)
        xmin = [1<<31]*(n+1)
        ymin = [1<<31]*(n+1)
        for x,y in buildings:
           xmin[y]=min(xmin[y],x)
           xmax[y]=max(xmax[y],x)
           ymin[x]=min(ymin[x],y)
           ymax[x]=max(ymax[x],y)

        count=0
        for x,y in buildings:
           coverx=(xmin[y]<x & x<xmax[y]) 
           covery=(ymin[x]<y & y<ymax[x])
           count+=(coverx & covery)
        return count