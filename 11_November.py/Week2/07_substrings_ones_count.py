class Solution:
    def numSub(self, s: str) -> int:
        M=10**9 + 7
        ans =0
        count =0
        for ch in s:
            if ch=='1':
                count+=1
                ans = (ans+count)%M
            else:
                count=0
        return ans 
