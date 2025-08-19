class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, streak=0,0
        for i in nums:
            if i==0:
                streak+=1
                count+=streak
            else:
                streak=0
        return count