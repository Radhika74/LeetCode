class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums)
        m=max(d.values())
        c=0
        for i in nums:
            if d[i]==m:
                c+=1
        return c