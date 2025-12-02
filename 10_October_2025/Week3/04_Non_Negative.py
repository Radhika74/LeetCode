class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq=[0]*value
        for i in nums:
            x=((i%value)+ value)% value
            freq[x]+=1
        j=0
        while True:
            x=j%value
            if freq[x]==0:
                return j
            freq[x]-=1
            j+=1