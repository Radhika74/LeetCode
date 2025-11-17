class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        count=-1
        for i in range(0,n):
            if nums[i]==1:
                if count!= -1 and i-count -1<k:
                   return False
                count=i
        return True