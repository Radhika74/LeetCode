class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF =10**30
        subarrays =[INF]*k
        subarrays[0]=0
        count=0
        ans=-10**30
        for i, x in enumerate(nums):
            count+=x
            mod=(i+1)%k
            if subarrays[mod]!=INF:
                ans = max(ans, count-subarrays[mod])
            subarrays[mod]=min(subarrays[mod],count)
        return ans
