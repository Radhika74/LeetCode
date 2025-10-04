class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        A=0
        L=0
        r=n-1
        while L<r:
            A=max(A,min(height[L], height[r])*(r-L))
            if height[r]<height[L]:
                r-=1
            else: 
                L+=1
        return A