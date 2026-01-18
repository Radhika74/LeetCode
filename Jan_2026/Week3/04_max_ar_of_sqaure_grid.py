class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        hBars.sort()
        vBars.sort()
        hcrr=2
        hmx=2
        for i in range(1,len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                hcrr+=1
            else:
                hcrr=2
            hmx=max(hmx,hcrr)
        
        vcrr=2
        vmx=2
        for i in range(1,len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                vcrr+=1
            else:
                vcrr=2
            vmx=max(vmx,vcrr)

        return min(hmx,vmx)**2
