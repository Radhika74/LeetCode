class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        balance = [0]*n
        first = dict()
        result = 0
        for l in reversed(range(n)):
            x = nums[l]
            if x in first:
                balance[first[x]] =0
            first[x]=l
            balance[l]=1 if (x & 1) == 0 else -1
            s=0
            for r in range(l,n):
                s+= balance[r]
                if s==0:
                    result = max(result, r-l+1)
        return result 
