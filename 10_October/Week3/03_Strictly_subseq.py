class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 1
        l=0
        c=1
        m=0
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                m=max(m, max(c//2, min(c,l)))
                l=c
                c=1
        m=max(m, max(c//2, min(c,l)))
        return m