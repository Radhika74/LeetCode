class Solution:
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0
        nums.sort()
        ans = 10**18
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans