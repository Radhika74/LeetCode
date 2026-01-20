class Solution:
    def get_num(self, n):
        i=0
        while(i<n):
            if(i | i+1 ==n):
                return i
            i+=1
        return -1
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums: 
            ans.append(self.get_num(num))
        return ans